import os
import subprocess
import re
from termcolor import colored

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

def update_ins():
	images_cmd =  "docker images --format '{{ .Repository }}:{{ .Tag }}'"
	
	images_ch_cmd = "docker images -q  0> /dev/null"
	f_up = open("re_up.txt", "w")
	f_st_up = open("re_st_up.txt", "w")

	if os.popen(images_ch_cmd).read() == "":
		images_ch_co = 'images not found'
	else:
		images_output = os.popen(images_cmd).read()
		images = images_output.split()
		for im in (images):
			update_ins_cmd = 'docker history ' + im + " | grep -e 'update'"
			update_ins_output = os.popen(update_ins_cmd).read()
			update_ins_output_a = update_ins_output.splitlines()
			if update_ins_output_a  == []:
					update_instruction_co = 'Ensure update instructions are not used alone in the Dockerfile'
					update_instruction_co_st = colored('INFO  ', 'blue')
				
			else:
					update_instruction_co = 'update instructions are used in the Dockerfile'
					update_instruction_co_st = colored('PASS  ', 'green')
			
			f_up.write(update_instruction_co)
			f_up.write("\n")
			f_st_up.write(update_instruction_co_st)
			f_st_up.write("\n")
		f_up= open("re_up.txt", "r")
		f_st_up= open("re_st_up.txt", "r")
		update_instruction_co_f = f_up.read()
		update_instruction_co_f_st = f_st_up.read()
		update_instruction_table = [[update_instruction_co_f_st , images_output , update_instruction_co_f]]
		return update_instruction_table