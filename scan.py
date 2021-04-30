import os
import subprocess
import re
from termcolor import colored
from tabulate import tabulate
import sys
import getopt

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
	images_ch_cmd = "docker images -q  2> /dev/null"
	f = open("re.txt", "w")
	f_st = open("re_st.txt", "w")
	if os.popen(images_ch_cmd).read() == "":
		container_user_co = 'images not found'
	else:
		container_user_output = os.popen(container_user_cmd).read()
		images_output = os.popen(images_cmd).read()
		images = images_output.split()
		container_users = container_user_output.split()
		for i in (container_users):
		 if i == 'User=' or i == 'User=root':
				container_user_co = 'not user for the container has been created'
				container_user_co_st = colored('WARN  ', 'red')
		 else:
				container_user_co = 'user for the container has been created'
				container_user_co_st = colored('PASS  ', 'green')
		f.write(container_user_co)
		f.write("\n")
		f_st.write(container_user_co_st)
		f_st.write("\n")
		f= open("re.txt", "r")
		f_st= open("re_st.txt", "r")
		container_user_co_f = f.read()
		container_user_co_f_st = f_st.read()
		table = [[container_user_co_f_st , images_output , container_user_co_f]]
		return table
    

def output():
	docker_version_re = docker_version()
	docker_root_re = docker_root()
	table = container_user()
	
	banner = (colored('# --------------------------------------------------------------------------------------------\n\
# CIS Docker 1.6 Benchmark\n\
# # v1.0.0 - 04-22-2015\n\
# --------------------------------------------------------------------------------------------\n\
	', 'green', attrs=['bold']))

	sc_ho	= colored('Docker Host',attrs=['bold'])
	sc_ho_1	= colored('INFO   ', 'blue'), docker_version_re
	sc_ho_2	= colored('WARN   ', 'red'), docker_root_re
	sc_im	= colored('Docker Images',attrs=['bold'])
	sc_im_1	= (tabulate(table))
	arguments = len(sys.argv) -1
	if arguments == 0:
		print (banner)
		print (sc_ho)
		print (sc_ho_1)
		print (sc_ho_2)
		print (sc_im)
		print (sc_im_1)
	elif (sys.argv[1] == '-s' or sys.argv[1] == '--scan') and sys.argv[2] == 'host':
		print (banner)
		print (sc_ho)
		print (sc_ho_1)
		print (sc_ho_2)
	elif (sys.argv[1] == '-s' or sys.argv[1] == '--scan') and sys.argv[2] == 'images':
		print (banner)
		print (sc_im)
		print (sc_im_1)
	elif (sys.argv[1] == '-h' or sys.argv[1] == '--help'):
		print ("help")
	else:
		print ("error")


if __name__ == "__main__":     
	output()
os.remove("re.txt")
os.remove("re_st.txt")