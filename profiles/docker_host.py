from plugins import * 

class cis_version_host():
	def cis_version_112(test):
		testcases = auditcontainerd.AuditContainerd().auditcontainerd_scan()
		print (testcases)
	def cis_version_111(test):
		testcases = cgroup.Cgroup().cgroup_scan()
		print (testcases)


