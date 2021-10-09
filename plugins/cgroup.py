###Profile host#
###CIS_Version 1.0.0:1.11.0#

import os
from termcolor import colored
from other_modules.print import *

class Cgroup(Print):
    """Confirm default cgroup usage"""

    def cgroup_scan(test):
       cgroup_out = Print.container_cgroup_print()
       return cgroup_out
        