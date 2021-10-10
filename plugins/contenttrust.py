###Profile images#
###CIS_Version 1.0.0:1.12.0#

from termcolor import colored
from other_modules.print import *

class contenttrust(Print):
	"""Enable Content trust for Docker"""

	def contenttrust_scan(test):
		contenttrust_value = "1"
		contenttrust_env = 'DOCKER_CONTENT_TRUST'
		contenttrust_out = Print.container_contenttrust_print(contenttrust_value,contenttrust_env)
		return contenttrust_out