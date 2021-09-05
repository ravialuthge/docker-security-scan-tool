from plugins import *

class cis_version_containers():
	def cis_version_12(test):
		testcases = apparmor.ApparmorPlugin().apparmor_scan()
		print (testcases)
	def cis_version_112(test):
		testcases = healthcheck.healthcheck().healthcheck_scan()
		print (testcases)
	def cis_version_111(test):
		testcases = seccomp.seccomp().seccomp_scan()
		print (testcases)