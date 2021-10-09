###Profile host#
###CIS_Version 1.0.0:1.6#

import grp
from termcolor import colored
from other_modules.print import *

class dockeruser(Print):
    """Only allow trusted users to control Docker daemon"""
    
    def dockeruserscan_scan(test):
        dockeruserscan_out = Print.container_defaultbridge_print()
        return dockeruserscan_out