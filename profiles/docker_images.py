from plugins import *

class cis_version_image_120:
	def version_scan(version):
		plugin_images_120 = common.outputpl(plugins=[containeruser.containeruser(),updateins.updateins()])
		plugin_images_120.run()

class cis_version_image_16:
	def version_scan(version):
		plugin_images_16 = common.outputpl(plugins=[containeruser.containeruser()])
		plugin_images_16.run()

class cis_version_image_111:
	def version_scan(version):
		plugin_images_111 = common.outputpl(plugins=[contenttrust.contenttrust()])
		plugin_images_111.run()

class cis_version_image_112:
	def version_scan(version):
		plugin_images_112 = common.outputpl(plugins=[updateins.updateins()])
		plugin_images_112.run()
