###Profile host#
###CIS_Version 1.0.0:1.12.0#

from other_modules.print import *

class AuditContainerd(Print):
	"""Audit Docker files and directories - /usr/bin/docker-containerd"""

	def auditcontainerd_scan(test):
		auditcontainerd_path = "/usr/bin/docker-containerd"
		auditcontainerd_re = Print.container_audit_print(auditcontainerd_path)
		return auditcontainerd_re