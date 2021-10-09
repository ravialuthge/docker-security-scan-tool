###Profile containers#
###CIS_Version 1.0.0:1.6#

#from termcolor import colored
#from tabulate import tabulate
from sdk.containers import *

class ApparmorPlugin():
    """Verify AppArmor Profile, if applicable"""
    #def __init__(test) -> None:
    #    super().__init__()
    @staticmethod
    def apparmor_scan():
        
        abc = ContainerList().container_appar()
        return abc

#sdk = ApparmorPlugin().apparmor_scan()
#print (sdk)
        

