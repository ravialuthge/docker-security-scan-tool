###Profile host#
###CIS_Version 1.0.0:1.12.0#

#import os
from termcolor import colored
#import tmp.audit_filepath
from other_modules.auditctl import *

class AuditContainerd(Audit):
	"""Audit Docker files and directories - /usr/bin/docker-containerd"""
	def __init__(test):
		super().__init__()
	def auditcontainerd_scan(test):
		auditcontainerd_output = test._auditcontainerd_output
		print (auditcontainerd_output)
		if auditcontainerd_output == "[]":
	    		auditcontainerd_re = colored('WARN   ', 'red') + "Add a rule for /usr/bin/docker-containerd file"
		else:
			auditcontainerd_re = colored('PASS  ', 'green') + "Audit Docker files and directories"
		return auditcontainerd_re