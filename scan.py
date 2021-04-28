import os
import subprocess
import re

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
	return docker_root()

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
	return output(docker_root_re)

def output(docker_root_re):
	print ('# --------------------------------------------------------------------------------------------\n\
# CIS Docker $version Benchmark\n\
# # v1.0.0 - 04-22-2015\n\
# # ---------------------------------------------------------------------------------------------\n\
	')
	print ('INFO   ', docker_version_re)
	print ('WARN   ', docker_root_re)
     
docker_version()