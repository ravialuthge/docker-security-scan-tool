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

def container_user():
	images_cmd =  "docker images --format '{{ .Repository }}:{{ .Tag }}'"
	container_user_cmd = "docker image inspect -f 'User={{.Config.User}}' $(docker images --format '{{ .Repository }}:{{ .Tag }}')"
	images_ch_cmd = "docker images -q  0> /dev/null"
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

def health_check():
	
	health_ch_cmd = "docker inspect $(docker ps -q) --format='{{.Config.Healthcheck}}'"
	container_image_cmd = "docker inspect $(docker ps -q) --format='{{.Config.Image}}'"
	container_name_cmd = "docker inspect $(docker ps -q) --format='{{.Name}}'"
	container_ch_cmd = "docker ps -q  2> /dev/null"
	f_he = open("re_he.txt", "w")
	f_st_he = open("re_st_he.txt", "w")
	if os.popen(container_ch_cmd).read() == "":
		container_he_co = 'containers not running'
	else:
		health_ch_output = os.popen(health_ch_cmd).read()
		container_image_output = os.popen(container_image_cmd).read()
		container_name_output_all = os.popen(container_name_cmd).read()
		container_name_output = container_name_output_all.replace("/",'')

		health_ch = health_ch_output.splitlines()

		for h in (health_ch):
				if h == '<nil>':
						health_ch_co = 'not added health check instructions'
						health_ch_co_st = colored('WARN  ', 'red')
				else:
						health_ch_co = 'added health check instructions'
						health_ch_co_st = colored('PASS  ', 'green')
				f_he.write(health_ch_co)
				f_he.write("\n")
				f_st_he.write(health_ch_co_st)
				f_st_he.write("\n")
		f_he= open("re_he.txt", "r")
		f_st_he= open("re_st_he.txt", "r")
		health_ch_co_f = f_he.read()
		health_ch_co_f_st = f_st_he.read()
		table_he = [[health_ch_co_f_st , container_image_output , container_name_output , health_ch_co_f]]
		return table_he

