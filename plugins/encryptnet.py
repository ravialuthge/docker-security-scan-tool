import os
import subprocess
import re
from termcolor import colored
from tabulate import tabulate

class encryptnet:
    def scan(test):
        f_encryptnet = open("re_encryptnet.txt", "w")
        f_st_encryptnet = open("re_st_encryptnet.txt", "w")
        encryptnet_ch_cmd = "docker network ls --filter driver=overlay --quiet | xargs docker network inspect --format '{{.Name}}'"
        encryptnet_ch_cmd = "docker network ls --filter driver=bridge --quiet | xargs docker network inspect --format '{{ .Options }}'"
        
        encryptnet_ch_output = os.popen(encryptnet_ch_cmd).read()
        container_image_output = os.popen(container_image_cmd).read()
		container_name_output_all = os.popen(container_name_cmd).read()
		container_name_output = container_name_output_all.replace("/",'')

		encryptnet_ch = encryptnet_ch_output.splitlines()

		for h in (encryptnet_ch):
				if h == 'map[encrypted:]':
						encryptnet_ch_co = 'Do not disable default encryptnet profile'
						encryptnet_ch_co_st = colored('WARN  ', 'red')
				else:
						encryptnet_ch_co = 'enabled default encryptnet profile'
						encryptnet_ch_co_st = colored('PASS  ', 'green')
				f_encryptnet.write(encryptnet_ch_co)
				f_encryptnet.write("\n")
				f_st_encryptnet.write(encryptnet_ch_co_st)
				f_st_encryptnet.write("\n")
		f_encryptnet= open("re_encryptnet.txt", "r")
		f_st_encryptnet= open("re_st_encryptnet.txt", "r")
		encryptnet_ch_co_f = f_encryptnet.read()
		encryptnet_ch_co_f_st = f_st_encryptnet.read()
		table_encryptnet = [[encryptnet_ch_co_f_st , container_image_output , container_name_output , encryptnet_ch_co_f]]
		print (tabulate(table_encryptnet))