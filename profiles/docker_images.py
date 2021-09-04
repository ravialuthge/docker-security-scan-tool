from plugins import * 

class cis_version_images(imageuser.ImageUser):
	def cis_version_16(test):
		testcases = imageuser.ImageUser().imageuser_scan()
		print (testcases)