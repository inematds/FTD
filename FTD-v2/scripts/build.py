#!/usr/bin/env python3
"""Monta o FTD v2 (PT) a partir de src/.
- src/curso.json      -> manifesto (idêntico em todas as páginas), nav, landing, índices
- src/landing.html    -> conteúdo do <main> da landing (index.html)
- src/trilhas/trilhaN-hero.html -> hero SVG do índice da trilha N
- src/modulos/modulo-N-Y.html   -> <main ...>...</main> de cada módulo
Os índices de trilha são GERADOS a partir dos módulos (título, data-sub e data-sum de cada tópico).
Uso: python3 scripts/build.py   (offline, sem API)"""
import json, re, html, sys
from pathlib import Path
from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / 'src'
C = json.loads((SRC / 'curso.json').read_text())
TOPICS = 7
COR_LIGHT = {'emerald': ('#047857', '4,120,87'), 'blue': ('#1d4ed8', '29,78,216'), 'purple': ('#6d28d9', '109,40,217')}
BTN = {'emerald': 'bg-emerald-700 hover:bg-emerald-600', 'blue': 'bg-blue-700 hover:bg-blue-600', 'purple': 'bg-purple-700 hover:bg-purple-600'}


def manifest():
    return {'course': C['course'], 'tracks': [
        {'n': t['n'], 'title': t['title'], 'modules': [
            {'id': m['id'], 'title': m['title'], 'topics': TOPICS,
             'href': f"curso/trilha{t['n']}/modulo-{m['id']}.html"} for m in t['modules']]}
        for t in C['tracks']]}


MANIFEST = json.dumps(manifest(), ensure_ascii=False, indent=2)
ANTIFOUC = (SRC / 'shell' / 'antifouc.html').read_text().strip()


def light_css():
    out = []
    for cor, (hexc, rgb) in COR_LIGHT.items():
        out.append(f"""    html:not(.dark) .text-{cor}-400 {{ color: {hexc}; }}
    html:not(.dark) .text-{cor}-300 {{ color: {hexc}; }}
    html:not(.dark) .hover\\:text-{cor}-400:hover {{ color: {hexc}; }}
    html:not(.dark) .bg-{cor}-500\\/20 {{ background-color: rgba({rgb},0.12); }}
    html:not(.dark) .bg-{cor}-500\\/10 {{ background-color: rgba({rgb},0.08); }}
    html:not(.dark) .hover\\:bg-{cor}-500\\/10:hover {{ background-color: rgba({rgb},0.08); }}
    html:not(.dark) .bg-{cor}-900\\/20 {{ background-color: rgba({rgb},0.07); }}
    html:not(.dark) .bg-{cor}-900\\/30 {{ background-color: rgba({rgb},0.08); }}
    html:not(.dark) .bg-{cor}-900\\/40 {{ background-color: rgba({rgb},0.09); }}
    html:not(.dark) .border-{cor}-500\\/30 {{ border-color: rgba({rgb},0.28); }}
    html:not(.dark) .hover\\:border-{cor}-500\\/30:hover {{ border-color: rgba({rgb},0.4); }}""")
    return '\n'.join(out)


