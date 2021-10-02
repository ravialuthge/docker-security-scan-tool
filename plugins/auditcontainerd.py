###Profile host#
###CIS_Version 1.0.0:1.12.0#

import os
from termcolor import colored
import tmp.audit_filepath
from other_modules.auditctl import *

class AuditContainerd(Audit):
	"""Audit Docker files and directories - /usr/bin/docker-containerd"""
	def __init__(test):
		test.auditcontainerd_cmd = "/usr/bin/docker-containerd"
		

	def auditcontainerd_scan(test):
		tmp.audit_filepath.AUDITFILEPATH = test.auditcontainerd_cmd
		
		#auditcontainerd_output = os.popen(test.auditcontainerd_cmd).read()
		auditcontainerd_output = test._item 
		if auditcontainerd_output == '':
			auditcontainerd_re = colored('WARN   ', 'red') + "Add a rule for /usr/bin/docker-containerd file"
		else:
			auditcontainerd_re = colored('PASS  ', 'green') + "Audit Docker files and directories"
		return auditcontainerd_re