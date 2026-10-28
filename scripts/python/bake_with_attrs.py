"""Bake геометрии в Rhino на нужный слой с User Text. Используется из GH Python-компонента в группе OUTPUT.

Входы компонента: geo (Brep), layer (str, напр. 'TUBE::40x40x2'), keys (list[str]), values (list[str]), run (bool).
Перед bake удаляет старые объекты с тем же «Обозначение» — так ревизия не плодит дубли.
"""
import Rhino
import scriptcontext as sc


def ensure_layer(doc, full_path):
    idx = doc.Layers.FindByFullPath(full_path, -1)
    if idx >= 0:
        return idx
    parent = None
    for name in full_path.split("::"):
        layer = Rhino.DocObjects.Layer()
        layer.Name = name
        if parent is not None:
            layer.ParentLayerId = doc.Layers[parent].Id
        path = name if parent is None else doc.Layers[parent].FullPath + "::" + name
        found = doc.Layers.FindByFullPath(path, -1)
        parent = found if found >= 0 else doc.Layers.Add(layer)
    return parent


def bake(geo, layer, attrs):
    doc = Rhino.RhinoDoc.ActiveDoc
    mark = attrs.get("Обозначение")
    if mark:
        for o in list(doc.Objects):
            if o.Attributes.GetUserString("Обозначение") == mark:
                doc.Objects.Delete(o, True)
    a = Rhino.DocObjects.ObjectAttributes()
    a.LayerIndex = ensure_layer(doc, layer)
    a.Name = mark or ""
    for k, v in attrs.items():
        a.SetUserString(k, str(v))
    return doc.Objects.AddBrep(geo, a)


if "run" in globals() and run:  # noqa: F821 — входы GH-компонента
    sc.doc = Rhino.RhinoDoc.ActiveDoc
    bake(geo, layer, dict(zip(keys, values)))  # noqa: F821
    sc.doc = ghdoc  # noqa: F821