def head(title, desc, rel):
    return f"""<!DOCTYPE html>
<html class="dark" lang="pt-BR">
<head>
<meta charset="utf-8"/>
<meta content="width=device-width, initial-scale=1.0" name="viewport"/>
<meta content="{C['course']}" name="inema-course"/>
<title>{html.escape(title)}</title>
<meta content="{html.escape(desc)}" name="description"/>
<meta content="{html.escape(title)}" property="og:title"/>
<meta content="{html.escape(desc)}" property="og:description"/>
<!-- ANTI-FOUC (Erro #18) — primeiro script do head -->
{ANTIFOUC}
<!-- MANIFESTO do curso (Erro #28) — idêntico em todas as páginas -->
<script data-inema-manifest="" type="application/json">
{MANIFEST}
</script>
<script src="https://cdn.tailwindcss.com"></script>
<script>
    tailwind.config = {{ darkMode: 'class', theme: {{ extend: {{ colors: {{ primary: '#FACC15', dark: {{ 900: '#0c0c10', 800: '#16161e', 700: '#1e1e28', 600: '#272730', 500: '#33333f' }} }}, fontFamily: {{ sans: ['Inter', 'system-ui', 'sans-serif'], display: ['Sora', 'Inter', 'sans-serif'], mono: ['"JetBrains Mono"', 'ui-monospace', 'monospace'] }} }} }} }}
  </script>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&amp;family=Sora:wght@600;700;800&amp;family=JetBrains+Mono:wght@400;600&amp;display=swap" rel="stylesheet"/>
<style>
    body {{ font-family: 'Inter', sans-serif; }}
    h1, h2, h3, h4, .font-display {{ font-family: 'Sora', 'Inter', sans-serif; }}
    .dark body {{ background-color: #0c0c10; }}
    .dark .text-neutral-100 {{ color: #e9e9ee; }}
    .topic-explanation {{ display: none; }}
    .topic-explanation.active {{ display: block; }}
    pre {{ white-space: pre-wrap; word-break: break-word; }}
    pre, code, .font-mono {{ font-family: 'JetBrains Mono', ui-monospace, monospace; }}

    /* Light mode — Parte 1: base */
    html:not(.dark) body {{ background-color: #f6f7f9; }}
    html:not(.dark) .bg-dark-900 {{ background-color: #ffffff; }}
    html:not(.dark) .bg-dark-800 {{ background-color: #ffffff; }}
    html:not(.dark) .bg-dark-800\\/50 {{ background-color: #f6f7f9; }}
    html:not(.dark) .bg-dark-700 {{ background-color: #eceef2; }}
    html:not(.dark) .bg-dark-700\\/50 {{ background-color: #f1f2f5; }}
    html:not(.dark) .bg-dark-700\\/30 {{ background-color: #f4f5f7; }}
    html:not(.dark) .bg-dark-600 {{ background-color: #e1e3ea; }}
    html:not(.dark) .hover\\:bg-dark-600:hover {{ background-color: #d6d9e1; }}
    html:not(.dark) .hover\\:bg-dark-700\\/50:hover {{ background-color: #eceef2; }}
    html:not(.dark) .text-neutral-100 {{ color: #1a1a22; }}
    html:not(.dark) .text-neutral-200 {{ color: #26262f; }}
    html:not(.dark) .text-neutral-300 {{ color: #3f3f4a; }}
    html:not(.dark) .text-neutral-400 {{ color: #5b5b68; }}
    html:not(.dark) .text-neutral-500 {{ color: #62626e; }}
    html:not(.dark) .border-dark-600 {{ border-color: #e1e3ea; }}
    html:not(.dark) .border-dark-700 {{ border-color: #e8e9ee; }}
    html:not(.dark) .divide-dark-600 > :not([hidden]) ~ :not([hidden]) {{ border-color: #e1e3ea; }}
    html:not(.dark) .bg-black\\/40 {{ background-color: #f1f2f5; }}
    html:not(.dark) pre.code-dark {{ background-color: #1a1a22; color: #e9e9ee; }}

    /* Light mode — Parte 2: acento das 3 trilhas (texto -700, nunca -400 no claro) */
{light_css()}

    /* Light mode — Parte 3: gradientes + especiais */
    html:not(.dark) [class*="bg-gradient-to"] {{ background-image: none !important; }}
    html:not(.dark) .text-primary {{ color: #854d0e; }}
    html:not(.dark) .text-yellow-400 {{ color: #854d0e; }}
    html:not(.dark) .hover\\:text-yellow-300:hover {{ color: #713f12; }}
    html:not(.dark) .bg-primary\\/10 {{ background-color: #FEF9C3; }}
    html:not(.dark) .border-primary\\/30 {{ border-color: #EAB308; }}
    html:not(.dark) .text-red-400 {{ color: #b91c1c; }}
    html:not(.dark) .bg-red-900\\/20 {{ background-color: rgba(185,28,28,0.07); }}
    html:not(.dark) .border-red-500\\/30 {{ border-color: rgba(185,28,28,0.25); }}
    html:not(.dark) .text-sky-400 {{ color: #0369a1; }}
    html:not(.dark) .hover\\:text-sky-300:hover {{ color: #075985; }}
    html:not(.dark) .bg-sky-900\\/20 {{ background-color: rgba(3,105,161,0.07); }}
    html:not(.dark) .border-sky-500\\/30 {{ border-color: rgba(3,105,161,0.25); }}

    /* Light mode — Parte 4: nav */
    html:not(.dark) .bg-dark-900\\/95 {{ background-color: rgba(255,255,255,0.95); }}

    /* Parte 5: bordas suavizadas no DARK (Erro #15) */
    .dark .border-dark-600 {{ border-color: #2a2a35; }}
    .dark .divide-dark-600 > :not([hidden]) ~ :not([hidden]) {{ border-color: #2a2a35; }}

    /* SVG: no claro, um fundo escuro emoldurado mantém o contraste do desenho */
    html:not(.dark) .svg-frame {{ background-color: #12121a; }}
    @media (prefers-reduced-motion: reduce) {{ svg * {{ animation: none !important; transition: none !important; }} }}
  </style>
<link href="{rel}/assets/learn.css" rel="stylesheet"/>
</head>
"""


