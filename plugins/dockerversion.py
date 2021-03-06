###Profile host#
###CIS_Version 1.0.0:1.6#

from other_modules.print import Print
from other_modules.docker_release import RELEASEVERSION

class dockerversion(Print):
    """Keep Docker up to date"""
    
    def dockerversion_scan(test):
        _latest_version = RELEASEVERSION
        docker_version_out = Print.container_dockerversion_print(_latest_version)
        return docker_version_out