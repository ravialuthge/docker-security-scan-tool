from plugins import *

class cis_version_images():
	def cis_version_16(test):
		testcases = imageuser.ImageUser().imageuser_scan()
		print (testcases)
	def cis_version_111(test):
		testcases = contenttrust.contenttrust().contenttrust_scan()
		print (testcases)
	def cis_version_112(test):
		testcases = updateins.updateins().updateins_scan()
		print (testcases)