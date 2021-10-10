###Profile host#
###CIS_Version 1.0.0:1.13.0#


from termcolor import colored
from tabulate import tabulate
from other_modules.print import *

class encryptnet(Print):
    """Encrypt data exchanged between containers on different nodes on the overlay network"""
            
    def encryptnet_scan(test):
            table_encryptnet_output = Print.container_encryptnet_print()
            return table_encryptnet_output