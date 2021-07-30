from plugins import *

class cis_version_120:
	def version_scan(version):
		plugin_host_120 = common.outputpl(plugins=[dockerversion.dockerversion(),datadir.dockerdatadirscan(),kernelversion.kernelversion(),dockeruser.dockeruserscan()])
		plugin_host_120.run()

class cis_version_16:
	def version_scan(version):
		plugin_host_16 = common.outputpl(plugins=[dockerversion.dockerversion(),datadir.dockerdatadirscan(),kernelversion.kernelversion(),dockeruser.dockeruserscan()])
		plugin_host_16.run()

class cis_version_111:
	def version_scan(version):
		plugin_host_111 = common.outputpl(plugins=[cgroup.cgroup()])
		plugin_host_111.run()

class cis_version_112:
	def version_scan(version):
		plugin_host_112 = common.outputpl(plugins=[auditcontainerd.auditcontainerd()])
		plugin_host_112.run()

class cis_version_113:
	def version_scan(version):
		plugin_host_113 = common.outputpl(plugins=[encryptnet.encryptnet()])
		plugin_host_113.run()



