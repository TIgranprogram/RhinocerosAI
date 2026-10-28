"""Каждая труба слоёв TUBE::* → отдельный STEP в 05_tube_3d (для TubesT). Запуск в Rhino: _-RunPythonScript"""
import os

from rh_utils import check_units, export_selected, objects_on, project_dir, props, safe_name

MAX_LEN_MM = 6500  # заменить на ответ из QUESTIONS.md (макс. длина трубореза)


def main():
    check_units()
    out = os.path.join(project_dir(), "05_tube_3d")
    for obj in objects_on("TUBE::"):
        p = props(obj)
        brep = obj.Geometry
        if not brep.IsSolid:
            print("!! не замкнута:", p["Обозначение"])
            continue
        bb = brep.GetBoundingBox(True)
        length = round(max(bb.Max.X - bb.Min.X, bb.Max.Y - bb.Min.Y, bb.Max.Z - bb.Min.Z))
        if length > MAX_LEN_MM:
            print("!! длиннее станка:", p["Обозначение"], length)
        name = "{}_{}_L{}_{}шт.step".format(p["Обозначение"], p["Толщина/Профиль"], length, p["Кол-во"] or 1)
        export_selected([obj.Id], os.path.join(out, safe_name(name)))
        print("OK", name)


main()
