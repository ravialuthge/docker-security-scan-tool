###Profile host#
###CIS_Version 1.0.0:1.12.0()

import os
from termcolor import colored

class AuditContainerd(object):
	"""Audit Docker files and directories - /usr/bin/docker-containerd"""
	def __init__(test):
		test.auditcontainerd_cmd = "auditctl -l | grep /usr/bin/docker-containerd"

	def auditcontainerd_scan(test):
		
		auditcontainerd_output = os.popen(test.auditcontainerd_cmd).read()
		
		if auditcontainerd_output == '':
			auditcontainerd_re = colored('WARN   ', 'red') + "Add a rule for /usr/bin/docker-containerd file"
		else:
			auditcontainerd_re = colored('PASS  ', 'green') + "Audit Docker files and directories"
		return auditcontainerd_re