def nav(depth, active=None):
    """depth: 'root' (landing) ou 'trilha' (curso/trilhaN/)."""
    logo = 'index.html' if depth == 'root' else '../../index.html'
    btns = []
    for t in C['tracks']:
        n, cor = t['n'], t['cor']
        if depth == 'root':
            href = f'curso/trilha{n}/index.html'
        else:
            href = 'index.html' if n == active else f'../trilha{n}/index.html'
        if n == active:
            cls = f'text-{cor}-400 bg-{cor}-500/10'
        else:
            cls = f'text-neutral-400 hover:text-{cor}-400 hover:bg-{cor}-500/10 transition-colors'
        btns.append(f'<a class="px-2.5 py-1.5 rounded-lg text-sm font-semibold {cls} whitespace-nowrap" href="{href}">\n'
                    f'<span class="lg:hidden">T{n}</span><span class="hidden lg:inline">{t["title"]}</span>\n</a>')
    return (SRC / 'shell' / 'nav.html').read_text().replace('{{LOGO}}', logo).replace('{{TRILHAS}}', '\n'.join(btns))


def footer(landing=False):
    extra = ''
    if landing:
        extra = ('\n<p class="mt-3"><a class="text-sky-400 hover:text-sky-300" href="https://www.inema.club/aprender-inteligencia-artificial/">Guia: como aprender inteligência artificial</a>'
                 ' · <a class="text-sky-400 hover:text-sky-300" href="https://www.inema.club/cursos/">Todos os cursos</a>'
                 ' · <a class="text-sky-400 hover:text-sky-300" href="https://www.inema.club/cursos/16-ftd-formacao-transformacao-digital/">Ficha do curso no INEMA.CLUB</a></p>')
    return f"""<footer class="border-t border-dark-600 py-8 mt-8">
<div class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8 text-center text-neutral-500 text-sm">
<p>FTD — Formação da Transformação Digital · conteúdo aberto e gratuito · 2026 · <a class="text-sky-400 hover:text-sky-300" href="https://inema.club" rel="noopener" target="_blank">INEMA.CLUB</a> - <a class="text-amber-700 dark:text-slate-300 hover:underline" href="https://inema.pro" rel="noopener" target="_blank">PRO</a></p>{extra}
</div>
</footer>
"""


def scripts(rel, auto_resume=False, accordion_group=False):
    group = """
      var moduleCard = button.closest('[data-module-card]');
      if (moduleCard) moduleCard.querySelectorAll('.topic-explanation.active').forEach(function (exp) {
        if (exp !== explanation) { exp.classList.remove('active'); var b = exp.closest('.topic-item').querySelector('button[aria-controls]'); if (b) b.setAttribute('aria-expanded', 'false'); }
      });""" if accordion_group else ''
    init = 'window.INEMA.init({ autoResume: true });' if auto_resume else 'window.INEMA.init();'
    return f"""<!-- SCRIPTS NÚCLEO v1 -->
<script>
    function toggleTopic(button) {{
      var topicItem = button.closest('.topic-item');
      if (!topicItem) return;
      var explanation = topicItem.querySelector('.topic-explanation');{group}
      var willOpen = !explanation.classList.contains('active');
      explanation.classList.toggle('active');
      button.setAttribute('aria-expanded', willOpen ? 'true' : 'false');
    }}
    function openModal(id) {{ var m = document.getElementById(id); if (m) {{ m.classList.remove('hidden'); document.body.style.overflow = 'hidden'; }} }}
    function closeModal() {{ document.querySelectorAll('.modal').forEach(function (m) {{ m.classList.add('hidden'); }}); document.body.style.overflow = 'auto'; }}
    document.addEventListener('keydown', function (e) {{ if (e.key === 'Escape') closeModal(); }});
    function copyCode(btn) {{
      var pre = btn.closest('[data-copy-box]').querySelector('pre');
      var txt = pre ? pre.innerText : '';
      var done = function () {{ var o = btn.getAttribute('data-label-ok') || 'Copiado'; var t = btn.textContent; btn.textContent = o; setTimeout(function () {{ btn.textContent = t; }}, 1500); }};
      try {{ navigator.clipboard.writeText(txt).then(done, done); }} catch (e) {{ done(); }}
    }}
    (function () {{
      var themeToggle = document.getElementById('theme-toggle');
      var darkIcon = document.getElementById('theme-toggle-dark-icon');
      var lightIcon = document.getElementById('theme-toggle-light-icon');
      var html = document.documentElement;
      function sync() {{ var isDark = html.classList.contains('dark'); if (darkIcon) darkIcon.classList.toggle('hidden', isDark); if (lightIcon) lightIcon.classList.toggle('hidden', !isDark); }}
      sync();
      if (themeToggle) themeToggle.addEventListener('click', function () {{
        html.classList.toggle('dark'); var nowDark = html.classList.contains('dark'); html.style.colorScheme = nowDark ? 'dark' : 'light';
        try {{ localStorage.setItem('theme', nowDark ? 'dark' : 'light'); }} catch (e) {{}}
        try {{ var p = JSON.parse(localStorage.getItem('inema.prefs') || '{{}}'); p.theme = nowDark ? 'inema-dark' : 'claro'; localStorage.setItem('inema.prefs', JSON.stringify(p)); }} catch (e) {{}}
        sync();
      }});
    }})();
  </script>
<!-- learn.js + INEMA.init() POR ÚLTIMO -->
<script src="{rel}/assets/learn.js"></script>
<script>
    if (window.INEMA && typeof window.INEMA.init === 'function') {{ {init} }}
  </script>
</body>
</html>
"""


