import sys
import os
import re
from termcolor import colored
import argparse
import pkgutil
import plugins
import textwrap
import importlib
from tabulate import tabulate
from plugins import *
from profiles import * 

def plugins_list(ns_pkg):
	return pkgutil.iter_modules(ns_pkg.__path__)

discovered_plugins = {
	name
	for finder, name, ispkg
	in plugins_list(plugins)
}

lst_plugins=[]

for he in (discovered_plugins):
		lst_plugins.append(he)
		
_lst_plugins_a = sorted(lst_plugins)
lst_plugins_a = "\n".join(_lst_plugins_a)

moduleshelplist = []

helpstring = re.compile('""" \"""')
for lp in _lst_plugins_a:
  if lp != '__init__.py':	 
        module_name = "plugins/"+lp+".py"
        for p,profile in enumerate(open(module_name)):
            for match in re.finditer(helpstring,profile):
                _d = '%s' % (match.groups()[0])
                moduleshelplist.append(_d)


#for i in (os.listdir('plugins/')):
#   if i.endswith(".py") and i != '__init__.py':
#           _i = "plugins/" + i
#           f = open(_i,"r")
#           mystring  = f.read()
#           for item in mystring.split("\n"):
#              if '"""' in item:
#                 d = item.strip()
#                 _d = d.replace('"""','')
#                 moduleshelplist.append(_d)
_moduleshelplist = "\n".join(moduleshelplist)
_ou = [[lst_plugins_a , _moduleshelplist]]
ou = tabulate(_ou)

lp_con = []
lp_host = []
lp_img = []
pattern_profile = re.compile("###Profile (.*)\(")
for lp in _lst_plugins_a:
	module_name = "plugins/"+lp+".py"
	for p,profile in enumerate(open(module_name)):
		for match in re.finditer(pattern_profile,profile):
			_profile = '%s' % (match.groups()[0])
			if _profile == "containers":
				lp_con.append(lp)
			elif _profile == "host":
				lp_host.append(lp)
			elif _profile == "images":
				lp_img.append(lp)

