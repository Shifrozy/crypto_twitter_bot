# snscrape_patch.py
import importlib, pkgutil, types

def patch_snscrape_import():
    # Import just the top-level package
    snscrape = importlib.import_module("snscrape")

    # Create our own safe modules package if it doesn't already exist
    if not hasattr(snscrape, "modules"):
        snscrape.modules = types.ModuleType("snscrape.modules")
        snscrape.modules.__path__ = [str(importlib.import_module("snscrape").__path__[0] + "/modules")]

    # Define safe reimplementation of _import_modules
    def _import_modules():
        for _, moduleName, _ in pkgutil.iter_modules(snscrape.modules.__path__):
            module = importlib.import_module(f"snscrape.modules.{moduleName}")
            globals()[moduleName] = module
            setattr(snscrape.modules, moduleName, module)

    snscrape.modules._import_modules = _import_modules
    snscrape.modules._import_modules()
    return snscrape