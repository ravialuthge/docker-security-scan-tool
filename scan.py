import os
import subprocess
import re
from termcolor import colored
from tabulate import tabulate
import sys
import getopt
import profiles.docker_containers
import profiles.docker_host
import profiles.docker_images
import runpy
from plugins.datadir import dockerdatadirscan
from plugins.dockeruser import dockeruserscan
from plugins.common import outputpl
from profiles.process import cis_version
from profiles.docker_host import *
from profiles.docker_images import *
from profiles.docker_containers import *

def output():
	
	full_cmd_arguments = sys.argv

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

	sc_im_plugin_120 = cis_version(version_plugins=[cis_version_image_120()])
	sc_im_plugin_16 = cis_version(version_plugins=[cis_version_image_16()])
	sc_im_plugin_111 = cis_version(version_plugins=[cis_version_image_111()]) 
	sc_im_plugin_112 = cis_version(version_plugins=[cis_version_image_112()])
	
	sc_co_plugin_120 = cis_version(version_plugins=[cis_version_containers_120()])
	sc_co_plugin_16 = cis_version(version_plugins=[cis_version_containers_16()])
	sc_co_plugin_111 = cis_version(version_plugins=[cis_version_containers_111()])
	sc_co_plugin_112 = cis_version(version_plugins=[cis_version_containers_112()])



	arguments = len(sys.argv) -1
	if arguments == 0 or (sys.argv[1] == '-v' or sys.argv[1] == '--version') and sys.argv[2] == '1.2.0':
		sub_version="1.2.0"
		main_version="v1.2.0 - 07-29-2019"
		print (banner .format(sub_version, main_version))
		print (sc_ho)
		sc_ho_plugin_120.version_run()
		print (sc_im)
		sc_im_plugin_120.version_run()
		print (sc_co)
		sc_co_plugin_120.version_run()
		
	elif (sys.argv[1] == '-v' or sys.argv[1] == '--version') and sys.argv[2] == '1.1.0':
		sub_version="1.1.0"
		main_version="v1.1.0 - 07-06-2017"
		print (banner .format(sub_version, main_version))
		print (sc_ho)
		
		print (sc_im)
		
		print (sc_co)
	
	elif (sys.argv[1] == '-v' or sys.argv[1] == '--version') and (sys.argv[2] == '1.0.0'):
		sub_version="1.6"
		main_version="v1.0.0 - 04-22-2015"
		print (banner .format(sub_version, main_version))
		print (sc_ho)
		sc_ho_plugin_16.version_run()
		print (sc_im)
		sc_im_plugin_16.version_run()
		print (sc_co)
		sc_co_plugin_16.version_run()
		

		sub_version_a="1.11.0"
		print (banner .format(sub_version_a, main_version))
		print (sc_ho)
		sc_ho_plugin_111.version_run()
		print (sc_im)
		sc_im_plugin_111.version_run()
		print (sc_co)
		sc_co_plugin_111.version_run()
		

		sub_version_b="1.12.0"
		print (banner .format(sub_version_b, main_version))
		print (sc_ho)

		print (sc_im)
		sc_im_plugin_112.version_run()
		print (sc_co)
		sc_co_plugin_112.version_run()
	

		sub_version_c="1.13.0"
		print (banner .format(sub_version_c, main_version))
		print (sc_ho)
		
		print (sc_im)
	
		print (sc_co)
	
	elif ((sys.argv[1] == '-sv' or sys.argv[1] == '--sub-version') and sys.argv[2] == '1.0.0') and sys.argv[3] == '1.6':
		sub_version="1.6"
		main_version="v1.0.0 - 04-22-2015"
		print (banner .format(sub_version, main_version))
		print (sc_ho)
		sc_ho_plugin_16.version_run()
		print (sc_im)
		sc_im_plugin_16.version_run()
		print (sc_co)
		sc_co_plugin_16.version_run()
		

	elif ((sys.argv[1] == '-sv' or sys.argv[1] == '--sub-version') and sys.argv[2] == '1.0.0') and sys.argv[3] == '1.11.0':
		sub_version="1.11.0"
		main_version="v1.0.0 - 04-22-2015"
		print (banner .format(sub_version, main_version))
		print (sc_ho)
		sc_ho_plugin_111.version_run()
		print (sc_im)
		sc_im_plugin_111.version_run()
		print (sc_co)
		sc_co_plugin_111.version_run()

	elif ((sys.argv[1] == '-sv' or sys.argv[1] == '--sub-version') and sys.argv[2] == '1.0.0') and sys.argv[3] == '1.12.0':
		sub_version="1.12.0"
		main_version="v1.0.0 - 04-22-2015"
		print (banner .format(sub_version, main_version))
		print (sc_ho)
	
		print (sc_im)
		sc_im_plugin_112.version_run()
		print (sc_co)
		sc_co_plugin_112.version_run()
	
	elif ((sys.argv[1] == '-sv' or sys.argv[1] == '--sub-version') and sys.argv[2] == '1.0.0') and sys.argv[3] == '1.13.0':
		sub_version="1.13.0"
		main_version="v1.0.0 - 04-22-2015"
		print (banner .format(sub_version, main_version))
		print (sc_ho)
	
		print (sc_im)
	
		print (sc_co)
	
	elif (sys.argv[1] == '-s' or sys.argv[1] == '--scan') and sys.argv[2] == 'host':
		sub_version="1.2.0"
		main_version="v1.2.0 - 07-29-2019"
		print (banner .format(sub_version, main_version))
		print (sc_ho)
		sc_ho_plugin_120.version_run()
	elif (sys.argv[1] == '-s' or sys.argv[1] == '--scan') and sys.argv[2] == 'images':
		sub_version="1.2.0"
		main_version="v1.2.0 - 07-29-2019"
		print (banner .format(sub_version, main_version))
		print (sc_im)
		sc_im_plugin_120.version_run()
	elif (sys.argv[1] == '-s' or sys.argv[1] == '--scan') and sys.argv[2] == 'containers':
		sub_version="1.2.0"
		main_version="v1.2.0 - 07-29-2019"
		print (banner .format(sub_version, main_version))
		print (sc_co)
		sc_co_plugin_120.version_run()
	elif (sys.argv[1] == '-h' or sys.argv[1] == '--help'):
		print ("-v , --version       optional  run for main CIS versions (currently available versions 1.2.0 , 1.1.0 , 1.0.0)\n\n\
-sv , --sub-version  optional  run for sub CIS versions  (currently available 1.0.0 sub versions 1.6, 1.11.0, 1.12.0, 1.13.0)")
	else:
		print ("error")


if __name__ == "__main__":     
	output()

try:
	os.remove("re.txt")
	os.remove("re_st.txt")
	os.remove("re_he.txt")
	os.remove("re_st_he.txt")
	os.remove("re_up.txt")
	os.remove("re_st_up.txt")
	os.remove("re_apparmor.txt")
	os.remove("re_st_apparmor.txt")
except:
	pass