def output():
	
	banner = (colored("# --------------------------------------------------------------------------------------------\n\
# CIS Docker {0} Benchmark\n\
# # {1}\n\
# --------------------------------------------------------------------------------------------\n\
	", 'green', attrs=['bold']))

	sc_ho	= (colored('Docker Host',attrs=['bold']))
	sc_im	= (colored('Docker Images',attrs=['bold']))
	sc_co   = (colored('Docker Containers',attrs=['bold']))
	sc_dockerfile = (colored('Best practices for writing Dockerfiles',attrs=['bold']))

	arguments_a = len(sys.argv) -1
	if arguments_a == 0:
		sub_version="1.2.0"
		main_version="v1.2.0 - 07-29-2019"
		print (banner .format(sub_version, main_version))
		pattern_def = re.compile("def (.*)\(")
		pattern_cls = re.compile("class (.*)\(")
		print (sc_ho)
		for lp in lp_host:
			module_name = "plugins/"+lp+".py"
			for i,line in enumerate(open(module_name)):
				for match in re.finditer(pattern_cls,line):
					cls = '%s' % (match.groups()[0])
					_cls = cls
				for match in re.finditer(pattern_def,line):
					def_name = '%s' % (match.groups()[0])
					if def_name != '__init__':
						_def = def_name
			_module_name = lp
			fun_name = _def
			_mod = "plugins."+_module_name
			mod = importlib.import_module(_mod)
			class_name = _cls
			my_class = getattr(mod, class_name)()
			result = getattr(my_class, "%s" % (fun_name))()
			print (result)
		print (sc_im)
		for lp in lp_img:
			module_name = "plugins/"+lp+".py"
			for i,line in enumerate(open(module_name)):
				for match in re.finditer(pattern_cls,line):
					cls = '%s' % (match.groups()[0])
					_cls = cls
				for match in re.finditer(pattern_def,line):
					def_name = '%s' % (match.groups()[0])
					if def_name != '__init__':
						_def = def_name
			_module_name = lp
			fun_name = _def
			_mod = "plugins."+_module_name
			mod = importlib.import_module(_mod)
			class_name = _cls
			my_class = getattr(mod, class_name)()
			result = getattr(my_class, "%s" % (fun_name))()
			print (result)
		print (sc_co)
		for lp in lp_con:
			module_name = "plugins/"+lp+".py"
			for i,line in enumerate(open(module_name)):
				for match in re.finditer(pattern_cls,line):
					cls = '%s' % (match.groups()[0])
					_cls = cls
				for match in re.finditer(pattern_def,line):
					def_name = '%s' % (match.groups()[0])
					if def_name != '__init__':
						_def = def_name
			_module_name = lp
			fun_name = _def
			_mod = "plugins."+_module_name
			mod = importlib.import_module(_mod)
			class_name = _cls
			my_class = getattr(mod, class_name)()
			result = getattr(my_class, "%s" % (fun_name))()
			print (result)

	else:
		parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter,epilog=textwrap.dedent("plugins:\n\n" + ou))
		parser.add_argument("-v", "--version", type=str , help="run for main CIS versions (currently available versions 1.2.0 , 1.1.0 , 1.0.0)")
		parser.add_argument("-sv", "--subversion", type=str , help="run for sub CIS versions  (currently available 1.0.0 sub versions 1.6, 1.11.0, 1.12.0, 1.13.0)")
		parser.add_argument("-cp", "--conprofile", type=str, help="run for configuration profiles  (currently available docker host , docker images & docker containers)")
		parser.add_argument("-f", "--files",type=str, help="check Best practices for Dockerfiles & docker-compose file")
		#parser.add_argument("-i", "--id", type=str, help="run for docker image id & docker container id")
		parser.add_argument("-p", "--plugins", type=str, help="for individually run plugins")
		#parser.add_argument("-pa", "--path", dest="filename", required=True,help="input file", metavar="FILE")
		args = parser.parse_args()
		
		if args.version:
			sub_version=args.version
			main_version=args.version
			print (banner .format(sub_version, main_version))
			lp_any = []
			pattern_def = re.compile("def (.*)\(")
			pattern_cls = re.compile("class (.*)\(")
			pattern_version = re.compile("###CIS_Version (.*)\(")
			for lp in _lst_plugins_a:
				module_name = "plugins/"+lp+".py"
				for p,profile in enumerate(open(module_name)):
					for match in re.finditer(pattern_version,profile):
						__profile = '%s' % (match.groups()[0])
						_profile = __profile.split(":")[0]
						if _profile == args.version:
							lp_any.append(lp)
			for lp in lp_any:
				module_name = "plugins/"+lp+".py"
				for i,line in enumerate(open(module_name)):
					for match in re.finditer(pattern_cls,line):
						cls = '%s' % (match.groups()[0])
						_cls = cls
					for match in re.finditer(pattern_def,line):
						def_name = '%s' % (match.groups()[0])
						if def_name != '__init__':
							_def = def_name
				_module_name = lp
				fun_name = _def
				_mod = "plugins."+_module_name
				mod = importlib.import_module(_mod)
				class_name = _cls
				my_class = getattr(mod, class_name)()
				result = getattr(my_class, "%s" % (fun_name))()
				print (result)
		
		elif args.subversion:
				sub_version=args.subversion
				main_version=args.version
				print (banner .format(sub_version, main_version))
				lp_any = []
				pattern_def = re.compile("def (.*)\(")
				pattern_cls = re.compile("class (.*)\(")
				pattern_version = re.compile("###CIS_Version (.*)\(")
				for lp in _lst_plugins_a:
					module_name = "plugins/"+lp+".py"
					for p,profile in enumerate(open(module_name)):
						for match in re.finditer(pattern_version,profile):
							__profile = '%s' % (match.groups()[0])
							_profile = __profile.split(":")[1]
							if _profile == args.subversion:
								lp_any.append(lp)
				for lp in lp_any:
					module_name = "plugins/"+lp+".py"
					for i,line in enumerate(open(module_name)):
						for match in re.finditer(pattern_cls,line):
							cls = '%s' % (match.groups()[0])
							_cls = cls
						for match in re.finditer(pattern_def,line):
							def_name = '%s' % (match.groups()[0])
							if def_name != '__init__':
								_def = def_name
					_module_name = lp
					fun_name = _def
					_mod = "plugins."+_module_name
					mod = importlib.import_module(_mod)
					class_name = _cls
					my_class = getattr(mod, class_name)()
					result = getattr(my_class, "%s" % (fun_name))()
					print (result)

		elif args.conprofile:
			lp_any = []
			pattern_def = re.compile("def (.*)\(")
			pattern_cls = re.compile("class (.*)\(")
			pattern_profile = re.compile("###Profile (.*)\(")
			for lp in _lst_plugins_a:
				module_name = "plugins/"+lp+".py"
				for p,profile in enumerate(open(module_name)):
					for match in re.finditer(pattern_profile,profile):
						_profile = '%s' % (match.groups()[0])
						if _profile == args.conprofile:
							lp_any.append(lp)
			for lp in lp_any:
				module_name = "plugins/"+lp+".py"
				for i,line in enumerate(open(module_name)):
					for match in re.finditer(pattern_cls,line):
						cls = '%s' % (match.groups()[0])
						_cls = cls
					for match in re.finditer(pattern_def,line):
						def_name = '%s' % (match.groups()[0])
						if def_name != '__init__':
							_def = def_name
				_module_name = lp
				fun_name = _def
				_mod = "plugins."+_module_name
				mod = importlib.import_module(_mod)
				class_name = _cls
				my_class = getattr(mod, class_name)()
				result = getattr(my_class, "%s" % (fun_name))()
				print (result)

		elif args.plugins:
			
			_cls = []
			_def_name = []
			_def = []
			pattern_def = re.compile("def (.*)\(")
			pattern = re.compile("class (.*)\(")
			module_name = "plugins/"+args.plugins+".py"
			for i,line in enumerate(open(module_name)):
				for match in re.finditer(pattern,line):
					cls = '%s' % (match.groups()[0])
					_cls.append(cls)
				for match in re.finditer(pattern_def,line):
					def_name = '%s' % (match.groups()[0])
					_def_name.append(def_name)
			for t in _def_name:
				if t != '__init__':
					_def.append(t)
			_module_name = args.plugins
			_def_str = str(_def)
			def_bbc = _def_str.replace("[",'')
			def_bbcdr = def_bbc.replace("]",'')
			__def = def_bbcdr.replace("'",'')
			fun_name = __def
			for mo in _lst_plugins_a:
				if mo == _module_name:
					for cl in _cls:
						_mod = "plugins."+mo
						mod = importlib.import_module(_mod)
						class_name = cl
						my_class = getattr(mod, class_name)()
						result = getattr(my_class, "%s" % (fun_name))()
						print (result)

		elif args.files == "dockerfile":
			print (sc_dockerfile)
			testcase1 = officialimage.officialimage().officialimagescan()
			print (testcase1)
			
		else:
			parser.print_help()
			
if __name__ == "__main__":
	output()

