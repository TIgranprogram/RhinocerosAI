---
name: rh-export-dxf
description: Развёртки листовых деталей Rhino в DXF 1:1 для лазерной резки.
---
1. Скрипт `scripts/python/export_sheet_dxf.py`: каждый объект слоя `SHEET::*` — Unroller → контур на XY → слой `CUT` (+ `BEND` по Q11).
2. Контуры замкнуты, без дублей и мусора; мм, 1:1.
3. Имя по CLAUDE.md, количество — из User Text «Кол-во» → `04_dxf_laser/`.
4. Сверка: габарит DXF = габарит развёртки.
