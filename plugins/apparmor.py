###Profile containers#
###CIS_Version 1.0.0:1.6#

import os
from termcolor import colored
from tabulate import tabulate
from sdk.containers_id_list import *
#from sdk.containers_image_name_list import containerimagelist
#import sdk.containers_image_name_list as containers_image_name_list

class ApparmorPlugin(containerlist):
    """Verify AppArmor Profile, if applicable"""
    def __init__(test):
        test.lst_con_img=[]
        test.lst_con_apparmor=[]
        test.lst_apparmor_co=[]
        test.lst_apparmor_co_st=[]
        #test.lst_con_img_name=[]
    
    def apparmor_scan(test):
        super().__init__()
        lst_str =  str(test.lst)
        lst_con_img_name = test.con_img_lst
        if lst_str == '[]':
            apparmor_output_cmd = 'containers not running'
        else:
            #con_id = test.lst
            #for d in (con_id):
            #    docker_con_img_name_cmd = "docker inspect " + d + " --format='{{.Config.Image}}'"
            #    docker_con_img_name_output = os.popen(docker_con_img_name_cmd).read()
            #    docker_con_img_name = docker_con_img_name_output.rstrip()
            #    docker_con_img_name_str = str(docker_con_img_name)
            #    test.lst_con_img_name.append(docker_con_img_name_str)
            
            lst_con_img_a = "\n".join(lst_con_img_name)
            images_output = lst_con_img_a
            images = test.lst
            for im in (images):
                apparmor_cmd = "docker inspect " + im + " --format 'AppArmorProfile={{.AppArmorProfile}}'"
                apparmor_output = os.popen(apparmor_cmd).read()
                apparmor_profile = apparmor_output.rstrip()
                apparmor_profile_str = str(apparmor_profile)
                test.lst_con_apparmor.append(apparmor_profile_str)
            apparmor_profile_str_a_s = test.lst_con_apparmor
            for i in (apparmor_profile_str_a_s):
                if i == 'AppArmorProfile=':
                        apparmor_co = 'Verify AppArmor Profile, if applicable'
                        apparmor_co_st = colored('WARN  ', 'red')
                        test.lst_apparmor_co.append(apparmor_co)
                        test.lst_apparmor_co_st.append(apparmor_co_st)
                else:
                        apparmor_co = 'AppArmor Profile available'
                        apparmor_co_st = colored('PASS  ', 'green')
                        test.lst_apparmor_co.append(apparmor_co)                      
                        test.lst_apparmor_co_st.append(apparmor_co_st)
            f_app = "\n".join(test.lst_apparmor_co)
            f_st_app = "\n".join(test.lst_apparmor_co_st)
            apparmor_co_f = f_app
            apparmor_co_f_st = f_st_app
            table_apparmor = [[apparmor_co_f_st , images_output , apparmor_co_f]]
            apparmor_output_cmd = tabulate(table_apparmor)
        return apparmor_output_cmd

