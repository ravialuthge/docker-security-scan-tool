#Profile host
#CIS_Version 1.0.0:1.6

import re
from termcolor import colored
import platform

class kernelversion(object):
	"""Use the updated Linux Kernel"""
	def __init__(self) -> None:
		super().__init__()
	def kernelversion_scan(test):
		recommand_version_cmd = "3.10.0"
		install_kernel_version_cmd = platform.release()
		install_kernel_version_str = re.split('-',install_kernel_version_cmd)
		install_kernel_version = install_kernel_version_str[0]

		if install_kernel_version >= recommand_version_cmd:
			kernel_version_re = colored('PASS   ', 'green') + "kernal is up to date"
		else:
			kernel_version_re = colored('WARN   ', 'red') + "kernal not update"
		return kernel_version_re