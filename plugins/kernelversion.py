###Profile host#
###CIS_Version 1.0.0:1.6#

import re
from termcolor import colored
import platform
from other_modules.print import *

class kernelversion(Print):
	"""Use the updated Linux Kernel"""
	
	def kernelversion_scan(test):
		kernel_version_output = Print.host_kernelversion_print()
		return kernel_version_output