import os
from termcolor import colored

class Cgroup(object):
    """Confirm default cgroup usage"""
    def __init__(test):
        test.cgroup_cmd = "ps -ef | grep docker | grep 'cgroup-parent'"
        
    def cgroup_scan(test):
        
        cgroup_output = os.popen(test.cgroup_cmd).read()
        cgroup_output_a = cgroup_output.rstrip()
        cgroup_output = "cgroup=" + cgroup_output_a

        if cgroup_output == "cgroup=":
            cgroup_output =  colored('PASS   ', 'green') + "default cgroup used"
        else:
           cgroup_output = colored('WARN   ', 'red') + "confirm default cgroup usage"
        return cgroup_output