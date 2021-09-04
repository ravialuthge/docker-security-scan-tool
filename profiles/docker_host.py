from plugins import *  

class cis_version_host(object):
	def cis_version_112(test):
		testcases = auditcontainerd.AuditContainerd().auditcontainerd_scan()
		print (testcases)
	def cis_version_111(test):
		testcases = cgroup.Cgroup().cgroup_scan()
		print (testcases)
	def cis_version_16(test):
		testcases = datadir.dockerdatadir().dockerdatadir_scan()
		testcases = dockeruser.dockeruser().dockeruserscan_scan()
		testcases = dockerversion.dockerversion().dockerversion_scan()
		print (testcases)


