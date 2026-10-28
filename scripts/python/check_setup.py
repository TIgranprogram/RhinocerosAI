"""Проверка рабочего места: Python, rhino3dm, openpyxl, Rhino, папки. Запуск: python scripts/python/check_setup.py"""
import glob
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
ok = True


def report(name, good, hint=""):
    global ok
    ok &= good
    print(f"[{'OK' if good else '!!'}] {name}" + ("" if good else f" -> {hint}"))


report("Python 64-bit", sys.maxsize > 2**32, "нужен 64-битный Python")
for mod in ("rhino3dm", "openpyxl"):
    try:
        __import__(mod)
        report(mod, True)
    except ImportError:
        report(mod, False, "pip install -r requirements.txt")

rhino = glob.glob(r"C:\Program Files\Rhino *\System\Rhino.exe")
report("Rhino: " + (rhino[-1] if rhino else "не найден"), bool(rhino), "установить Rhino 8")

for d in ["00_INBOX", "10_LIBRARY/standards_company", "_AI/knowledge", "projects/_TEMPLATE"]:
    report(d, os.path.isdir(os.path.join(ROOT, d)), "папка отсутствует")
tpl = glob.glob(os.path.join(ROOT, "10_LIBRARY/standards_company/*.3dm"))
report("шаблон .3dm в standards_company", bool(tpl), "положить шаблон (мм, слои, Layout со штампом)")
print("\nГотово к работе." if ok else "\nЕсть пункты для исправления (см. !!).")
