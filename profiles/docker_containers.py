from plugins import *

class cis_version_containers(apparmor.ApparmorPlugin):
	def cis_version_12(test):
		testcases = test.apparmor_output_cmd
		print (testcases)

