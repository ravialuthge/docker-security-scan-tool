#Profile containers()
#CIS_Version 1.0.0:1.12.0

import os
from termcolor import colored
from tabulate import tabulate
from sdk.containers_id_list import *

class healthcheck(containerlist):
    """Check container health at runtime"""
    def __init__(test):
        test.lst_con_img_name=[]
        test.lst_health_ch=[]
        test.lst_health_ch_co=[]
        test.lst_health_ch_co_st=[]

    def healthcheck_scan(test):
        
        super().__init__()
        lst_str =  str(test.lst)
        if lst_str == '[]':
            table_he_output = 'containers not running'
        else:
            con_id = test.lst
            for d in (con_id):
                docker_con_img_name_cmd = "docker inspect " + d + " --format='{{.Config.Image}}'"
                docker_con_img_name_output = os.popen(docker_con_img_name_cmd).read()
                docker_con_img_name = docker_con_img_name_output.rstrip()
                docker_con_img_name_str = str(docker_con_img_name)
                test.lst_con_img_name.append(docker_con_img_name_str)
                health_ch_cmd = "docker inspect " + d + " --format='{{.Config.Healthcheck}}'"
                health_ch_output = os.popen(health_ch_cmd).read()
                health_ch_name = health_ch_output.rstrip()
                health_ch_name_str = str(health_ch_name)
                test.lst_health_ch.append(health_ch_name_str)
            lst_con_img_a = "\n".join(test.lst_con_img_name)
            container_image_output = lst_con_img_a
            _container_name_output = test.con_name_lst
            container_name_output = "\n".join(_container_name_output)
            health_ch = test.lst_health_ch

            for h in (health_ch):
                    if h == '<nil>':
                            health_ch_co = 'not added health check instructions'
                            health_ch_co_st = colored('WARN  ', 'red')
                            test.lst_health_ch_co.append(health_ch_co)
                            test.lst_health_ch_co_st.append(health_ch_co_st)
                    else:
                            health_ch_co = 'added health check instructions'
                            health_ch_co_st = colored('PASS  ', 'green')
                            test.lst_health_ch_co.append(health_ch_co)
                            test.lst_health_ch_co_st.append(health_ch_co_st)
            health_ch_co_f = "\n".join(test.lst_health_ch_co)
            health_ch_co_f_st = "\n".join(test.lst_health_ch_co_st)
            table_he = [[health_ch_co_f_st , container_image_output , container_name_output , health_ch_co_f]]
            table_he_output = tabulate(table_he)
        return table_he_output