def output():
	docker_version_re = docker_version()
	docker_root_re = docker_root()
	table = container_user()
	table_he = health_check()
	full_cmd_arguments = sys.argv

	banner = (colored("# --------------------------------------------------------------------------------------------\n\
# CIS Docker {0} Benchmark\n\
# # {1}\n\
# --------------------------------------------------------------------------------------------\n\
	", 'green', attrs=['bold']))

	sc_ho	= (colored('Docker Host',attrs=['bold']))
	sc_ho_1 = (docker_version_re)
	sc_ho_2 = (docker_root_re)
	sc_im	= (colored('Docker Images',attrs=['bold']))
	sc_im_1	= (tabulate(table))
	sc_co   = (colored('Docker Containers',attrs=['bold']))
	sc_co_1 = (tabulate(table_he))

	arguments = len(sys.argv) -1
	if arguments == 0:
		sub_version="1.2.0"
		main_version="v1.2.0 - 07-29-2019"
		print (banner .format(sub_version, main_version))
		print (sc_ho)
		print (sc_ho_1)
		print (sc_ho_2)
		print (sc_im)
		print (sc_im_1)
		print (sc_co)
		print (sc_co_1)
	elif (sys.argv[1] == '-v' or sys.argv[1] == '--version') and sys.argv[2] == '1.1.0':
		sub_version="1.1.0"
		main_version="v1.1.0 - 07-06-2017"
		print (banner .format(sub_version, main_version))
		print (sc_ho)
		print (sc_ho_1)
		print (sc_ho_2)
		print (sc_im)
		print (sc_im_1)
		print (sc_co)
		print (sc_co_1)
	elif (sys.argv[1] == '-v' or sys.argv[1] == '--version') and (sys.argv[2] == '1.0.0'):
		sub_version="1.6"
		main_version="v1.0.0 - 04-22-2015"
		print (banner .format(sub_version, main_version))
		print (sc_ho)
		print (sc_ho_1)
		print (sc_ho_2)
		print (sc_im)
		print (sc_im_1)
		print (sc_co)
		print (sc_co_1)

		sub_version_a="1.11.0"
		print (banner .format(sub_version_a, main_version))
		print (sc_ho)
		print (sc_ho_1)
		print (sc_ho_2)
		print (sc_im)
		print (sc_im_1)
		print (sc_co)
		print (sc_co_1)

		sub_version_b="1.12.0"
		print (banner .format(sub_version_b, main_version))
		print (sc_ho)
		print (sc_ho_1)
		print (sc_ho_2)
		print (sc_im)
		print (sc_im_1)
		print (sc_co)
		print (sc_co_1)

		sub_version_c="1.13.0"
		print (banner .format(sub_version_c, main_version))
		print (sc_ho)
		print (sc_ho_1)
		print (sc_ho_2)
		print (sc_im)
		print (sc_im_1)
		print (sc_co)
		print (sc_co_1)	
	elif ((sys.argv[1] == '-sv' or sys.argv[1] == '--sub-version') and sys.argv[2] == '1.0.0') and sys.argv[3] == '1.6':
		sub_version="1.6"
		main_version="v1.0.0 - 04-22-2015"
		print (banner .format(sub_version, main_version))
		print (sc_ho)
		print (sc_ho_1)
		print (sc_ho_2)
		print (sc_im)
		print (sc_im_1)
		print (sc_co)
		print (sc_co_1)
	elif ((sys.argv[1] == '-sv' or sys.argv[1] == '--sub-version') and sys.argv[2] == '1.0.0') and sys.argv[3] == '1.11.0':
		sub_version="1.11.0"
		main_version="v1.0.0 - 04-22-2015"
		print (banner .format(sub_version, main_version))
		print (sc_ho)
		print (sc_ho_1)
		print (sc_ho_2)
		print (sc_im)
		print (sc_im_1)
		print (sc_co)
		print (sc_co_1)
	elif ((sys.argv[1] == '-sv' or sys.argv[1] == '--sub-version') and sys.argv[2] == '1.0.0') and sys.argv[3] == '1.12.0':
		sub_version="1.12.0"
		main_version="v1.0.0 - 04-22-2015"
		print (banner .format(sub_version, main_version))
		print (sc_ho)
		print (sc_ho_1)
		print (sc_ho_2)
		print (sc_im)
		print (sc_im_1)
		print (sc_co)
		print (sc_co_1)
	elif ((sys.argv[1] == '-sv' or sys.argv[1] == '--sub-version') and sys.argv[2] == '1.0.0') and sys.argv[3] == '1.13.0':
		sub_version="1.13.0"
		main_version="v1.0.0 - 04-22-2015"
		print (banner .format(sub_version, main_version))
		print (sc_ho)
		print (sc_ho_1)
		print (sc_ho_2)
		print (sc_im)
		print (sc_im_1)
		print (sc_co)
		print (sc_co_1)
	elif (sys.argv[1] == '-s' or sys.argv[1] == '--scan') and sys.argv[2] == 'host':
		sub_version="1.2.0"
		main_version="v1.2.0 - 07-29-2019"
		print (banner .format(sub_version, main_version))
		print (sc_ho)
		print (sc_ho_1)
		print (sc_ho_2)
	elif (sys.argv[1] == '-s' or sys.argv[1] == '--scan') and sys.argv[2] == 'images':
		sub_version="1.2.0"
		main_version="v1.2.0 - 07-29-2019"
		print (banner .format(sub_version, main_version))
		print (sc_im)
		print (sc_im_1)
	elif (sys.argv[1] == '-s' or sys.argv[1] == '--scan') and sys.argv[2] == 'containers':
		sub_version="1.2.0"
		main_version="v1.2.0 - 07-29-2019"
		print (banner .format(sub_version, main_version))
		print (sc_co)
		print (sc_co_1)
	elif (sys.argv[1] == '-h' or sys.argv[1] == '--help'):
		print ("help")
	else:
		print ("error")


if __name__ == "__main__":     
	output()
os.remove("re.txt")
os.remove("re_st.txt")
os.remove("re_he.txt")
os.remove("re_st_he.txt")