import os
from termcolor import colored
from tabulate import tabulate
import docker
from sdk.containers_list import *

class apparmor(containerlist):
    """Verify AppArmor Profile, if applicable"""
    def __init__(self):
        self.lst_con_img=[]
        self.lst_con_apparmor=[]
        self.lst_apparmor_co=[]
        self.lst_apparmor_co_st=[]
    
    def apparmor_scan(self):
        super().__init__()
        print (self.lst)
        if self.lst == '[]':
            print ('containers not running')
        else:
            client = docker.from_env()
            for container in client.containers.list():
                a = container.image
                ab = str(a)
                b = ab.split()
                bb = b[1]
                bbc = bb.replace(">",'')
                vv = bbc.replace("'",'')
                self.lst_con_img.append(vv)
            lst_con_img_a = "\n".join(self.lst_con_img)
            images_output = lst_con_img_a
            images = self.lst
            for im in (images):
                apparmor_cmd = "docker inspect " + im + " --format 'AppArmorProfile={{.AppArmorProfile}}'"
                apparmor_output = os.popen(apparmor_cmd).read()
                apparmor_profile = apparmor_output.rstrip()
                apparmor_profile_str = str(apparmor_profile)
                self.lst_con_apparmor.append(apparmor_profile_str)
            apparmor_profile_str_a_s = self.lst_con_apparmor
            for i in (apparmor_profile_str_a_s):
                if i == 'AppArmorProfile=':
                        apparmor_co = 'Verify AppArmor Profile, if applicable'
                        apparmor_co_st = colored('WARN  ', 'red')
                        self.lst_apparmor_co.append(apparmor_co)
                        self.lst_apparmor_co_st.append(apparmor_co_st)
                else:
                        apparmor_co = 'AppArmor Profile available'
                        apparmor_co_st = colored('PASS  ', 'green')
                        self.lst_apparmor_co.append(apparmor_co)                      
                        self.lst_apparmor_co_st.append(apparmor_co_st)
            f_app = "\n".join(self.lst_apparmor_co)
            f_st_app = "\n".join(self.lst_apparmor_co_st)
            apparmor_co_f = f_app
            apparmor_co_f_st = f_st_app
            table_apparmor = [[apparmor_co_f_st , images_output , apparmor_co_f]]
            print (tabulate(table_apparmor))


object1 = apparmor()
output = object1.apparmor_scan()