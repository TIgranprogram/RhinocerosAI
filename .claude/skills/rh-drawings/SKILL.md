---
name: rh-drawings
description: Рабочие чертежи в Rhino Layout (или Make2D) из проверенной модели, штамп из User Text, экспорт PDF.
---
1. Только после PASS `rh-checker`. Шаблон Layout — из `10_LIBRARY/standards_company`.
2. Сборка: изометрия + главные виды + таблица позиций из BOM. Деталь: виды с размерами (слой `DIM`); лист — развёртка; труба — длина и углы реза.
3. Штамп — поля `%<UserText(...)>%`, руками не вписывать.
4. PDF → `03_drawings_pdf/<ОБОЗН>_<Наим>_rev<N>.pdf`.
