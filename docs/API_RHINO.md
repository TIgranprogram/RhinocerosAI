# Rhino 8 + Grasshopper — справочник API

Официально: https://developer.rhino3d.com/ (гайды) · RhinoCommon: https://developer.rhino3d.com/api/rhinocommon/ ·
rhinoscriptsyntax: https://developer.rhino3d.com/api/RhinoScriptSyntax/ · Grasshopper SDK: https://developer.rhino3d.com/api/grasshopper/ ·
rhino3dm: https://github.com/mcneel/rhino3dm · Compute: https://developer.rhino3d.com/guides/compute/

## 1. Способы подключения
| Способ | Где работает | Для чего |
|---|---|---|
| **ScriptEditor (Rhino 8)**, Python 3 / C# | внутри Rhino | основной: моделирование, экспорт, bake |
| `_-RunPythonScript "путь.py"` | командная строка / макрос / кнопка | запуск наших скриптов из `scripts/python` |
| Компоненты **Python 3 / C# Script** в GH | Grasshopper | своя логика в определении |
| **rhino3dm** (`pip install rhino3dm`) | любой Python, без Rhino | читать/писать .3dm, атрибуты, BOM — **работает и без Rhino** |
| **Rhino.Compute** / **Rhino.Inside** | сервер / другие программы | пакетный пересчёт .gh без интерфейса |
| **MCP для Rhino** (сообщество) | Rhino + Claude | прямое управление из чата — проверить на рабочем ПК |

Сторонние пакеты в Python 3 Rhino 8: первой строкой скрипта `# r: openpyxl` — Rhino установит сам.

## 2. Ключевые объекты
`Rhino.RhinoDoc.ActiveDoc` → `.Objects`, `.Layers`, `.Views`, `.ModelUnitSystem`, `.ModelAbsoluteTolerance`.
Геометрия: `Brep`, `Curve`, `Mesh`, `Point3d`, `Plane`. Атрибуты: `ObjectAttributes` (`LayerIndex`, `Name`, `SetUserString`).
`rhinoscriptsyntax as rs` — простая обёртка; `scriptcontext.doc` — текущий документ.

## 3. Команды, которые нам нужны
| Задача | Вызов |
|---|---|
| Слой | `rs.AddLayer("PART::LV-001-03", color)`; `rs.ObjectLayer(id, layer)` |
| Атрибуты (User Text) | `rs.SetUserText(id, "Обозначение", "LV-001-03")`; `rs.GetUserText(id, key)` |
| User Text документа | `rs.SetDocumentUserText(key, val)` (шапка изделия, ревизия) |
| Добавить Brep | `sc.doc.Objects.AddBrep(brep, attrs)` |
| Закрыт ли / объём | `brep.IsSolid`; `VolumeMassProperties.Compute(brep).Volume` (мм³) |
| Пересечения | `Intersection.BrepBrep(a, b, tol)` |
| Габарит | `brep.GetBoundingBox(True)` |
| Труба по оси | `Brep.CreatePipe(...)` или `Brep.CreateFromSweep(rail, section, True, tol)` |
| Развёртка листа | `Rhino.Geometry.Unroller(brep).PerformUnroll()` или команда `_UnrollSrf` |
| Контур развёртки | `brep.DuplicateNakedEdgeCurves(True, False)` → `Curve.JoinCurves` |
| Команда без диалога | `rs.Command('_-Export "C:\\path\\x.dxf" _Enter', False)` |
| Экспорт выделенного | `rs.SelectObject(id)` → `_-Export "x.step"`; схема DXF/STEP настраивается один раз |
| Сохранить | `sc.doc.WriteFile(path, Rhino.FileIO.FileWriteOptions())` |
| Снимок вида | `_-ViewCaptureToFile "x.png" _Width=1920 _Height=1080 _Enter` |
| Именованный вид | `rs.RestoreNamedView("Iso")`; `rs.ViewDisplayMode(view, "Shaded")` |
| PDF | `_-Print _Setup _Destination _Pdf ...` или `Rhino.FileIO.FilePdf` |
| Make2D | `_-Make2D ... _Enter` |

## 4. Grasshopper из скрипта
```python
import Grasshopper as gh
doc = gh.Instances.ActiveCanvas.Document
for o in doc.Objects:
    if o.NickName == "L" and hasattr(o, "Slider"):
        o.Slider.Value = 1500          # изменить параметр
doc.NewSolution(True)                  # пересчитать
```
Открыть: `rs.Command('_-Grasshopper _Document _Open "x.gh" _Enter')`.

## 5. Без Rhino (rhino3dm)
```python
import rhino3dm
m = rhino3dm.File3dm.Read("x.3dm")
for o in m.Objects:
    print(m.Layers[o.Attributes.LayerIndex].FullPath, o.Attributes.GetUserStrings())
```
Подходит для BOM, проверки атрибутов, индекса аналогов. Булевы операции, развёртка, экспорт DXF/STEP — **только в Rhino**.
