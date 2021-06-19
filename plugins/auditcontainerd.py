import os
import re
from termcolor import colored

class auditcontainerd:
	def scan(test):
		auditcontainerd_cmd = "auditctl -l | grep /usr/bin/docker-containerd"
		auditcontainerd_output = os.popen(auditcontainerd_cmd).read()

		if auditcontainerd_output == '':
			auditcontainerd_re = colored('WARN   ', 'red') + "Add a rule for /usr/bin/docker-containerd file"
		else:
			auditcontainerd_re = colored('PASS  ', 'green') + "Audit Docker files and directories"
		print (auditcontainerd_re)