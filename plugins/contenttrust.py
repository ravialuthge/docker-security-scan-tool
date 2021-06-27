import os
from termcolor import colored

class contenttrust:
	"""Enable Content trust for Docker"""
	def scan(test):
		contenttrust_cmd = "1"
		contenttrust_version_cmd = "echo $DOCKER_CONTENT_TRUST"
		contenttrust_output = os.popen(contenttrust_version_cmd).read()

		if contenttrust_output == contenttrust_cmd:
			contenttrust_re = colored('PASS   ', 'green') + "Enabled Content trust for Docker"
		else:
			contenttrust_re = colored('WARN   ', 'red') + "Enable Content trust for Docker"
		print (contenttrust_re)