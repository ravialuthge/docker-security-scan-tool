import os
import subprocess
import re
from termcolor import colored
from plugins.dockerversion import *
from plugins.datadir import *
from plugins.kernelversion import *
from plugins.dockeruser import *
from plugins.cgroup import *
from plugins.auditcontainerd import *
from plugins.userland import *
from plugins.common import outputpl

class cis_version_120:
	def version_scan(version):
		plugin_host_120 = outputpl(plugins=[dockerversion(),dockerdatadirscan(),kernelversion(),dockeruserscan()])
		plugin_host_120.run()

class cis_version_16:
	def version_scan(version):
		plugin_host_16 = outputpl(plugins=[dockerversion(),dockerdatadirscan(),kernelversion(),dockeruserscan()])
		plugin_host_16.run()

class cis_version_111:
	def version_scan(version):
		plugin_host_111 = outputpl(plugins=[cgroup()])
		plugin_host_111.run()

class cis_version_112:
	def version_scan(version):
		plugin_host_112 = outputpl(plugins=[auditcontainerd()])
		plugin_host_112.run()

class cis_version_113:
	def version_scan(version):
		plugin_host_113 = outputpl(plugins=[userland()])
		plugin_host_113.run()



