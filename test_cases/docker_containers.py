import os
import subprocess
import re
from termcolor import colored

def health_check():
	
	health_ch_cmd = "docker inspect $(docker ps -q) --format='{{.Config.Healthcheck}}'"
	container_image_cmd = "docker inspect $(docker ps -q) --format='{{.Config.Image}}'"
	container_name_cmd = "docker inspect $(docker ps -q) --format='{{.Name}}'"
	container_ch_cmd = "docker ps -q  2> /dev/null"
	f_he = open("re_he.txt", "w")
	f_st_he = open("re_st_he.txt", "w")
	if os.popen(container_ch_cmd).read() == "":
		table_he_out = 'containers not running'
		table_he_a = [[table_he_out]]
		return table_he_a
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

def apparmor():
	images_cmd =  "docker images --format '{{ .Repository }}:{{ .Tag }}'"
	apparmor_cmd = "docker ps -q | xargs docker inspect --format '{{ .Id }}: AppArmorProfile={{ .AppArmorProfile }}'"
	images_ch_cmd = "docker images -q  0> /dev/null"
	f_app = open("re_apparmor.txt", "w")
	f_st_app = open("re_st_apparmor.txt", "w")
	if os.popen(images_ch_cmd).read() == "":
		container_user_co = 'images not found'
	else:
		apparmor_output = os.popen(apparmor_cmd).read()
		images_output = os.popen(images_cmd).read()
	
		apparmor_profile = apparmor_output.split()
		
		for i in (apparmor_profile):
		 if i == 'AppArmorProfile=':
				apparmor_co = 'Verify AppArmor Profile'
				apparmor_co_st = colored('WARN  ', 'red')
		 else:
				apparmor_co = 'AppArmor Profile available'
				apparmor_co_st = colored('PASS  ', 'green')
		 f_app.write(apparmor_co)
		 f_app.write("\n")
		 f_st_app.write(apparmor_co_st)
		 f_st_app.write("\n")
		f_app= open("re.txt", "r")
		f_st_app= open("re_st.txt", "r")
		apparmor_co_f = f_app.read()
		apparmor_co_f_st = f_st_app.read()
		table_apparmor = [[apparmor_co_f_st , images_output , apparmor_co_f]]
		return table_apparmor


	
