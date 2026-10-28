"""Общие функции для скриптов внутри Rhino 8 (Python 3). Импорт: from rh_utils import *"""
import os

import Rhino
import rhinoscriptsyntax as rs
import scriptcontext as sc

PROPS = ["Обозначение", "Наименование", "Материал", "Толщина/Профиль", "Кол-во"]


def project_dir():
    """Папка изделия = родитель папки, где лежит открытый .3dm (02_model)."""
    path = sc.doc.Path
    if not path:
        raise RuntimeError("Сохраните .3dm в projects/<КОД>/02_model")
    return os.path.dirname(os.path.dirname(path))


def check_units():
    if sc.doc.ModelUnitSystem != Rhino.UnitSystem.Millimeters:
        raise RuntimeError("Единицы документа должны быть мм")


def objects_on(prefix):
    """Объекты на слоях, начинающихся с prefix (напр. 'TUBE::')."""
    return [o for o in sc.doc.Objects
            if sc.doc.Layers[o.Attributes.LayerIndex].FullPath.startswith(prefix)]


def props(obj):
    return {k: obj.Attributes.GetUserString(k) or "" for k in PROPS}


def export_selected(obj_ids, path):
    rs.UnselectAllObjects()
    rs.SelectObjects(obj_ids)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    rs.Command('_-Export "{}" _Enter _Enter'.format(path), False)
    rs.UnselectAllObjects()


def safe_name(s):
    return "".join(c if c.isalnum() or c in "-_." else "_" for c in s)
