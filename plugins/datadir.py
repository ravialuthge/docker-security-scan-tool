###Profile host#
###CIS_Version 1.0.0:1.6#

from other_modules.print import *

class dockerdatadir(Print):
    """Create a separate partition for containers"""

    def dockerdatadir_scan(test):
        
        datadir_out = Print.container_datadir_print()
        return datadir_out

