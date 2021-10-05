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
		testcases2 = dockeruser.dockeruser().dockeruserscan_scan()
		testcases3 = dockerversion.dockerversion().dockerversion_scan()
		testcases4 = kernelversion.kernelversion().kernelversion_scan()
		print (testcases)
		print (testcases2)
		print (testcases3)
		print (testcases4)
	def cis_version_113(test):
		testcases = encryptnet.encryptnet().encryptnet_scan()
		print (testcases)


