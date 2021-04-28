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
	for c in range(len(images)):
		container_user_re_a = images[c] + " " + container_users[c]
	return container_user_re_a

def container_user_b():
	images_cmd =  "docker images --format '{{ .Repository }}:{{ .Tag }}'"
	container_user_cmd = "docker image inspect -f 'User={{.Config.User}}' $(docker images --format '{{ .Repository }}:{{ .Tag }}')"
	container_user_output = os.popen(container_user_cmd).read()
	images_output = os.popen(images_cmd).read()
	images = images_output.split()
	container_users = container_user_output.split()
	for i in (container_users):
		if i == 'User=' or i == 'User=root':
				container_user_re_b = "not user for the container has been created:"
		else:
				container_user_re_b = "user for the container has been created:"
	return container_user_re_b

def output():
	docker_version_re = docker_version()
	docker_root_re = docker_root()
	container_user_re_a = container_user()
	container_user_re_b = container_user()
	print (colored('# --------------------------------------------------------------------------------------------\n\
# CIS Docker 1.6 Benchmark\n\
# # v1.0.0 - 04-22-2015\n\
# # ------------------------------------------------------------------------------------------\n\
	', 'green'))
	print (colored('Docker Host',attrs=['bold']))
	print (colored('INFO   ', 'blue'), docker_version_re)
	print (colored('WARN   ', 'red'), docker_root_re)
	print (colored('Docker Images',attrs=['bold']))
	print (colored('WARN   ', 'red'), container_user_re_a)
    print (colored('WARN   ', 'red'), container_user_re_b)

if __name__ == "__main__":     
	output()