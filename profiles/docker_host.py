import os
import subprocess
import re
from termcolor import colored
from plugins.dockerversion import *
from plugins.datadir import *
from plugins.kernelversion import *
from plugins.dockeruser import *
from plugins.common import outputpl

class cis_version_120:
	def version_scan(version):
		plugin_host_120 = outputpl(plugins=[dockerversion(),dockerdatadirscan(),kernelversion(),dockeruserscan()])
		plugin_host_120.run()


