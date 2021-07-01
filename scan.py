import os
import sys
from termcolor import colored
from profiles.process import *
#from profiles.docker_host import *
from profiles.docker_images import *
from profiles.docker_containers import *
import argparse
from profiles import *

def loadImports(path):
    files = os.listdir(path)
    imps = []

    for i in range(len(files)):
        name = files[i].split('.')
        if len(name) > 1:
            if name[1] == 'py' and name[0] != '__init__':
               name = name[0]
               imps.append(name)

    file = open(path+'__init__.py','w')

    toWrite = '__all__ = '+str(imps)

    file.write(toWrite)
    file.close()

from profiles import *

def output():
	
	banner = (colored("# --------------------------------------------------------------------------------------------\n\
# CIS Docker {0} Benchmark\n\
# # {1}\n\
# --------------------------------------------------------------------------------------------\n\
	", 'green', attrs=['bold']))


	sc_ho	= (colored('Docker Host',attrs=['bold']))
	sc_im	= (colored('Docker Images',attrs=['bold']))
	sc_co   = (colored('Docker Containers',attrs=['bold']))
	
	sc_ho_plugin_120 = cis_version(version_plugins=[cis_version_120()])
	sc_ho_plugin_16 = cis_version(version_plugins=[cis_version_16()])
	sc_ho_plugin_111 = cis_version(version_plugins=[cis_version_111()])
	sc_ho_plugin_112 = cis_version(version_plugins=[cis_version_112()])
	sc_ho_plugin_113 = cis_version(version_plugins=[cis_version_113()])

	sc_im_plugin_120 = cis_version(version_plugins=[cis_version_image_120()])
	sc_im_plugin_16 = cis_version(version_plugins=[cis_version_image_16()])
	sc_im_plugin_111 = cis_version(version_plugins=[cis_version_image_111()]) 
	sc_im_plugin_112 = cis_version(version_plugins=[cis_version_image_112()])
	
	sc_co_plugin_120 = cis_version(version_plugins=[cis_version_containers_120()])
	sc_co_plugin_16 = cis_version(version_plugins=[cis_version_containers_16()])
	sc_co_plugin_111 = cis_version(version_plugins=[cis_version_containers_111()])
	sc_co_plugin_112 = cis_version(version_plugins=[cis_version_containers_112()])

	arguments_a = len(sys.argv) -1
	if arguments_a == 0:
		sub_version="1.2.0"
		main_version="v1.2.0 - 07-29-2019"
		print (banner .format(sub_version, main_version))
		print (sc_ho)
		sc_ho_plugin_120.version_run()
		print (sc_im)
		sc_im_plugin_120.version_run()
		print (sc_co)
		sc_co_plugin_120.version_run()
	else:
		parser = argparse.ArgumentParser()
		parser.add_argument("-v", "--version", type=str , help="run for main CIS versions (currently available versions 1.2.0 , 1.1.0 , 1.0.0)")
		parser.add_argument("-sv", "--sub-version", type=str , help="run for sub CIS versions  (currently available 1.0.0 sub versions 1.6, 1.11.0, 1.12.0, 1.13.0)")
		parser.add_argument("-p", "--profile", type=str, help="run for configuration profiles  (currently available docker host , docker images & docker containers)")
		args = parser.parse_args()

		if args.version == "1.2.0":
			sub_version="1.2.0"
			main_version="v1.2.0 - 07-29-2019"
			print (banner .format(sub_version, main_version))
			print (sc_ho)
			sc_ho_plugin_120.version_run()
			print (sc_im)
			sc_im_plugin_120.version_run()
			print (sc_co)
			sc_co_plugin_120.version_run()

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
			sc_ho_plugin_16.version_run()
			print (sc_im)
			sc_im_plugin_16.version_run()
			print (sc_co)
			sc_co_plugin_16.version_run()

			sub_version="1.11.0"
			main_version="v1.0.0 - 04-22-2015"
			print (banner .format(sub_version, main_version))
			print (sc_ho)
			sc_ho_plugin_111.version_run()
			print (sc_im)
			sc_im_plugin_111.version_run()
			print (sc_co)
			sc_co_plugin_111.version_run()

			sub_version="1.12.0"
			main_version="v1.0.0 - 04-22-2015"
			print (banner .format(sub_version, main_version))
			print (sc_ho)
			sc_ho_plugin_112.version_run()
			print (sc_im)
			sc_im_plugin_112.version_run()
			print (sc_co)
			sc_co_plugin_112.version_run()

			sub_version="1.13.0"
			main_version="v1.0.0 - 04-22-2015"
			print (banner .format(sub_version, main_version))
			print (sc_ho)
			sc_ho_plugin_113.version_run()
			print (sc_im)
		
			print (sc_co)
		else:
			parser = argparse.ArgumentParser()
			parser.parse_args()
	

if __name__ == "__main__":
	loadImports('profiles/')     
	output()

pwd_output = os.getcwd()
pwd_list = os.listdir(pwd_output)
for list in pwd_list:
    if list.endswith(".txt"):
        os.remove(os.path.join(pwd_output, list))

