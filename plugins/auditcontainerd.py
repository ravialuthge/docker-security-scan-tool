###Profile host#
###CIS_Version 1.0.0:1.12.0#

#import os
from termcolor import colored
#import tmp.audit_filepath
#from other_modules.auditctl import *

class AuditContainerd(object):
	"""Audit Docker files and directories - /usr/bin/docker-containerd"""
	def __init__(test):
		
		audit = []

	def auditcontainerd_scan(test):
		super().__init__()
		auditcontainerd_cmd = "/usr/bin/docker-containerd"
		au = "/etc/audit/audit.rules"
		_au = au
		_auditcontainerd_cmd = auditcontainerd_cmd
		_fi = open(_au, "r")
		_mystring  = _fi.read()
		for it in _mystring.split("\n"):
  			if _auditcontainerd_cmd in it:
     				_auditcontainerd_output = it
		
		#auditcontainerd_output = os.popen(test.auditcontainerd_cmd).read()
		auditcontainerd_output = str(_auditcontainerd_output)
		if auditcontainerd_output == '':
			auditcontainerd_re = colored('WARN   ', 'red') + "Add a rule for /usr/bin/docker-containerd file"
		else:
			auditcontainerd_re = colored('PASS  ', 'green') + "Audit Docker files and directories"
		return auditcontainerd_re