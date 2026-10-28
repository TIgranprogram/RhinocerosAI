# RhinocerosAI

**Rhino 8 + Grasshopper → полный пакет на производство одной цепочкой.**
Параметрическая модель · чертежи PDF · DXF на лазер · STEP труб в TubesT · спецификация · рендеры · техописание · паспорт.

> Главный принцип: **изделие живёт в Grasshopper и только правится.** Все размеры — слайдеры в группе `PARAMS`; поменяли цифру — геометрия, чертежи и файлы пересобрались.

---

## 🚀 Старт на рабочем ПК (с Rhino)
```bash
git clone https://github.com/TIgranprogram/RhinocerosAI.git
pip install -r requirements.txt
python scripts/python/check_setup.py
```
Все пункты `[OK]` → можно работать. В Rhino: `Tools → Options → Files → Search paths` добавить `scripts/python` (чтобы находился `rh_utils`).
Дальше скажите Claude **«что дальше?»** — он доложит по `docs/ROADMAP.md`.

---

## 📁 Структура
| Папка | Для кого | Зачем |
|---|---|---|
| `00_INBOX/` | люди | кидать всё новое без сортировки |
| `10_LIBRARY/` | люди | справочная база (см. «Что загрузить») |
| `20_TEST/` | все | песочница |
| `_AI/` | агенты | их память: знания, индекс аналогов, уроки, шаблоны ТО/паспорта |
| `projects/` | все | изделия; `_TEMPLATE` → копировать |
| `docs/` | все | регламент, вопросы, API, дорожная карта |
| `scripts/` | агенты | Python для Rhino, определения Grasshopper |

Папки изделия: `01_input` `02_model` `03_drawings_pdf` `04_dxf_laser` `05_tube_3d` `06_bom` `07_render` `08_docs_tech` `09_passport`

## 🤖 Агенты и скрипты
| Агент | Делает |
|---|---|
| **librarian** | разбирает INBOX, ищет аналоги, ведёт память `_AI` |
| **rh-designer** | строит и правит параметрические модели |
| **rh-checker** | нормоконтроль перед выдачей |
| **doc-writer** | рендеры, техописание, паспорт |

| Скрипт (`scripts/python`) | Где | Что |
|---|---|---|
| `bake_with_attrs.py` | GH | bake на слой + атрибуты, без дублей |
| `check_model.py` | Rhino | проверка: единицы, атрибуты, замкнутость, пересечения |
| `export_sheet_dxf.py` | Rhino | развёртки листа → DXF |
| `export_tubes_step.py` | Rhino | трубы по одной → STEP |
| `bom_from_3dm.py` | без Rhino | спецификация → XLSX |
| `check_setup.py` | без Rhino | готовность рабочего места |

Навыки: `rh-model` `rh-revision` `rh-drawings` `rh-export-dxf` `rh-export-tube` `rh-api` `rh-docs`

---

## ❓ Ответить людям (один раз)
Полностью — [`docs/QUESTIONS.md`](docs/QUESTIONS.md). Самое важное:
1. Версия Rhino и плагины GH; Claude пишет скрипты или управляет Rhino сам (MCP)?
2. «ToBST» = BLM TubesT? Формат: STEP / IGES / SAT?
3. Станки: труборез (макс. длина, профили), лазер (макс. лист)
4. Чертежи — в Rhino Layout или в другой программе? ЕСКД?
5. Типовые трубы и лист; K-фактор / радиусы гиба
6. Что включать в DXF (контур, отверстия, гибы, маркировка)
7. Какие размеры меняются чаще всего; изделия дизайнерские или инженерные?

## 📥 Что загрузить (в `00_INBOX` или сразу по папкам)
| Документ | Папка | Приоритет |
|---|---|---|
| Шаблон `.3dm`: мм, слои, Layout со штампом | `10_LIBRARY/standards_company` | 🔴 |
| 2–3 эталонных чертежа «как надо» (PDF) | `10_LIBRARY/drawings_examples` | 🔴 |
| Таблица гиба / K-фактор, толщины листа | `10_LIBRARY/standards_company` | 🔴 |
| Сортамент труб (кривые сечений) | `10_LIBRARY/materials_profiles` | 🔴 |
| Существующие `.gh` определения | `10_LIBRARY/gh_definitions` | 🟡 |
| Характеристики трубореза, лазера, гибочника | `10_LIBRARY/machines` | 🟡 |
| Пример файла, который принимает TubesT | `10_LIBRARY/machines` | 🟡 |
| Модели прошлых изделий `.3dm` | `10_LIBRARY/models_analogs` | 🟡 |
| Образец паспорта / ТО | `10_LIBRARY/passports_examples` | 🟢 |
| Применяемые ГОСТ | `10_LIBRARY/standards_gost` | 🟢 |

---

## 🗺 Статус
Этап 1 (каркас) — ✅ · Этап 2 (подключение Rhino) — **следующий** · Этап 3 (пилот: лавочка) · Этап 4 (автовыпуск пакета).
Подробно — [`docs/ROADMAP.md`](docs/ROADMAP.md).
