import os
import subprocess
import re
from termcolor import colored
from tabulate import tabulate

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
		docker_version_re = "Docker is up to date"
	elif install_version != latest_version:
		docker_version_re = "Docker not update"
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
		docker_root_re = "crated separate partition for docker root directory"
	else:
		docker_root_re = "not crated separate partition for docker root directory"
	return docker_root_re

def container_user():
	images_cmd =  "docker images --format '{{ .Repository }}:{{ .Tag }}'"
	container_user_cmd = "docker image inspect -f 'User={{.Config.User}}' $(docker images --format '{{ .Repository }}:{{ .Tag }}')"
	container_user_output = os.popen(container_user_cmd).read()
	images_output = os.popen(images_cmd).read()
	images = images_output.split()
	container_users = container_user_output.split()
	f = open("re.txt", "w")
	for i in (container_users):
	if i == 'User=' or i == 'User=root':
			container_user_co = "not user for the container has been created"
	else:
			container_user_co = "user for the container has been created"
	f.write(container_user_co)
	f.write("\n")
	f= open("re.txt", "r")
	container_user_co_f = f.read()
	table = [[images_output , container_user_co_f]]
	print(tabulate(table))
	
	return table


def output():
	docker_version_re = docker_version()
	docker_root_re = docker_root()
	container_user_re = container_user()
	
	print (colored('# --------------------------------------------------------------------------------------------\n\
# CIS Docker 1.6 Benchmark\n\
# # v1.0.0 - 04-22-2015\n\
# # ------------------------------------------------------------------------------------------\n\
	', 'green'))
	print (colored('Docker Host',attrs=['bold']))
	print (colored('INFO   ', 'blue'), docker_version_re)
	print (colored('WARN   ', 'red'), docker_root_re)
	print (colored('Docker Images',attrs=['bold']))
	print (colored('WARN   ', 'red'), tabulate(table))

if __name__ == "__main__":     
	output()
os.remove("re.txt")