###Profile containers#
###CIS_Version 1.0.0:1.11.0#

from other_modules.print import *

class seccomp(Print):
    """Do not disable default seccomp profile""" 
    
    def seccomp_scan(test):
      
        seccomp_output = Print.conatiner_seccomp_print()
        return seccomp_output