def page(title, desc, rel, depth, active, main, landing=False, auto_resume=False, group=False, after=''):
    return (head(title, desc, rel) + '<body class="bg-dark-900 text-neutral-100 min-h-screen">\n'
            + nav(depth, active) + '\n' + main.strip() + '\n' + footer(landing) + after + scripts(rel, auto_resume, group))


def txt(el, limit=None):
    if el is None:
        return ''
    s = re.sub(r'\s+', ' ', el.get_text(' ')).strip()
    s = re.sub(r'\s+([,.;:!?)])', r'\1', s)
    if limit and len(s) > limit:
        s = s[:limit].rsplit(' ', 1)[0].rstrip(',;:') + '…'
    return s


EMOJI = re.compile(r'^([^\w\s«“"(]{1,3})\s*')


def topic_rows(mid):
    soup = BeautifulSoup((SRC / 'modulos' / f'modulo-{mid}.html').read_text(), 'html.parser')
    rows = []
    for sec in soup.select('section[data-inema-topic]'):
        h2 = sec.find('h2')
        title = txt(h2)
        m = EMOJI.match(title)
        emo, title = (m.group(1), title[m.end():]) if m else ('•', title)
        rows.append({'emo': emo, 'title': title, 'sub': h2.get('data-sub', '') if h2 else '',
                     'oque': txt(sec.select_one('[data-sum="oque"]'), 260),
                     'porque': txt(sec.select_one('[data-sum="porque"]'), 260),
                     'conceitos': txt(sec.select_one('[data-sum="conceitos"]'), 200)})
    return rows


