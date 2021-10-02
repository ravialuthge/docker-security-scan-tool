###Profile host#
###CIS_Version 1.0.0:1.11.0#

import os
from termcolor import colored
from sdk.docker_info import *

class Cgroup(dockerinfo):
    """Confirm default cgroup usage"""
    def __init__(test):
        test.cgroup_cmd=[] 
        
    def cgroup_scan(test):
        super().__init__()
        word = " 'CgroupDriver':"
        vv = test.lst_dir
        for h in vv:
            if word in h:
              _h = h.split(":")
              _cgroup_output  = _h[1]
              bbc = _cgroup_output.replace(" '",'')
              cgroup_output = bbc.replace("'",'')
        #cgroup_output = os.popen(test.cgroup_cmd).read()
        #cgroup_output_a = cgroup_output.rstrip()
        #cgroup_output = "cgroup=" + cgroup_output_a

        if cgroup_output == "cgroup-parent":
            cgroup_output =  colored('PASS   ', 'green') + "default cgroup used"
        else:
           cgroup_output = colored('WARN   ', 'red') + "confirm default cgroup usage"
        return cgroup_output