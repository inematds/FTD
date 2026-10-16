# CONVENTIONS — FTD v2 (leia antes de escrever qualquer módulo)

Curso: **FTD — Formação da Transformação Digital**, refeito no formato-curso-v2 (INEMA.CLUB), outubro de 2026.
courseId `ftd-v2`. 3 trilhas × 9 módulos. Todo módulo tem **exatamente 7 tópicos**.

## O que você escreve
Só o arquivo `src/modulos/modulo-X-Y.html`, contendo **um único `<main>…</main>`** (nada de `<html>`, `<head>`,
nav, footer ou `<script>` — o `scripts/build.py` monta a página inteira: head, anti-FOUC, manifesto, nav, footer,
scripts da camada de aprendizagem). O índice da trilha é GERADO a partir do seu módulo (h2 + `data-sub` +
`data-sum`), então esses atributos são obrigatórios.

**Padrão-ouro: `src/modulos/modulo-1-1.html`. Copie a estrutura dele, peça por peça.** Troque a cor
`emerald` pela cor da sua trilha: Trilha 1 = `emerald`, Trilha 2 = `blue`, Trilha 3 = `purple`
(classes `text-COR-400`, `bg-COR-500/20`, `border-COR-500/30`, `from-COR-900/30`, `bg-COR-900/20`,
botão "Próximo módulo" `bg-COR-700 hover:bg-COR-600`). Cor secundária permitida: `sky` (ciano). Erros: `red`.
Dica/destaque: `primary` (`bg-primary/10 border-primary/30 text-primary`). **Nunca** use cores de outra trilha.

## Contrato (o validador `python3 scripts/validar.py X-Y` confere tudo isto)
1. `<main data-inema-module="X-Y" data-inema-track="X" id="conteudo">`.
2. Breadcrumb + header (badge `MÓDULO X.Y`, `h1` = emoji + título EXATO do `src/curso.json`, parágrafo,
   4 stat cards com `7` Tópicos, minutos do curso.json, Nível, Tipo; anel `data-inema-meter="modulo:X-Y"`).
3. TOC `<nav data-inema-toc>` com 7 links `#topico-1`…`#topico-7` (texto curto).
4. `<article class="inema-prose …">` começando com `<h2 …>Conteúdo detalhado</h2>`.
5. 7 × `<section class="mb-16" data-inema-topic="modulo-X-Y#topico-N" id="topico-N" style="scroll-margin-top:5rem">`, cada uma com:
   - círculo numerado + `<h2 class="text-2xl font-bold pt-1" data-sub="subtítulo curto">EMOJI Título</h2>`;
   - botão de dúvida (`data-inema-doubt-toggle aria-pressed="false"`) no topo, botão marcar-lido
     (`data-inema-read-toggle`, os 4 spans canônicos) no fim — copie do padrão-ouro;
   - parágrafos de prosa com `data-inema-block="mX-Y-tN-pP"` (X-Y com hífen, ex. `m2-5-t3-p1`), únicos, ≥2 por tópico;
   - caixa **O que é** com `data-sum="oque"`; parágrafo **Por que aprender** (h3 exato `Por que aprender`)
     com `data-sum="porque"`; grade **Conceitos-chave** (h3 exato `Conceitos-chave`) com `data-sum="conceitos"`.
6. Resumo do módulo no fim, com "Próximo módulo" (X.Y+1, ou a próxima trilha `../trilhaN/index.html` no módulo .9;
   o 3.9 volta para `../../index.html`) e "← Voltar para a Trilha" (`index.html`).
7. **≥3 SVG** inline `role="img"` com `aria-label` descritivo (≥30 caracteres), cada um dentro de
   `<figure class="svg-frame rounded-2xl border border-COR-500/30 bg-dark-900/40 p-3 sm:p-4 mb-6">` com
   `<figcaption>` começando por `<strong class="text-COR-400">Como ler:</strong>` que ENSINA o que olhar.
   Estilo futurista: fundo de grade de pontos, cor da trilha + ciano `#38bdf8`, glow, Inter. Textos do SVG em
   cores claras (o quadro fica escuro também no tema claro). Animação só com CSS dentro de `<style>` no `<defs>`
   (o build já desliga com `prefers-reduced-motion`). **Todo `id` dentro de SVG começa com `mXY`**
   (ex.: `m25-glow`, `m25-grid`). Rótulos de texto do SVG não podem se sobrepor a linhas nem sair do viewBox.
   Ilustre cada conceito-chave que introduz uma ideia nova (o mínimo é 3; use mais quando ajudar).
