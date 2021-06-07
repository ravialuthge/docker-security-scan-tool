import os
import subprocess
import re
from termcolor import colored
from plugins.containeruser import containeruser
from plugins.updateins import updateins
from plugins.common import outputpl

class cis_version_image_120:
	def version_scan(version):
		plugin_images_120 = outputpl(plugins=[containeruser(),updateins()])
		plugin_images_120.run()
