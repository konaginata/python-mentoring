import importlib
import pathlib


def get_package_path(package_name):
    try:
        return str(pathlib.Path(importlib.import_module(package_name).__file__).parent)
    except ModuleNotFoundError:
        return "Package not found"
