###Profile images#
###CIS_Version 1.0.0:1.12.0()

import os
from termcolor import colored

class contenttrust(object):
	"""Enable Content trust for Docker"""
	def __init__(test):
		test.contenttrust_cmd = "1"
		test.contenttrust_version_cmd = "echo $DOCKER_CONTENT_TRUST"
	def contenttrust_scan(test):
		
		contenttrust_output = os.popen(test.contenttrust_version_cmd).read()

		if contenttrust_output == test.contenttrust_cmd:
			contenttrust_re = colored('PASS   ', 'green') + "Enabled Content trust for Docker"
		else:
			contenttrust_re = colored('WARN   ', 'red') + "Enable Content trust for Docker"
		return contenttrust_re