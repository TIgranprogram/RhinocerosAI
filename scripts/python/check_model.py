"""Проверка модели в Rhino перед выдачей (агент rh-checker). Запуск в Rhino: _-RunPythonScript"""
import Rhino
import scriptcontext as sc
from rh_utils import PROPS, objects_on, props

fails = []
if sc.doc.ModelUnitSystem != Rhino.UnitSystem.Millimeters:
    fails.append("единицы не мм")

parts = objects_on("PART::") + objects_on("TUBE::") + objects_on("SHEET::")
if not parts:
    fails.append("нет объектов на слоях PART/TUBE/SHEET")
for obj in parts:
    p = props(obj)
    missing = [k for k in PROPS if not p[k] and k != "Кол-во"]
    if missing:
        fails.append("{}: нет {}".format(p["Обозначение"] or obj.Id, ", ".join(missing)))
    if isinstance(obj.Geometry, Rhino.Geometry.Brep) and not obj.Geometry.IsSolid:
        fails.append("{}: тело не замкнуто".format(p["Обозначение"]))

tol = sc.doc.ModelAbsoluteTolerance
breps = [(props(o)["Обозначение"], o.Geometry) for o in parts if isinstance(o.Geometry, Rhino.Geometry.Brep)]
for i in range(len(breps)):
    for j in range(i + 1, len(breps)):
        ok, curves, _ = Rhino.Geometry.Intersect.Intersection.BrepBrep(breps[i][1], breps[j][1], tol)
        if ok and curves and any(c.GetLength() > 1 for c in curves):
            fails.append("пересечение/касание: {} × {}".format(breps[i][0], breps[j][0]))

print("PASS" if not fails else "FAIL:\n- " + "\n- ".join(fails))
