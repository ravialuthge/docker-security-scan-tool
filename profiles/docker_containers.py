from plugins import *
import sdk.containers as containers

class cis_version_containers_120:
	def version_scan(version):
		plugin_containers_120 = common.outputpl(plugins=[healthcheck.healthcheck(),apparmor.apparmor(containers.containerlist)])
		plugin_containers_120.run()

class cis_version_containers_16:
	def version_scan(version):
		plugin_containers_16 = common.outputpl(plugins=[apparmor.apparmor(containers.containerlist)])
		plugin_containers_16.run()

class cis_version_containers_111:
	def version_scan(version):
		plugin_containers_111 = common.outputpl(plugins=[seccomp.seccomp()])
		plugin_containers_111.run()

class cis_version_containers_112:
	def version_scan(version):
		plugin_containers_112 = common.outputpl(plugins=[healthcheck.healthcheck()])
		plugin_containers_112.run()



	
