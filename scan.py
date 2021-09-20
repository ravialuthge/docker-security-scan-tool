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

for i in (os.listdir('plugins/')):
   if i.endswith(".py") and i != '__init__.py':
           _i = "plugins/" + i
           f = open(_i,"r")
           mystring  = f.read()
           for item in mystring.split("\n"):
              if '"""' in item:
                 d = item.strip()
                 _d = d.replace('"""','')
                 moduleshelplist.append(_d)
_moduleshelplist = "\n".join(moduleshelplist)
_ou = [[lst_plugins_a , _moduleshelplist]]
ou = tabulate(_ou)

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
		print (sc_ho)
		docker_host.cis_version_host().cis_version_112()
		docker_host.cis_version_host().cis_version_111()
		docker_host.cis_version_host().cis_version_16()
		docker_host.cis_version_host().cis_version_113()
		print (sc_im)
		docker_images.cis_version_images().cis_version_16()
		docker_images.cis_version_images().cis_version_111()
		docker_images.cis_version_images().cis_version_112()
		print (sc_co)
		docker_containers.cis_version_containers().cis_version_12()
		docker_containers.cis_version_containers().cis_version_112()
		docker_containers.cis_version_containers().cis_version_111()
		
	else:
		parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter,epilog=textwrap.dedent("plugins:\n\n" + ou))
		parser.add_argument("-v", "--version", type=str , help="run for main CIS versions (currently available versions 1.2.0 , 1.1.0 , 1.0.0)")
		parser.add_argument("-sv", "--sub-version", type=str , help="run for sub CIS versions  (currently available 1.0.0 sub versions 1.6, 1.11.0, 1.12.0, 1.13.0)")
		#parser.add_argument("-pr", "--profile", type=str, help="run for configuration profiles  (currently available docker host , docker images & docker containers)")
		parser.add_argument("-f", "--files",type=str, help="check Best practices for Dockerfiles & docker-compose file")
		parser.add_argument("-i", "--id", type=str, help="run for docker image id & docker container id")
		parser.add_argument("-p", "--plugins", type=str, help="for individually run plugins")
		#parser.add_argument("-pa", "--path", dest="filename", required=True,help="input file", metavar="FILE")
		args = parser.parse_args()
		
		if args.version == "1.2.0":
			sub_version="1.2.0"
			main_version="v1.2.0 - 07-29-2019"
			print (banner .format(sub_version, main_version))
			print (sc_ho)
			testcases = apparmor.ApparmorPlugin().apparmor_scan()
			#testcases = _testcases()
			print (testcases)
			print (sc_im)
	
			print (sc_co)
			
		

		elif args.version == "1.1.0":
			sub_version="1.1.0"
			main_version="v1.1.0 - 07-06-2017"
			print (banner .format(sub_version, main_version))
			print (sc_ho)
			
			print (sc_im)
			
			print (sc_co)
		
		elif args.sub_version == "1.0.0":
			sub_version="1.6"
			main_version="v1.0.0 - 04-22-2015"
			print (banner .format(sub_version, main_version))
			print (sc_ho)
	
			print (sc_im)
		
			print (sc_co)
		

			sub_version="1.11.0"
			main_version="v1.0.0 - 04-22-2015"
			print (banner .format(sub_version, main_version))
			print (sc_ho)
		
			print (sc_im)
			
			print (sc_co)
	

			sub_version="1.12.0"
			main_version="v1.0.0 - 04-22-2015"
			print (banner .format(sub_version, main_version))
			print (sc_ho)
	
			print (sc_im)
			
			print (sc_co)
		

			sub_version="1.13.0"
			main_version="v1.0.0 - 04-22-2015"
			print (banner .format(sub_version, main_version))
			print (sc_ho)
			
			print (sc_im)
		
			print (sc_co)
		
		elif args.plugins:
			#testcases = apparmor.ApparmorPlugin().apparmor_scan()
			#print (testcases)
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
		
			_cls_str = str(_cls)
			_bbc = _cls_str.replace("[",'')
			_bbcdr = _bbc.replace("]",'')
			__cls = _bbcdr.replace("'",'')
			
			_def_str = str(_def)
			def_bbc = _def_str.replace("[",'')
			def_bbcdr = def_bbc.replace("]",'')
			__def = def_bbcdr.replace("'",'')
			
			module = args.plugins
			cls_name = __cls+"()"
			fun_name = __def+"()"
			#cls_name = __cls
			#fun_name = __def
			#function_string = module.cls_name.fun_name
			#function_string = "%s.%s.%s" % (module,cls_name,fun_name)
			_function_string = "{0}.{1}.{2}"
			function_string = _function_string .format(module,cls_name,fun_name)
			#mod_name, func_name = function_string.rsplit('.',1)
			#mod = importlib.import_module(mod_name)
			#func = getattr(mod, func_name)
			#func = importlib.import_module(function_string)
			result = str(function_string)
			#getattr(locals().get("foo") or globals().get("foo") or __import__("foo"), "bar")()
			#_testcases = testcases()
			#_testcases = getattr('apparmor',__cls,__def)()
			print (result())
		

		elif args.files == "officialimage":
			print (sc_dockerfile)
			#officialimage.officialimage().officialimagescan()
			
			
		else:
			parser.print_help()
			
if __name__ == "__main__":
	output()

