---
name: rh-export-tube
description: Экспорт труб из Rhino по одной в STEP/IGES для BLM TubesT и трубореза.
---
1. Скрипт `scripts/python/export_tubes_step.py`: каждый Brep слоя `TUBE::*` — отдельный STEP AP214.
2. Труба — замкнутое тело, сечение из библиотеки, отверстия — реальные вырезы; длина ≤ станка.
3. Имя `<ОБОЗН>_<профиль>_L<длина>_<N>шт.step` → `05_tube_3d/`.
