###Profile containers#
###CIS_Version 1.0.0:1.6#

#from termcolor import colored
#from tabulate import tabulate
from sdk.containers import *

class ApparmorPlugin(ContainerList):
    """Verify AppArmor Profile, if applicable"""
    def __init__(self) -> None:
        super().__init__()
    def apparmor_scan():
        
        abc = ContainerList().container_appar()
        return abc

#sdk = ApparmorPlugin().apparmor_scan()
#print (sdk)
        

