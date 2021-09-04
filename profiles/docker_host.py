from plugins import * 

class cis_version_host(auditcontainerd.AuditContainerd):
	def cis_version_112(test):
		testcases = auditcontainerd.AuditContainerd().auditcontainerd_scan()
		print (testcases)


