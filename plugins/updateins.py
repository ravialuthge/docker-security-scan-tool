###Profile images#
###CIS_Version 1.0.0:1.12.0#

import os
from termcolor import colored
from tabulate import tabulate
from other_modules.print import *

class updateins(Print):
    """Do not use update instructions alone in the Dockerfile"""
    

    def updateins_scan(test):
        
            update_instruction_out = Print.conatiner_updateins_print()
            return update_instruction_out