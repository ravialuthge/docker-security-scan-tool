import os
from termcolor import colored
from tabulate import tabulate
import docker
from sdk.containers_list import *

class apparmor(containerlist):
    """Verify AppArmor Profile, if applicable"""
    def __init__(self):
        super().__init__()
        if self.lst == "[]":
            print ('containers not running')
        else:
            lst_con_img=[]
            lst_con_apparmor=[]
            lst_apparmor_co=[]
            lst_apparmor_co_st=[]
            client = docker.from_env()
            for container in client.containers.list():
                a = container.image
                ab = str(a)
                b = ab.split()
                bb = b[1]
                bbc = bb.replace(">",'')
                vv = bbc.replace("'",'')
                lst_con_img.append(vv)
            lst_con_img_a = "\n".join(lst_con_img)
            images_output = lst_con_img_a
            images = self.lst
            for im in (images):
                apparmor_cmd = "docker inspect " + im + " --format 'AppArmorProfile={{.AppArmorProfile}}'"
                apparmor_output = os.popen(apparmor_cmd).read()
                apparmor_profile = apparmor_output.rstrip()
                apparmor_profile_str = str(apparmor_profile)
                lst_con_apparmor.append(apparmor_profile_str)
            apparmor_profile_str_a_s = lst_con_apparmor
            for i in (apparmor_profile_str_a_s):
                if i == 'AppArmorProfile=':
                        apparmor_co = 'Verify AppArmor Profile, if applicable'
                        apparmor_co_st = colored('WARN  ', 'red')
                        lst_apparmor_co.append(apparmor_co)
                        lst_apparmor_co_st.append(apparmor_co_st)
                else:
                        apparmor_co = 'AppArmor Profile available'
                        apparmor_co_st = colored('PASS  ', 'green')
                        lst_apparmor_co.append(apparmor_co)                      
                        lst_apparmor_co_st.append(apparmor_co_st)
            f_app = "\n".join(lst_apparmor_co)
            f_st_app = "\n".join(lst_apparmor_co_st)
            apparmor_co_f = f_app
            apparmor_co_f_st = f_st_app
            table_apparmor = [[apparmor_co_f_st , images_output , apparmor_co_f]]
            print (tabulate(table_apparmor))


object2 = apparmor()