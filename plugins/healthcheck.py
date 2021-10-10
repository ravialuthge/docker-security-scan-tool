###Profile containers#
###CIS_Version 1.0.0:1.12.0#

from termcolor import colored
from tabulate import tabulate
from other_modules.print import Print
from sdk.containers_id_list import *

class healthcheck(Print):
    """Check container health at runtime"""
    
    def healthcheck_scan(test):
        
        _table_he_output = Print.container_healthcheck_print()
        return _table_he_output