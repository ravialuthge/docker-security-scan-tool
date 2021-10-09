###Profile containers#
###CIS_Version 1.0.0:1.6#

#from termcolor import colored
#from tabulate import tabulate
from other_modules import *
from other_modules.print import Print

class ApparmorPlugin(Print):
    """Verify AppArmor Profile, if applicable"""
    def apparmor_scan():
        
        print.Print().container_appar_print()
        