def trilha_index(t):
    n, cor = t['n'], t['cor']
    mods = t['modules']
    total_min = sum(m['min'] for m in mods)
    hero = (SRC / 'trilhas' / f'trilha{n}-hero.html').read_text().strip()
    mapa = '\n'.join(f"""<a class="group bg-dark-800 rounded-xl border border-dark-600 hover:border-{cor}-500/30 p-5 transition-all" href="#modulo-{m['id']}">
<div class="flex items-center justify-between mb-2"><span class="text-{cor}-400 font-bold text-sm">{m['id'].replace('-', '.')}</span><span class="text-xs text-neutral-500">~{m['min']} min</span></div>
<h3 class="font-semibold mb-1 group-hover:text-{cor}-400 transition-colors">{m['emoji']} {m['title']}</h3>
<p class="text-xs text-neutral-400">{m['sub']}</p>
</a>""" for m in mods)
    cards, modais = [], []
    for m in mods:
        mid = m['id']
        dot = mid.replace('-', '.')
        items = []
        for i, r in enumerate(topic_rows(mid), 1):
            pid = f"t{mid.replace('-', '')}-{i}"
            sub = f'<span class="text-neutral-500 text-sm ml-2">- {html.escape(r["sub"])}</span>' if r['sub'] else ''
            items.append(f"""<div class="topic-item">
<button aria-controls="{pid}" aria-expanded="false" class="w-full px-6 py-4 flex items-center space-x-3 hover:bg-dark-700/50 transition-colors text-left" onclick="toggleTopic(this)">
<span class="w-6 h-6 rounded-full bg-{cor}-500/20 text-{cor}-400 text-sm font-bold flex items-center justify-center flex-shrink-0">{i}</span>
<span class="text-lg">{r['emo']}</span><div><span class="font-medium">{html.escape(r['title'])}</span>{sub}</div>
</button>
<div class="topic-explanation px-6 pb-4" id="{pid}"><div class="bg-dark-700/50 rounded-lg p-4 space-y-3 sm:ml-9">
<div><span class="text-{cor}-400 font-semibold">O que é:</span><p class="text-neutral-300 text-sm">{html.escape(r['oque'])}</p></div>
<div><span class="text-{cor}-400 font-semibold">Por que aprender:</span><p class="text-neutral-300 text-sm">{html.escape(r['porque'])}</p></div>
<div><span class="text-{cor}-400 font-semibold">Conceitos-chave:</span><p class="text-neutral-300 text-sm">{html.escape(r['conceitos'])}</p></div>
</div></div>
</div>""")
        cards.append(f"""<!-- MÓDULO {dot} -->
<div class="bg-dark-800 rounded-xl border border-dark-600 mb-6" data-module-card="" id="modulo-{mid}" style="scroll-margin-top:5rem">
<div class="p-6 border-b border-dark-600">
<div class="flex items-center justify-between mb-2">
<span class="text-{cor}-400 font-bold">{dot}</span>
<div class="flex items-center gap-3">
<span class="text-xs text-neutral-500">~{m['min']} min</span>
<div aria-label="Progresso do módulo {dot}" class="inema-ring" data-inema-meter="modulo:{mid}" style="--ring-size:2.4rem"><span class="inema-ring__value" data-inema-meter-pct="">0%</span></div>
</div>
</div>
<h3 class="text-2xl font-bold mb-2">{m['emoji']} {m['title']}</h3>
<p class="text-neutral-400 text-sm">{m['desc']}</p>
</div>
<div class="divide-y divide-dark-600">
{chr(10).join(items)}
</div>
<div class="p-4 bg-dark-700/30 flex flex-wrap justify-start gap-3">
<button class="px-4 py-2 text-sm bg-dark-600 hover:bg-dark-500 rounded-lg transition-colors" onclick="openModal('modal-{mid}')" type="button">Ver em Modal</button>
<a class="px-4 py-2 text-sm {BTN[cor]} text-white rounded-lg transition-colors" href="modulo-{mid}.html">Ver Completo</a>
</div>
</div>""")
        modais.append(f"""<div class="modal hidden fixed inset-0 z-[60] flex items-center justify-center p-2 sm:p-4 bg-black/80" id="modal-{mid}" onclick="if(event.target === this) closeModal()">
<div class="bg-dark-800 rounded-xl w-full max-w-6xl h-[95vh] flex flex-col border border-dark-600">
<div class="p-4 border-b border-dark-600 flex justify-between items-center flex-shrink-0">
<div class="flex items-center space-x-3"><span class="text-{cor}-400 font-bold">{dot}</span><span class="font-semibold">{m['title']}</span></div>
<button aria-label="Fechar" class="text-neutral-400 hover:text-neutral-100 text-2xl leading-none" onclick="closeModal()" type="button">×</button>
</div>
<iframe class="flex-1 w-full rounded-b-xl" loading="lazy" src="modulo-{mid}.html" title="Módulo {dot}"></iframe>
</div>
</div>""")
    prev_next = []
    if int(n) > 1:
        prev_next.append(f'<a class="px-5 py-3 bg-dark-700 text-neutral-300 rounded-lg font-semibold hover:bg-dark-600 transition-colors" href="../trilha{int(n)-1}/index.html">← Trilha anterior</a>')
    if int(n) < len(C['tracks']):
        prev_next.append(f'<a class="px-5 py-3 {BTN[cor]} text-white rounded-lg font-semibold transition-colors" href="../trilha{int(n)+1}/index.html">Próxima trilha →</a>')
    main = f"""<main data-inema-track="{n}" id="conteudo">
<nav aria-label="Trilha de navegação" class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8 py-4">
<div class="flex items-center space-x-2 text-sm text-neutral-400">
<a class="hover:text-{cor}-400" href="../../index.html">Início</a><span>/</span>
<span class="text-{cor}-400">Trilha {n} · {t['title']}</span>
</div>
</nav>
<header class="bg-gradient-to-br from-{cor}-900/30 via-dark-800 to-dark-800 py-12 border-b border-dark-600">
<div class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8">
<span class="inline-block px-3 py-1 bg-{cor}-500/20 text-{cor}-400 text-xs font-semibold rounded-full mb-4">TRILHA {n}</span>
<h1 class="text-3xl sm:text-4xl font-bold mb-4">{t['emoji']} {t['titulo']}</h1>
<p class="text-lg text-neutral-400 max-w-3xl">{t['desc']}</p>
<div class="grid grid-cols-2 sm:grid-cols-4 gap-4 mt-8 max-w-2xl">
<div class="bg-dark-800/50 rounded-lg p-3 border border-dark-600"><div class="text-xl font-bold text-{cor}-400">{len(mods)}</div><div class="text-xs text-neutral-400">Módulos</div></div>
<div class="bg-dark-800/50 rounded-lg p-3 border border-dark-600"><div class="text-xl font-bold text-{cor}-400">{len(mods) * TOPICS}</div><div class="text-xs text-neutral-400">Tópicos</div></div>
<div class="bg-dark-800/50 rounded-lg p-3 border border-dark-600"><div class="text-xl font-bold text-{cor}-400">~{round(total_min / 60)}h</div><div class="text-xs text-neutral-400">Duração</div></div>
<div class="bg-dark-800/50 rounded-lg p-3 border border-dark-600"><div class="text-xl font-bold text-{cor}-400">{t['nivel']}</div><div class="text-xs text-neutral-400">Nível</div></div>
</div>
<div class="flex items-center gap-3 mt-8">
<div aria-label="Progresso da Trilha {n}" class="inema-ring" data-inema-meter="trilha:{n}"><span class="inema-ring__value" data-inema-meter-pct="">0%</span></div>
<div class="inema-meter-label" data-inema-meter="trilha:{n}"><strong data-inema-meter-frac="">0 de 0</strong> tópicos lidos</div>
</div>
</div>
</header>
<div class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
{hero}
<section class="mb-12">
<h2 class="text-2xl font-bold mb-6">Mapa da trilha</h2>
<div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4">
{mapa}
</div>
</section>
<h2 class="text-2xl font-bold mb-6">Conteúdo detalhado</h2>
{chr(10).join(cards)}
<div class="flex flex-wrap justify-start gap-4 mt-10">
{chr(10).join(prev_next)}
</div>
</div>
</main>"""
    return page(f"Trilha {n} · {t['title']} | FTD v2", t['desc'], '../..', 'trilha', n, main,
                group=True, after='<!-- MODAIS (iframe carrega a página completa do módulo) -->\n' + '\n'.join(modais) + '\n')


