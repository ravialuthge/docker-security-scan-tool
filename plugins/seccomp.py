import os
import subprocess
import re
from termcolor import colored
from tabulate import tabulate

class seccomp:
    def scan(test):
        seccomp_ch_cmd = "docker ps -q  2> /dev/null"
        f_seccomp = open("re_seccomp.txt", "w")
        f_st_seccomp = open("re_st_seccomp.txt", "w")
        if os.popen(seccomp_ch_cmd).read() == "":
            table_seccomp_out = 'containers not running'
            print (table_seccomp_out)
        else:
            seccomp_ch_cmd = "docker inspect $(docker ps -q) --format  'SecurityOpt={{ .HostConfig.SecurityOpt }}'"
            container_image_cmd = "docker inspect $(docker ps -q) --format='{{.Config.Image}}'"
            container_name_cmd = "docker inspect $(docker ps -q) --format='{{.Name}}'"
            seccomp_ch_output = os.popen(seccomp_ch_cmd).read()
            container_image_output = os.popen(container_image_cmd).read()
            container_name_output_all = os.popen(container_name_cmd).read()
            container_name_output = container_name_output_all.replace("/",'')

            seccomp_ch = seccomp_ch_output.splitlines()

            for h in (seccomp_ch):
                    if h == '[seccomp:unconfined]':
                            seccomp_ch_co = 'Do not disable default seccomp profile'
                            seccomp_ch_co_st = colored('WARN  ', 'red')
                    else:
                            seccomp_ch_co = 'enabled default seccomp profile'
                            seccomp_ch_co_st = colored('PASS  ', 'green')
                    f_seccomp.write(seccomp_ch_co)
                    f_seccomp.write("\n")
                    f_st_seccomp.write(seccomp_ch_co_st)
                    f_st_seccomp.write("\n")
            f_seccomp= open("re_seccomp.txt", "r")
            f_st_seccomp= open("re_st_seccomp.txt", "r")
            seccomp_ch_co_f = f_seccomp.read()
            seccomp_ch_co_f_st = f_st_seccomp.read()
            table_seccomp = [[seccomp_ch_co_f_st , container_image_output , container_name_output , seccomp_ch_co_f]]
            print (tabulate(table_seccomp))