8. **≥1 bloco copia-e-cola** (`data-copy-box`, igual ao padrão-ouro): **Objetivo/Experimente** + `<pre class="code-dark …">`
   com prompt, comando ou código REAL e completo (partes variáveis entre `&lt;…&gt;`) + **Como verificar**.
   Escape `<`, `>` e `&` dentro do `<pre>`. Trilha 1: prompts para assistentes (ChatGPT, Claude, Gemini).
   Trilha 2: código/comandos que rodam (Python 3, `pip install …`), de preferência **locais e gratuitos**
   (Ollama em `http://localhost:11434`, inclusive a rota compatível com OpenAI `/v1`; modelos como `llama3.2`,
   `qwen2.5`, `nomic-embed-text`), com nota de que uma API paga funciona igual trocando a URL/chave.
   Se usar Anthropic, o modelo é `claude-sonnet-5-5`. Trilha 3: mistura de configs, scripts, checklists e
   prompts de análise. Módulos práticos devem ter 2+ blocos.
9. Variedade (não repita o mesmo template 7×): ≥2 grades ✓/✗, ≥1 timeline ou passo a passo, ≥2 dicas
   (`primary`), tabelas quando comparar, cartões. Trilha 1: ≥2 caixas **"🌱 Novo aqui?"** que definem termos
   técnicos NA PRIMEIRA vez que aparecem (Trilhas 2 e 3 também definem termo novo inline, mais curto).
10. Proibido: `<script>`, `<img>`, `justify-center` em botão, seta `▶`, links para páginas que não existem,
    ids repetidos.
11. Tamanho do arquivo: **≥450 linhas** (o padrão-ouro tem ~520). Profundidade real, não enchimento.

## Conteúdo
- **Fonte**: o módulo original em `~/projetos/FTD/FTD-Base/modulos/modulo-X-Y.html` (só leia; não altere).
  Mantenha o TEMA e o título do módulo; o conteúdo é **reescrito, aprofundado e atualizado para outubro de 2026**.
  O original tem estatísticas sem fonte ("85% das empresas…", "40% mais produtivos") — **não copie números sem fonte**.
- **Sem estatística inventada.** Número só se for fato estabelecido (ex.: datas históricas, "o Transformer é de 2017").
  Na dúvida, descreva qualitativamente. Percentuais ilustrativos em diagramas devem ser marcados "(ilustrativo)".
- Ferramentas: cite as estabelecidas (ChatGPT, Claude, Gemini, Claude Code, Codex, Ollama, n8n, Make, Zapier,
  Hugging Face, PyTorch, LangGraph, MCP, pgvector, Qdrant, Chroma, Whisper, Stable Diffusion/FLUX…). Não invente
  versões, preços ou lançamentos. Avise que nomes e preços mudam; o método fica.
- Brasil: LGPD quando falar de dados pessoais. Português do Brasil, "você", voz ativa, frases curtas, sem hype
  ("revolucionar", "incrível"), sem "!!". Emoji só como ícone de título/cartão, nunca no meio da frase.
- Público: Trilha 1 leigo adulto; Trilha 2 quem programa ou está aprendendo; Trilha 3 arquitetos, líderes técnicos e gestores.
- Tópicos: 7 por módulo, cada um com uma ideia clara; "O que é" (definição concreta), "Por que aprender" (o ganho real),
  "Conceitos-chave" (4 cartões curtos).

## Como validar e ver
```bash
cd ~/projetos/FTD/FTD-v2
python3 scripts/validar.py X-Y            # tem que dar "0 erros"
python3 scripts/build.py X-Y              # monta curso/trilhaX/modulo-X-Y.html
BASE_URL=http://127.0.0.1:8941 node scripts/shot.cjs <pasta-saida> curso/trilhaX/modulo-X-Y.html
```
O servidor HTTP na porta 8941 já roda na raiz `FTD-v2/`. Abra 1–2 capturas e confira se os SVG estão legíveis
(sem texto sobreposto) e se não há overflow no celular. **Não** rode git, não faça commit, não mexa em outros
arquivos além dos seus `src/modulos/modulo-X-Y.html`.
