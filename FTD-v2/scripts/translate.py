#!/usr/bin/env python3
"""Traduz i18n/source.json (gerado por localization.py) para EN/ES e guarda em i18n/<lang>.json.
Motor ÚNICO: tradutor central do INEMA (`inema-traduz`, INEMA_TRADUCAO_* em ~/.config/inema/modelos.env, hoje Sonnet 5.5)
pela assinatura. Nenhuma API, nenhuma reserva.
Só envia o que ainda não está no cache; lotes em paralelo; resposta validada (ids, tipo, tamanho) antes de gravar.
Uso: python3 scripts/translate.py [en] [es]      (PARALELO=4 LOTE=5000 por variável de ambiente)"""
import json, os, re, subprocess, sys, tempfile, threading
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PARALELO = int(os.environ.get('PARALELO', '4'))
LOTE = int(os.environ.get('LOTE', '5000'))
NOME = {'en': 'clear, natural US English', 'es': 'neutral Latin American Spanish'}
LOCK = threading.Lock()

SYS = """You are a careful professional translator of an open, free AI course (INEMA.CLUB, course "FTD").
Translate EVERY value from Brazilian Portuguese into {nome}.
INPUT: a JSON object id -> {{"kind": "text"|"pre", "source": string}}. Fragments of web pages, in reading order.
OUTPUT: ONLY a JSON object with EXACTLY the same ids, each mapped to the translated STRING. No other keys, no commentary, no code fences.
RULES
- Never summarize, omit or add content. Keep every sentence, example, number and date unchanged in meaning.
- A fragment may start or end mid-sentence (it sits between HTML tags): translate just that fragment and keep its leading/trailing punctuation and spacing.
- kind "pre" is a copy-paste block (prompt, command or code). Prompts written for an AI assistant: translate them fully, keeping line breaks and placeholders like <...> (translate the words inside the placeholder). Code: keep code, identifiers, function names, keys, URLs, model names, file names and commands EXACTLY; translate only comments and human-facing strings. Shell commands stay exactly as they are.
- Keep exactly: product and model names (ChatGPT, Claude, Claude Code, Codex, Gemini, Ollama, n8n, Make, Zapier, Hugging Face, PyTorch, LangGraph, MCP, FLUX, Whisper, llama3.2, qwen2.5, nomic-embed-text, claude-sonnet-5-5), INEMA, INEMA.CLUB, PRO, FTD, URLs, e-mails, file paths, environment variables, emoji.
- Brazilian law LGPD: keep "LGPD" and, the first time it appears in a sentence, you may add the local equivalent in parentheses only if natural (e.g. "LGPD (Brazil's data protection law)"). Do not invent other laws.
- Course UI words: "Trilha" = "Track"/"Ruta", "Módulo" = "Module"/"Módulo", "Tópico" = "Topic"/"Tema", "Marcar como lido" = "Mark as read"/"Marcar como leído", "Tenho dúvida" = "I have a question"/"Tengo una duda", "Novo aqui?" = "New here?"/"¿Nuevo aquí?", "Como ler:" = "How to read:"/"Cómo leer:", "Como verificar:" = "How to check:"/"Cómo verificar:", "Copiar" = "Copy"/"Copiar".
- Tone: direct, second person ("you"/"tú"), active voice, no hype."""


_TRADUTOR = os.path.expanduser("~/projetos/wifi/scripts/inema-traduz")
def chamar_tradutor(pedido: str, timeout: int = 900) -> str:
    """Tradução pelo tradutor central do INEMA (INEMA_TRADUCAO_* em ~/.config/inema/modelos.env). Assinatura, nunca API."""
    if os.path.exists(_TRADUTOR):
        cmd = [_TRADUTOR]
    else:  # fora da máquina do Nei: Claude Code da assinatura com o modelo da variável (padrão Sonnet 5.5)
        cmd = ["claude", "-p", "--model", os.environ.get("INEMA_TRADUCAO_MODELO", "claude-sonnet-5-5"),
               "--output-format", "text", "--tools", ""]
    env = {k: v for k, v in os.environ.items() if k not in ("ANTHROPIC_API_KEY", "OPENAI_API_KEY", "CLAUDECODE")}
    with tempfile.TemporaryDirectory() as d:
        r = subprocess.run(cmd, input=pedido, capture_output=True, text=True, timeout=timeout, env=env, cwd=d)
    if r.returncode != 0 or not r.stdout.strip():
        raise RuntimeError(f"tradutor falhou rc={r.returncode}: {(r.stderr or r.stdout)[-300:]}")
    return r.stdout


def tradutor_json(prompt):
    t = re.sub(r'^```(?:json)?\s*|\s*```$', '', chamar_tradutor(prompt, timeout=1200).strip())
    return json.loads(t[t.index('{'):t.rindex('}') + 1])


def check(batch, ids, raw, lang):
    if set(raw) != set(ids):
        raise ValueError(f'ids divergentes ({len(set(ids) - set(raw))} faltando)')
    out = {ids[k]: v for k, v in raw.items()}
    for k, v in out.items():
        src = batch[k]['source']
        if not isinstance(v, str) or not v.strip():
            raise ValueError('valor vazio')
        if len(src) > 120 and len(v) < len(src) * 0.5:
            raise ValueError('tradução encurtada')
        if batch[k]['kind'] == 'pre' and src.count('\n') and abs(v.count('\n') - src.count('\n')) > max(2, src.count('\n') // 5):
            raise ValueError('quebras de linha do bloco mudaram')
        for url in re.findall(r'https?://[^\s<>"\')]+', src):
            if url not in v:
                raise ValueError(f'URL alterada: {url}')
    return out


def translate(lang):
    source = json.loads((ROOT / 'i18n/source.json').read_text())
    path = ROOT / f'i18n/{lang}.json'
    cache = json.loads(path.read_text()) if path.exists() else {}
    missing = [(k, v) for k, v in source.items() if k not in cache]
    batches, batch, size = [], {}, 0
    for k, v in missing:
        if size + len(v['source']) > LOTE and batch:
            batches.append(batch); batch, size = {}, 0
        batch[k] = v; size += len(v['source'])
    if batch:
        batches.append(batch)
    print(f'{lang}: {len(missing)} trechos faltando em {len(batches)} lotes', flush=True)
    falhas = []

    def run(idx, batch):
        ids = {str(i): k for i, k in enumerate(batch)}
        payload = json.dumps({i: batch[k] for i, k in ids.items()}, ensure_ascii=False)
        prompt = SYS.format(nome=NOME[lang]) + '\n\nINPUT JSON:\n' + payload
        for tent in range(3):
            try:
                out = check(batch, ids, tradutor_json(prompt), lang)
                with LOCK:
                    cache.update(out)
                    path.write_text(json.dumps(cache, ensure_ascii=False, indent=1) + '\n')
                    print(f'{lang} lote {idx}/{len(batches)} ok ({len(cache)} no cache)', flush=True)
                return
            except (RuntimeError, ValueError, json.JSONDecodeError, subprocess.TimeoutExpired) as e:
                print(f'{lang} lote {idx} tentativa {tent + 1} falhou: {str(e)[:160]}', flush=True)
        falhas.append(idx)

    with ThreadPoolExecutor(PARALELO) as ex:
        list(as_completed([ex.submit(run, i, b) for i, b in enumerate(batches, 1)]))
    if falhas:
        raise SystemExit(f'{lang}: lotes sem tradução {falhas} — rode de novo (o cache guarda o resto)')
    print(f'{lang}: completo', flush=True)


if __name__ == '__main__':
    for lang in sys.argv[1:] or ['en', 'es']:
        translate(lang)
