###Profile host#
###CIS_Version 1.0.0:1.6#

import os
import subprocess
import re
from termcolor import colored
import platform
from sdk.docker_info import *

class dockerversion(dockerinfo):
    """Keep Docker up to date"""
    def __init__(test):
        test.a_h=[]
    def dockerversion_scan(test):
        super().__init__()
        
        vv = test.lst_ver
        word = " 'Version':"
        for h in vv:
          if word in h:
            test.a_h.append(h)
        __h = test.a_h[0]
        _h = __h.split(":")
        _install_version  = _h[1]
        bbc =  _install_version.replace(" '",'')
        install_version = bbc.replace("'",'')
    
        centos_version_cmd = platform.linux_distribution()[1]
        centos_version_str_x = centos_version_cmd.split(".")
        centos_version = centos_version_str_x[0]
        if centos_version == '7':
            latest_version_cmd = "yum list docker-ce | sort -r | awk '{print $2}' | sed -n 6p"
            latest_version_output = os.popen(latest_version_cmd).read()
            latest_version_str = latest_version_output.rstrip()
            latest_version_str_x = re.split(':|-',latest_version_str)
            latest_version = latest_version_str_x[1]
            if install_version == latest_version:
                docker_version_re = colored('PASS   ', 'green') + "Docker is up to date"
            elif install_version != latest_version:
                docker_version_re = colored('INFO   ', 'blue') + "Docker not update"
            else:
                docker_version_re = "Docker not install"
    
        elif centos_version == '8':
            latest_version_cmd = "yum list docker-ce | sort -r | awk '{print $2}' | sed -n 3p"
            latest_version_output = os.popen(latest_version_cmd).read()
            latest_version_str = latest_version_output.rstrip()
            latest_version_str_x = re.split(':|-',latest_version_str)
            latest_version = latest_version_str_x[1]
            if install_version == latest_version:
                docker_version_re = colored('PASS   ', 'green') + "Docker is up to date"
            elif install_version != latest_version:
                docker_version_re = colored('INFO   ', 'blue') + "Docker not update"
            else:
                docker_version_re = "Docker not install"
        return docker_version_re