---
name: rh-model
description: Построение или правка параметрической модели изделия в Grasshopper/Rhino по params.md — рамы из труб, листовые детали, сборки.
---
1. Прочитай ответы `docs/QUESTIONS.md` и `02_model/params.md`; нет params.md — составь и согласуй.
2. Ищи аналог: `_AI/analogs_index/INDEX.md`, `10_LIBRARY/gh_definitions`. Есть `.gh` изделия → навык `rh-revision`.
3. Структура `.gh`: PARAMS → SKELETON → узлы → OUTPUT. Слайдеры с именами из params.md.
4. Трубы — Sweep сечения из библиотеки по оси, каждая отдельный Brep; лист — с толщиной и развёрткой.
5. Bake скриптом `scripts/python/bake_with_attrs.py` (слои + User Text) в `02_model/<КОД>.3dm`.
6. Передать агенту `rh-checker`.
