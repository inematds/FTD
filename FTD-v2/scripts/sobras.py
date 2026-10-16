#!/usr/bin/env python3
"""Procura português esquecido nas páginas EN/ES (texto visível, atributos e manifesto).
Marcadores que não existem em inglês nem em espanhol: ã õ ç ê, "você", "não".
Uso: python3 scripts/sobras.py   -> lista por página; '0 sobras' no fim = passou."""
import re, sys
from pathlib import Path
from bs4 import BeautifulSoup, Comment

ROOT = Path(__file__).resolve().parents[1]
PT = re.compile(r'[ãõçêÃÕÇÊ]|\bvocê\b|\bnão\b', re.I)
OK = re.compile(r'São Paulo|Inteligência Artificial \(PT\)|LGPD', re.I)
total = 0
for lang in ('en', 'es'):
    for p in sorted((ROOT / lang).rglob('*.html')):
        s = BeautifulSoup(p.read_text(), 'html.parser')
        hits = []
        for n in s.find_all(string=True):
            if isinstance(n, Comment) or n.parent.name in ('style',):
                continue
            if n.parent.name == 'script' and not n.parent.has_attr('data-inema-manifest'):
                continue
            t = str(n)
            if PT.search(t) and not OK.search(t):
                hits.append(re.sub(r'\s+', ' ', t).strip()[:90])
        for tag in s.find_all(True):
            for a in ('aria-label', 'title', 'alt', 'placeholder', 'content'):
                v = tag.get(a)
                if isinstance(v, str) and PT.search(v):
                    hits.append(f'[{a}] {v[:80]}')
        if hits:
            total += len(hits)
            print(f'{p.relative_to(ROOT)}: {len(hits)}')
            for h in hits[:6]:
                print('   ', h)
print(f'{total} sobras')
sys.exit(1 if total else 0)
