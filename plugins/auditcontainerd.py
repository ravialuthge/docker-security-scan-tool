###Profile host#
###CIS_Version 1.0.0:1.12.0#

#import os
from termcolor import colored
#import tmp.audit_filepath
#from other_modules.auditctl import *

class AuditContainerd(object):
	"""Audit Docker files and directories - /usr/bin/docker-containerd"""
	def __init__(test):
		
		test.auditcontainerd_cmd = "/usr/bin/docker-containerd"
		test.au = "/etc/audit/audit.rules" 
		

	def auditcontainerd_scan(test):
		fi = open(test.au, "r")
		mystring  = fi.read()
		for item in mystring.split("\n"):
			if test.auditcontainerd_cmd in item:
				auditcontainerd_output = item
		
		#auditcontainerd_output = os.popen(test.auditcontainerd_cmd).read()
		 
		if auditcontainerd_output == '':
			auditcontainerd_re = colored('WARN   ', 'red') + "Add a rule for /usr/bin/docker-containerd file"
		else:
			auditcontainerd_re = colored('PASS  ', 'green') + "Audit Docker files and directories"
		return auditcontainerd_re