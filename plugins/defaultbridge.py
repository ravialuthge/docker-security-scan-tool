###Profile host#
###CIS_Version 1.1.0:1.1.0#


from termcolor import colored
from tabulate import tabulate
from sdk.docker_bridge_net_name import *
from other_modules.print import *

class defaultbridge(Print):
    """Ensure network traffic is restricted between containers on the default bridge"""
            
    def defaultbridge_scan(test):
            _table_defaultbridge_out = Print.container_defaultbridge_print()
            return _table_defaultbridge_out