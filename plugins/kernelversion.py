import os
import re
from termcolor import colored

class kernelversion:
	"""Use the updated Linux Kernel"""
	def scan(test):
		recommand_version_cmd = "3.10.0"
		install_kernel_version_cmd = "uname -r"
		root_dir_ch_output_output = os.popen(install_kernel_version_cmd).read()
		install_kernel_version_str = re.split('-',root_dir_ch_output_output)
		install_kernel_version = install_kernel_version_str[0]

		if install_kernel_version >= recommand_version_cmd:
			kernel_version_re = colored('PASS   ', 'green') + "kernal is up to date"
		else:
			kernel_version_re = colored('WARN   ', 'red') + "kernal not update"
		print (kernel_version_re)