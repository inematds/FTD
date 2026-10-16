# FALHAS

| data | o que quebrou | menor correção | prompt \| infra |
|---|---|---|---|
| 2026-10-16 | Tradução FTD v2: Codex devolveu 6 trechos (blocos de código) iguais ao PT e 1 lote ES com JSON quebrado ("Extra data") | sobras.py pega PT em en/es; apagar do cache e retraduzir com LOTE menor (1500–2500) | prompt |
