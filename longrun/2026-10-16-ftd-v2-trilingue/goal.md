# Goal — FTD refeito no formato v2, PT/EN/ES

Pedido (16/10/2026): "refaça este curso em 3 línguas e formato v2 https://inematds.github.io/FTD/FTD-Base/index.html"

## Escopo
- Novo curso em `~/projetos/FTD/FTD-v2/` (FTD-Base fica intacto). URL: https://inematds.github.io/FTD/FTD-v2/
- 3 trilhas (Iniciante=emerald, Técnico=blue, Masterclass=purple) × 9 módulos = 27 módulos, mesmos títulos do original.
- courseId `ftd-v2`. PT na raiz de FTD-v2, EN em `FTD-v2/en/`, ES em `FTD-v2/es/`.
- Tradução só por `codex exec -m gpt-6-luna` (assinatura). Nenhuma API.

## Critério de pronto (nível 3)
1. `python3 FTD-v2/scripts/validar.py` → `0 erros` (31 páginas PT: landing + 3 índices + 27 módulos; meta, anti-FOUC 1º, manifesto idêntico, nº de tópicos = manifesto, ≥500 linhas por módulo, ≥2 SVG role=img por módulo, INEMA.CLUB+PRO, "Conteúdo detalhado").
2. `python3 FTD-v2/scripts/render-locales.py` → sem "trechos sem tradução"; 31 páginas em en/ e 31 em es/.
3. `node FTD-v2/scripts/browser-check.cjs` → 0 erros JS, 0 recursos 404, sem overflow a 390px nas 93 páginas (servido por HTTP).
4. Varredura de sobras PT em en/es (palavras-sentinela) → 0 por página (exceto nomes próprios).
5. `git push` no origin; 93 URLs → HTTP 200.
