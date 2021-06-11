import os
import subprocess
import re
from termcolor import colored

class dockerversion:
    def scan(test):
        centos_version_cmd = "cat /etc/centos-release | awk '{print $4}'"
        centos_version_cmd_output = os.popen(centos_version_cmd).read()
        centos_version_str_x = re.split('.',centos_version_cmd_output)
        centos_version = centos_version_str_x[1]
        if os.popen(centos_version).read() == 7:
            latest_version_cmd = "yum list docker-ce | sort -r | awk '{print $2}' | sed -n 6p"
            install_version_output = subprocess.check_output(["docker", "version" , "--format" , "'{{.Server.Version}}'"])
            install_version_x = install_version_output.decode("utf-8")
            install_version = install_version_x.replace("'",'')
            latest_version_output = os.popen(latest_version_cmd).read()
            latest_version_str = latest_version_output.rstrip()
            latest_version_str_x = re.split(':|-',latest_version_str)
            latest_version = latest_version_str_x[1]
        elif os.popen(centos_version).read() == 8:
            latest_version_cmd = "yum list docker-ce | sort -r | awk '{print $2}' | sed -n 4p"
            install_version_output = subprocess.check_output(["docker", "version" , "--format" , "'{{.Server.Version}}'"])
            install_version_x = install_version_output.decode("utf-8")
            install_version = install_version_x.replace("'",'')
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