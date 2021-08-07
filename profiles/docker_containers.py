from plugins import *

class cis_version_containers(apparmor.ApparmorPlugin):
	def cis_version_12(test):
		testcases = ApparmorPlugin().apparmor_scan()
		print (testcases)

