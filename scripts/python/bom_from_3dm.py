"""Спецификация из .3dm без Rhino (rhino3dm): группирует детали по «Обозначение» → XLSX.
Запуск: python scripts/python/bom_from_3dm.py projects/<КОД>/02_model/<КОД>.3dm
"""
import os
import sys
from collections import OrderedDict

import rhino3dm
from openpyxl import Workbook

COLS = ["Обозначение", "Наименование", "Материал", "Толщина/Профиль", "Кол-во", "Слой"]


def read_bom(path):
    model = rhino3dm.File3dm.Read(path)
    if model is None:
        raise SystemExit("Не читается: " + path)
    rows = OrderedDict()
    for obj in model.Objects:
        attrs = obj.Attributes
        mark = attrs.GetUserString("Обозначение")
        if not mark:
            continue
        if mark in rows:
            rows[mark]["Кол-во"] += 1
            continue
        row = {k: attrs.GetUserString(k) or "" for k in COLS[:4]}
        row["Кол-во"] = 1
        row["Слой"] = model.Layers[attrs.LayerIndex].FullPath
        rows[mark] = row
    return list(rows.values())


def main(path):
    rows = read_bom(path)
    wb = Workbook()
    ws = wb.active
    ws.append(COLS)
    for r in rows:
        ws.append([r[c] for c in COLS])
    out_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(path))), "06_bom")
    os.makedirs(out_dir, exist_ok=True)
    out = os.path.join(out_dir, os.path.splitext(os.path.basename(path))[0] + "_BOM.xlsx")
    wb.save(out)
    print(f"{len(rows)} позиций → {out}")


if __name__ == "__main__":
    main(sys.argv[1])
