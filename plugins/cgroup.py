import os
import subprocess
import re
from termcolor import colored

class cgroup:
    def scan(test):
        cgroup_cmd = "ps -ef | grep docker | grep 'cgroup-parent'"
        cgroup_output = os.popen(cgroup_cmd).read()
        cgroup_output_a = cgroup_output.rstrip()
        cgroup_output = "cgroup=" + cgroup_output_a

        if cgroup_output == "cgroup=":
            print (colored('PASS   ', 'green') + "default cgroup used")
        else:
            print (colored('WARN   ', 'red') + "confirm default cgroup usage")