---
name: rh-docs
description: Визуализация и описание изделия — снимки видов, техническое описание и паспорт из атрибутов модели и BOM.
---
1. Снимки: именованные виды Iso/Front/Top, Shaded/Rendered → `_-ViewCaptureToFile` → `07_render/`.
2. Данные: User Text, объём × плотность = масса, габарит по BoundingBox, состав — `scripts/python/bom_from_3dm.py`.
3. Шаблоны `_AI/templates_text/` → `08_docs_tech/TO.md`, `09_passport/`. Нет данных — «ЗАПОЛНИТЬ».
