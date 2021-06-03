import os
import subprocess
import re
from termcolor import colored

class dockerdatadirscan:
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


class dockeruserscan:
    def scan(test):
        trusted_users_cmd = "cat /etc/group | grep docker"
        health_ch_output_output = os.popen(trusted_users_cmd).read()
        trusted_users_cmd_str = re.split(':',health_ch_output_output)
        trusted_users_output_a = trusted_users_cmd_str[3]
        trusted_users_output = "user=" + trusted_users_output_a

        if trusted_users_output == "user=":
            print (colored('PASS   ', 'green') + "allowed trusted users to control Docker daemon")
        else:
            print (colored('WARN   ', 'red') + "Only allow trusted users to control Docker daemon")
