from plugins.healthcheck import *
from plugins.apparmor import *
from plugins.seccomp import *
from plugins.common import *
#from plugins import *

class cis_version_containers_120:
	def version_scan(version):
		plugin_containers_120 = outputpl(plugins=[healthcheck(),apparmor()])
		plugin_containers_120.run()

class cis_version_containers_16:
	def version_scan(version):
		plugin_containers_16 = outputpl(plugins=[apparmor()])
		plugin_containers_16.run()

class cis_version_containers_111:
	def version_scan(version):
		plugin_containers_111 = outputpl(plugins=[seccomp()])
		plugin_containers_111.run()

class cis_version_containers_112:
	def version_scan(version):
		plugin_containers_112 = outputpl(plugins=[healthcheck()])
		plugin_containers_112.run()



	
