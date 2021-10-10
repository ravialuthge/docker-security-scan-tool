###Profile host#
###CIS_Version 1.0.0:1.6#

from other_modules.print import *

class dockeruser(Print):
    """Only allow trusted users to control Docker daemon"""
    
    def dockeruserscan_scan(test):
        dockeruserscan_out = Print.host_dockeruser_print()
        return dockeruserscan_out