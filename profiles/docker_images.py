import os
import subprocess
import re
from termcolor import colored
from plugins.containeruser import *
from plugins.updateins import *
from plugins.contenttrust import *
from plugins.common import outputpl

class cis_version_image_120:
	def version_scan(version):
		plugin_images_120 = outputpl(plugins=[containeruser(),updateins()])
		plugin_images_120.run()

class cis_version_image_16:
	def version_scan(version):
		plugin_images_16 = outputpl(plugins=[containeruser()])
		plugin_images_16.run()

class cis_version_image_111:
	def version_scan(version):
		plugin_images_111 = outputpl(plugins=[contenttrust()])
		plugin_images_111.run()

class cis_version_image_112:
	def version_scan(version):
		plugin_images_112 = outputpl(plugins=[updateins()])
		plugin_images_112.run()
