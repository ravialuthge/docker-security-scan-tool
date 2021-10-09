###Profile containers#
###CIS_Version 1.0.0:1.6#

#from termcolor import colored
#from tabulate import tabulate
from other_modules.print import *

class ApparmorPlugin(object):
    """Verify AppArmor Profile, if applicable"""
    #def __init__(test) -> None:
    #    super().__init__()
    def apparmor_scan(test):
        
        Print().container_appar_print()
        #return abc

#sdk = ApparmorPlugin().apparmor_scan()
#print (sdk)
        

