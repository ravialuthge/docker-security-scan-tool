import os
from termcolor import colored
from tabulate import tabulate
import docker

class  containeruser:
    """Create a user for the container"""
    def scan(test):
        f = open("re.txt", "w")
        f_st = open("re_st.txt", "w")
        f_st_img = open("re_st_img.txt", "w")
        images_cmd =  "docker images --format '{{ .Repository }}:{{ .Tag }}'"
        container_user_cmd = "docker image inspect -f 'User={{.Config.User}}' $(docker images --format '{{ .Repository }}:{{ .Tag }}')"
        client = docker.from_env()
        for image in client.images.list():
            images_ch_cmd_a = image.id
            f_st_img.write(images_ch_cmd_a)
        f_st_img = open("re_st_img.txt", "r")
        images_ch_cmd = f_st_img.read()
        if images_ch_cmd == "":
            print ('images not found')
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
            print (tabulate(table))
