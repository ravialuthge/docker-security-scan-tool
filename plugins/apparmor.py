###Profile containers#
###CIS_Version 1.0.0:1.6#

from termcolor import colored
from tabulate import tabulate
from sdk.containers import *

class ApparmorPlugin(ContainerList):
    """Verify AppArmor Profile, if applicable"""
    def apparmor_scan():
        
        ContainerList.container_appar_print()

sdk = ApparmorPlugin.apparmor_scan()
print(sdk)
        

