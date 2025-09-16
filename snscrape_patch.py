# snscrape_patch.py
import importlib, pkgutil, sys

def patch_snscrape_import():
    # Import root snscrape without triggering modules
    snscrape = importlib.import_module("snscrape")

    # Manually import the modules package, but stop it from auto-running
    import snscrape.modules
    # Monkey-patch its _import_modules
    def _import_modules():
        for _, moduleName, _ in pkgutil.iter_modules(snscrape.modules.__path__):
            module = importlib.import_module(f"snscrape.modules.{moduleName}")
            globals()[moduleName] = module

    snscrape.modules._import_modules = _import_modules
    snscrape.modules._import_modules()