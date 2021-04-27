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
		print ("Docker is up to date")
	elif install_version != latest_version:
		print ("Docker not update")
	else:
		print ("Docker not install")
	return docker_root()

def docker_root():
	root_dir_ch_cmd = "df -h | grep $(docker info -f '{{ .DockerRootDir }}') | awk '{print $6}'"
	root_dir_output = subprocess.check_output(["docker", "info" , "--format" , "'{{.DockerRootDir}}'"])
	root_dir_x = root_dir_output.decode("utf-8")
	root_dir = root_dir_x.replace("'",'')
	root_dir_ch_output = os.popen(root_dir_ch_cmd).read()
	root_dir_ch = root_dir_ch_output.rstrip()

	if root_dir == root_dir_ch:
		print ("crated separate partition for docker root directory")
	else:
		print ("not crated separate partition for docker root directory")

docker_version()