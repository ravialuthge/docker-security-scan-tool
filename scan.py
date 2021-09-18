import sys
import os
from termcolor import colored
import argparse
import pkgutil
import plugins
import textwrap
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

files = os.listdir('plugins/')
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

ou = lst_plugins_a + "   " + _moduleshelplist


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
		
		elif args.plugins == "apparmor":
			#print (apparmor.ApparmorPlugin().apparmor_scan())
			all_my_base_classes = {cls.__name__: cls for cls in apparmor.__subclasses__()}
			print (all_my_base_classes)

		elif args.files == "officialimage":
			print (sc_dockerfile)
			officialimage.officialimage().officialimagescan()
			
		else:
			parser.print_help()
			
if __name__ == "__main__":
	output()

