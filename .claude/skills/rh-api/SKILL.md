---
name: rh-api
description: Управление Rhino 8/Grasshopper через Python 3, RhinoCommon, rhinoscriptsyntax, rhino3dm. Используй перед написанием или запуском любого скрипта.
---
1. Справочник — `docs/API_RHINO.md`. Нет вызова — developer.rhino3d.com, затем допиши справочник.
2. Общие функции — в `scripts/python/rh_utils.py`; не дублируй.
3. Единицы — мм; проверить `doc.ModelUnitSystem` и допуск.
4. Команды Rhino из скрипта — только «минусовые» (`_-Export`), без диалогов.
5. Без Rhino — только `rhino3dm`. Проверка места: `python scripts/python/check_setup.py`.
