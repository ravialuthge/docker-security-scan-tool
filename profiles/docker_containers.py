from plugins.apparmor import *

class cis_version_containers(apparmor):
	def version_120(self):
		plugin_containers_120 = apparmor()
		plugin_containers_120_output = plugin_containers_120.apparmor_scan()
		return plugin_containers_120_output

object1 = cis_version_containers()
sum = object1.version_120()
print (sum)




	
