import importlib
import pkgutil
import plugins

def iter_namespace(ns_pkg):
	return pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + ".")

def load_plugins():
    for _, name, _ in iter_namespace(plugins):
        importlib.import_module(name)
        
load_plugins()