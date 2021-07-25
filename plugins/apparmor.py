import os
from termcolor import colored
from tabulate import tabulate
import docker
import sdk.containers as containers

class apparmor(containers.containerlist):
    """Verify AppArmor Profile, if applicable"""
    def __init__(self):
        self.container_ch_cmd_a = self.container_ch_cmd_a

    def scan(self):
        
        f_app = open("re_apparmor.txt", "w")
        f_st_app = open("re_st_apparmor.txt", "w")
        f_st_app_images = open("re_st_apparmor_images.txt", "w")
        f_st_app_images_a = open("re_st_apparmor_images_a.txt", "w")
        f_st_app_images_id = open("re_st_apparmor_images_id.txt", "w")
        
        container_ch_cmd = self.container_ch_cmd_a
        if container_ch_cmd == "":
            print (container_ch_cmd)
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
                f_st_app_images.write(vv)
                f_st_app_images.write("\n")
                a_id = container.id
                f_st_app_images_id.write(a_id)
                f_st_app_images_id.write("\n")
            f_st_app_images = open("re_st_apparmor_images.txt", "r")
            images_output = f_st_app_images.read()
            f_st_app_images_id = open("re_st_apparmor_images_id.txt", "r")
            images_output_id =  f_st_app_images_id.read()   
            images = images_output_id.splitlines()
            for im in (images):
                apparmor_cmd = "docker inspect " + im + " --format 'AppArmorProfile={{.AppArmorProfile}}'"
                apparmor_output = os.popen(apparmor_cmd).read()
                apparmor_profile = apparmor_output.rstrip()
                apparmor_profile_str = str(apparmor_profile)
                f_st_app_images_a.write(apparmor_profile_str)
                f_st_app_images_a.write("\n")
            f_st_app_images_a = open("re_st_apparmor_images_a.txt", "r")
            apparmor_profile_str_a =  f_st_app_images_a.read()   
            apparmor_profile_str_a_s = apparmor_profile_str_a.split() 
            for i in (apparmor_profile_str_a_s):
                if i == 'AppArmorProfile=':
                        apparmor_co = 'Verify AppArmor Profile, if applicable'
                        apparmor_co_st = colored('WARN  ', 'red')
                else:
                        apparmor_co = 'AppArmor Profile available'
                        apparmor_co_st = colored('PASS  ', 'green')
                f_app.write(apparmor_co)
                f_app.write("\n")
                f_st_app.write(apparmor_co_st)
                f_st_app.write("\n")
            f_app= open("re_apparmor.txt", "r")
            f_st_app= open("re_st_apparmor.txt", "r")
            apparmor_co_f = f_app.read()
            apparmor_co_f_st = f_st_app.read()
            table_apparmor = [[apparmor_co_f_st , images_output , apparmor_co_f]]
            print (tabulate(table_apparmor))



class containerlist(object):
    def __init__(self): 
        lst=[]
        client = docker.from_env()
        for container in client.containers.list():
                    container_ch_cmd_a = container.id
                    lst.append(container_ch_cmd_a)
        self.lst = lst 
    def container(self):
        self.lst = self.lst        
        return self.lst        


class apparmor(containerlist):
    """Verify AppArmor Profile, if applicable"""
    def __init__(self):
        super().__init__()
        f_app = open("re_apparmor.txt", "w")
        f_st_app = open("re_st_apparmor.txt", "w")
        f_st_app_images = open("re_st_apparmor_images.txt", "w")
        f_st_app_images_a = open("re_st_apparmor_images_a.txt", "w")
        f_st_app_images_id = open("re_st_apparmor_images_id.txt", "w")
        if self.lst == "[]":
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
                f_st_app_images.write(vv)
                f_st_app_images.write("\n")
                a_id = container.id
                f_st_app_images_id.write(a_id)
                f_st_app_images_id.write("\n")
            f_st_app_images = open("re_st_apparmor_images.txt", "r")
            images_output = f_st_app_images.read()
            f_st_app_images_id = open("re_st_apparmor_images_id.txt", "r")
            images_output_id =  f_st_app_images_id.read()   
            images = images_output_id.splitlines()
            for im in (images):
                apparmor_cmd = "docker inspect " + im + " --format 'AppArmorProfile={{.AppArmorProfile}}'"
                apparmor_output = os.popen(apparmor_cmd).read()
                apparmor_profile = apparmor_output.rstrip()
                apparmor_profile_str = str(apparmor_profile)
                f_st_app_images_a.write(apparmor_profile_str)
                f_st_app_images_a.write("\n")
            f_st_app_images_a = open("re_st_apparmor_images_a.txt", "r")
            apparmor_profile_str_a =  f_st_app_images_a.read()   
            apparmor_profile_str_a_s = apparmor_profile_str_a.split() 
            for i in (apparmor_profile_str_a_s):
                if i == 'AppArmorProfile=':
                        apparmor_co = 'Verify AppArmor Profile, if applicable'
                        apparmor_co_st = colored('WARN  ', 'red')
                else:
                        apparmor_co = 'AppArmor Profile available'
                        apparmor_co_st = colored('PASS  ', 'green')
                f_app.write(apparmor_co)
                f_app.write("\n")
                f_st_app.write(apparmor_co_st)
                f_st_app.write("\n")
            f_app= open("re_apparmor.txt", "r")
            f_st_app= open("re_st_apparmor.txt", "r")
            apparmor_co_f = f_app.read()
            apparmor_co_f_st = f_st_app.read()
            table_apparmor = [[apparmor_co_f_st , images_output , apparmor_co_f]]
            print (tabulate(table_apparmor))


object2 = apparmor()