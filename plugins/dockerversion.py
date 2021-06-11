import os
import subprocess
import re
from termcolor import colored

class dockerversion:
    def scan(test):
        install_version_output = subprocess.check_output(["docker", "version" , "--format" , "'{{.Server.Version}}'"])
        install_version_x = install_version_output.decode("utf-8")
        install_version = install_version_x.replace("'",'')
        centos_version_cmd = "cat /etc/centos-release | awk '{print $4}'"
        centos_version_cmd_output = os.popen(centos_version_cmd).read()
        centos_version_cmd_output_a = centos_version_cmd_output.rstrip()
        centos_version_str_x = centos_version_cmd_output_a.split(".")
        centos_version = centos_version_str_x[0]
        if centos_version == 7:
            latest_version_cmd = "yum list docker-ce | sort -r | awk '{print $2}' | sed -n 6p"
            latest_version_output = os.popen(latest_version_cmd).read()
            latest_version_str = latest_version_output.rstrip()
            latest_version_str_x = re.split(':|-',latest_version_str)
            latest_version = latest_version_str_x[1]
        elif centos_version == 8:
            latest_version_cmd = "yum list docker-ce | sort -r | awk '{print $2}' | sed -n 4p"
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
        print (docker_version_re)