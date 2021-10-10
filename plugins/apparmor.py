###Profile containers#
###CIS_Version 1.0.0:1.6#

from other_modules.print import *

class ApparmorPlugin(Print):
    """Verify AppArmor Profile, if applicable"""
    
    def apparmor_scan(test):
        
        abc = Print.container_appar_print()
        return abc

        