def module_page(t, m):
    body = (SRC / 'modulos' / f"modulo-{m['id']}.html").read_text()
    return page(f"Módulo {m['id'].replace('-', '.')} · {m['title']} | FTD v2", m['desc'], '../..', 'trilha', t['n'], body, auto_resume=True)


def main():
    only = set(sys.argv[1:])
    built, missing = 0, []
    for t in C['tracks']:
        d = ROOT / 'curso' / f"trilha{t['n']}"
        d.mkdir(parents=True, exist_ok=True)
        ok = True
        for m in t['modules']:
            src = SRC / 'modulos' / f"modulo-{m['id']}.html"
            if not src.exists():
                missing.append(m['id']); ok = False; continue
            if only and m['id'] not in only:
                continue
            (d / f"modulo-{m['id']}.html").write_text(module_page(t, m)); built += 1
        if ok and (SRC / 'trilhas' / f"trilha{t['n']}-hero.html").exists():
            (d / 'index.html').write_text(trilha_index(t)); built += 1
    if (SRC / 'landing.html').exists():
        (ROOT / 'index.html').write_text(page(C['nome'] + ' | FTD v2 · INEMA.CLUB',
            'Curso aberto e gratuito em três níveis — Iniciante, Técnico e Masterclass — para entender, usar e construir com inteligência artificial.',
            '.', 'root', None, (SRC / 'landing.html').read_text(), landing=True)); built += 1
    print(f'{built} páginas montadas; faltando módulos: {missing or "nenhum"}')


if __name__ == '__main__':
    main()
