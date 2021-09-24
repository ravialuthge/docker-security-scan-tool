###Profile host#
###CIS_Version 1.0.0:1.6()

import os
import psutil
from termcolor import colored

class dockerdatadir(object):
    """Create a separate partition for containers"""
    def __init__(test):
        test.mountdir=[]

    def dockerdatadir_scan(test):
        super().__init__()
        root_dir_cmd = "docker info -f '{{.DockerRootDir}}'"
        _root_dir_ch_output = os.popen(root_dir_cmd).read()
        root_dir_ch_output = _root_dir_ch_output.rstrip()
        partitions = psutil.disk_partitions()
        for p in partitions:
             if (p.mountpoint) == root_dir_ch_output:
                 test.mountdir.append(p.mountpoint)
        _root_dir = str(test.mountdir)
        bbc = _root_dir.replace("[",'')
        bbcdr = bbc.replace("]",'')
        root_dir = bbcdr.replace("'",'')
        if root_dir_ch_output == root_dir:
            datadir_output =  colored('PASS   ', 'green') + "crated separate partition for docker root directory"
        else:
            datadir_output = colored('WARN   ', 'red') + "not crated separate partition for docker root directory"
        return datadir_output

