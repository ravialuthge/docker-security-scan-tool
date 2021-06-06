import os
from termcolor import colored

class apparmor:
    def scan(test):
        images_cmd =  "docker inspect $(docker ps -q) --format='{{.Config.Image}}'"
        apparmor_cmd = "docker ps -q | xargs docker inspect --format 'AppArmorProfile={{ .AppArmorProfile }}'"
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
            print (table_apparmor)