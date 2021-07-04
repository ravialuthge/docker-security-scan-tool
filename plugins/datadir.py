import os
import subprocess
from termcolor import colored

class dockerdatadirscan:
    """Create a separate partition for containers"""
    def scan(test):
        root_dir_ch_cmd = "df -h | grep $(docker info -f '{{ .DockerRootDir }}') | awk '{print $6}'"
        root_dir_output = subprocess.check_output(["docker", "info" , "--format" , "'{{.DockerRootDir}}'"])
        root_dir_x = root_dir_output.decode("utf-8")
        root_dir = root_dir_x.replace("'",'')
        root_dir_ch_output = os.popen(root_dir_ch_cmd).read()
        root_dir_ch = root_dir_ch_output.rstrip()

        if root_dir == root_dir_ch:
            print (colored('PASS   ', 'green') + "crated separate partition for docker root directory")
        else:
            print (colored('WARN   ', 'red') + "not crated separate partition for docker root directory")

