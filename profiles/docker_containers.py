import os
import subprocess
import re
from termcolor import colored
from plugins.healthcheck import *
from plugins.apparmor import *
from plugins.common import outputpl

class cis_version_containers_120:
	def version_scan(version):
		plugin_containers_120 = outputpl(plugins=[healthcheck(),apparmor()])
		plugin_containers_120.run()



	