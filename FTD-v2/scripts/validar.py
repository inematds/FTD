#!/usr/bin/env python3
"""Portão de qualidade do FTD v2 (PT). Confere cada src/modulos/modulo-X-Y.html contra o contrato do
CONVENTIONS.md e, se as páginas já foram montadas, o que o build gerou.
Uso: python3 scripts/validar.py [1-2 2-5 ...]   -> imprime erros por módulo; '0 erros' no fim = passou."""
import json, re, sys
from pathlib import Path
from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parents[1]
C = json.loads((ROOT / 'src/curso.json').read_text())
MODS = {m['id']: (t, m) for t in C['tracks'] for m in t['modules']}
ALL = list(MODS)


def check_module(mid):
    t, m = MODS[mid]
    cor, n = t['cor'], t['n']
    p = ROOT / 'src/modulos' / f'modulo-{mid}.html'
    if not p.exists():
        return ['arquivo ausente']
    raw = p.read_text()
    e = []
    lines = raw.count('\n')
    if lines < 450:
        e.append(f'só {lines} linhas no corpo (mínimo 450)')
    s = BeautifulSoup(raw, 'html.parser')
    main = s.find('main')
    if not main or main.get('data-inema-module') != mid or main.get('data-inema-track') != n or main.get('id') != 'conteudo':
        e.append('<main> sem id="conteudo" / data-inema-module / data-inema-track corretos')
    if s.find('script'):
        e.append('<script> dentro do módulo (o build injeta os scripts)')
    if not s.find('h1') or m['title'] not in s.find('h1').get_text():
        e.append(f'h1 não contém o título do manifesto: {m["title"]!r}')
    if not any(h.get_text(strip=True) == 'Conteúdo detalhado' for h in s.find_all('h2')):
        e.append('falta h2 "Conteúdo detalhado"')
    secs = s.select('section[data-inema-topic]')
    if len(secs) != 7:
        e.append(f'{len(secs)} tópicos (precisa 7)')
    for i, sec in enumerate(secs, 1):
        tag = f'tópico {i}'
        if sec.get('id') != f'topico-{i}' or sec.get('data-inema-topic') != f'modulo-{mid}#topico-{i}':
            e.append(f'{tag}: id/data-inema-topic errado')
        if 'scroll-margin-top' not in (sec.get('style') or ''):
            e.append(f'{tag}: sem scroll-margin-top')
        h2 = sec.find('h2')
        if not h2 or not h2.get('data-sub'):
            e.append(f'{tag}: h2 sem data-sub')
        for k in ('oque', 'porque', 'conceitos'):
            el = sec.select_one(f'[data-sum="{k}"]')
            if not el or len(el.get_text(strip=True)) < 25:
                e.append(f'{tag}: falta data-sum="{k}" com texto')
        if not sec.select_one('button[data-inema-read-toggle][aria-pressed]'):
            e.append(f'{tag}: falta botão marcar-lido')
        if not sec.select_one('button[data-inema-doubt-toggle][aria-pressed]'):
            e.append(f'{tag}: falta botão de dúvida')
        if len(sec.select('[data-inema-block]')) < 2:
            e.append(f'{tag}: menos de 2 blocos anotáveis (data-inema-block)')
        hs = [x.get_text(strip=True) for x in sec.find_all('h3')]
        if 'Por que aprender' not in hs or 'Conceitos-chave' not in hs:
            e.append(f'{tag}: faltam h3 "Por que aprender" / "Conceitos-chave"')
    blocks = [b['data-inema-block'] for b in s.select('[data-inema-block]')]
    if len(blocks) != len(set(blocks)):
        e.append('data-inema-block repetido')
    bad = [b for b in blocks if not b.startswith(f'm{mid}-t')]
    if bad:
        e.append(f'data-inema-block fora do padrão m{mid}-tT-pP: {bad[:3]}')
    toc = s.select('[data-inema-toc] a')
    if [a.get('href') for a in toc] != [f'#topico-{i}' for i in range(1, 8)]:
        e.append('TOC não tem os 7 links #topico-1..7')
    svgs = [x for x in s.find_all('svg') if x.get('role') == 'img']
    if len(svgs) < 3:
        e.append(f'{len(svgs)} SVG role="img" (mínimo 3)')
    for x in svgs:
        if not x.get('aria-label') or len(x['aria-label']) < 30:
            e.append('SVG sem aria-label descritivo')
        if x.find_parent('figure') is None or x.find_parent('figure').find('figcaption') is None:
            e.append('SVG fora de <figure> com <figcaption> "Como ler"')
    ids = [x['id'] for x in s.find_all(attrs={'id': True})]
    dup = {i for i in ids if ids.count(i) > 1}
    if dup:
        e.append(f'ids repetidos: {sorted(dup)[:5]}')
    for x in s.find_all(['marker', 'pattern', 'filter', 'linearGradient', 'lineargradient', 'radialGradient']):
        if x.get('id') and not x['id'].startswith(f'm{mid.replace("-", "")}'):
            e.append(f'id de SVG sem prefixo m{mid.replace("-", "")}: {x["id"]}')
    if len(s.select('[data-copy-box] pre')) < 1:
        e.append('nenhum bloco copia-e-cola (data-copy-box + pre)')
    if n == '1' and raw.count('Novo aqui?') < 2:
        e.append('Trilha 1: menos de 2 caixas "Novo aqui?"')
    if raw.count('✓') < 4 or raw.count('✗') < 2:
        e.append('falta grade ✓/✗')
    if any('justify-center' in ' '.join(x.get('class', [])) for x in s.find_all(['button', 'a'])) or \
       any('justify-center' in ' '.join(x.get('class', [])) and x.find(['button', 'a']) for x in s.find_all('div')):
        e.append('justify-center em botão/grupo de botões (Erro #1)')
    if '▶' in raw:
        e.append('seta ▶ (Erro #2)')
    if re.search(r'<img\b', raw):
        e.append('<img> (use SVG inline)')
    for k in ('text-', 'bg-', 'border-'):
        for other in ('emerald', 'blue', 'purple', 'amber', 'teal', 'rose'):
            if other != cor and re.search(rf'\b{k}{other}-', raw):
                e.append(f'cor de outra trilha: {k}{other}-'); break
    for a in s.find_all('a', href=True):
        h = a['href']
        if re.match(r'^(https?:|#|mailto:)', h):
            continue
        tgt = (ROOT / 'curso' / f'trilha{n}' / h.split('#')[0]).resolve()
        ok = tgt.exists() or (tgt.parent.name.startswith('trilha') and re.fullmatch(r'modulo-\d-\d\.html|index\.html', tgt.name)) or tgt == (ROOT / 'index.html').resolve()
        if not ok:
            e.append(f'link quebrado: {h}')
    return e


def main():
    ids = sys.argv[1:] or ALL
    total = 0
    for mid in ids:
        errs = check_module(mid)
        total += len(errs)
        print(f'{mid}: ' + ('OK' if not errs else f'{len(errs)} erro(s)'))
        for x in errs[:25]:
            print('   -', x)
    print(f'{total} erros')
    sys.exit(1 if total else 0)


if __name__ == '__main__':
    main()
