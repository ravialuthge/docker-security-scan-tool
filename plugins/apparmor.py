import os
from termcolor import colored
from tabulate import tabulate
import docker
from sdk.containers_list import *

class apparmor(containerlist):
    """Verify AppArmor Profile, if applicable"""
    def __init__(test):
        test.lst_con_img=[]
        test.lst_con_apparmor=[]
        test.lst_apparmor_co=[]
        test.lst_apparmor_co_st=[]
    
    def apparmor_scan(test):
        super().__init__()
        lst_str =  str(test.lst)
        if lst_str == '[]':
            apparmor_output_cmd = 'containers not running'
        else:
            client = docker.from_env()
            for container in client.containers.list():
                a = container.image
                ab = str(a)
                b = ab.split()
                bb = b[1]
                bbc = bb.replace(">",'')
                vv = bbc.replace("'",'')
                test.lst_con_img.append(vv)
            lst_con_img_a = "\n".join(test.lst_con_img)
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
        print (apparmor_output_cmd)

#object1 = apparmor()
#output = object1.apparmor_scan()
#print (output)
