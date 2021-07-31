from plugins import *


class cis_version_containers_111:
	def version_scan(version):
		plugin_containers_111 = common.outputpl(plugins=[seccomp.seccomp()])
		plugin_containers_111.run()

class cis_version_containers_112:
	def version_scan(version):
		plugin_containers_112 = common.outputpl(plugins=[healthcheck.healthcheck()])
		plugin_containers_112.run()




	
