import os
import subprocess
import re
from termcolor import colored
from plugins.dockerversion import dockerversion
from plugins.datadir import dockerdatadirscan
from plugins.kernelversion import kernelversion
from plugins.dockeruser import dockeruserscan
from plugins.common import outputpl

class cis_version_120:
	def version_scan(version):
		plugin_host_120 = outputpl(plugins=[dockerversion()])
		plugin_host_120.run()


