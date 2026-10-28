"""Развёртки всех объектов слоёв SHEET::* → DXF 1:1 в 04_dxf_laser. Запуск в Rhino: _-RunPythonScript"""
import os

import Rhino
import rhinoscriptsyntax as rs
import scriptcontext as sc
from rh_utils import check_units, export_selected, objects_on, project_dir, props, safe_name


def flat_outline(brep):
    unroller = Rhino.Geometry.Unroller(brep)
    flat, _, _, _ = unroller.PerformUnroll()
    if not flat:
        return []
    edges = flat[0].DuplicateNakedEdgeCurves(True, True)
    return Rhino.Geometry.Curve.JoinCurves(edges, sc.doc.ModelAbsoluteTolerance)


def main():
    check_units()
    out = os.path.join(project_dir(), "04_dxf_laser")
    for obj in objects_on("SHEET::"):
        p = props(obj)
        curves = flat_outline(obj.Geometry)
        if not curves or not all(c.IsClosed for c in curves):
            print("!! не развернулось / контур не замкнут:", p["Обозначение"])
            continue
        ids = [sc.doc.Objects.AddCurve(c) for c in curves]
        name = "{}_{}_{}mm_{}шт.dxf".format(p["Обозначение"], p["Материал"], p["Толщина/Профиль"], p["Кол-во"] or 1)
        export_selected(ids, os.path.join(out, safe_name(name)))
        rs.DeleteObjects(ids)
        print("OK", name)


main()
