import os
import subprocess
import re
from termcolor import colored

def docker_version():
	latest_version_cmd = "yum list docker-ce | sort -r | awk '{print $2}' | sed -n 6p"
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
	return docker_version_re

def docker_root():
	root_dir_ch_cmd = "df -h | grep $(docker info -f '{{ .DockerRootDir }}') | awk '{print $6}'"
	root_dir_output = subprocess.check_output(["docker", "info" , "--format" , "'{{.DockerRootDir}}'"])
	root_dir_x = root_dir_output.decode("utf-8")
	root_dir = root_dir_x.replace("'",'')
	root_dir_ch_output = os.popen(root_dir_ch_cmd).read()
	root_dir_ch = root_dir_ch_output.rstrip()

	if root_dir == root_dir_ch:
		docker_root_re = colored('PASS   ', 'green') + "crated separate partition for docker root directory"
	else:
		docker_root_re = colored('WARN   ', 'red') + "not crated separate partition for docker root directory"
	return docker_root_re

def kernel_version():
	recommand_version_cmd = "3.10.0"
	install_kernel_version_cmd = "uname -r"
	root_dir_ch_output_output = os.popen(install_kernel_version_cmd).read()
	install_kernel_version_str = re.split('-',root_dir_ch_output_output)
	install_kernel_version = install_kernel_version_str[0]

	if install_kernel_version >= recommand_version_cmd:
		kernel_version_re = colored('PASS   ', 'green') + "kernal is up to date"
	else:
		kernel_version_re = colored('WARN   ', 'red') + "kernal not update"
	return kernel_version_re	

def trusted_users():
	
	trusted_users_cmd = "cat /etc/group | grep docker"
	health_ch_output_output = os.popen(trusted_users_cmd).read()
	trusted_users_cmd_str = re.split(':',health_ch_output_output)
	trusted_users = trusted_users_cmd_str[3]

	if trusted_users == ' ':
		trusted_users_re = colored('PASS   ', 'green') + "allowed trusted users to control Docker daemon"
	else:
		trusted_users_re = colored('WARN   ', 'red') + "Only allow trusted users to control Docker daemon" + trusted_users
	return trusted_users_re

