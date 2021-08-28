import os
from termcolor import colored
from tabulate import tabulate
from sdk.images_list import *
from sdk.images_name_list import *

class ImageUser(imageslist):
    """Create a user for the container"""
    def __init__(test):
        test.images_cmd =  "docker images --format '{{.Repository}}:{{.Tag}}'"

    def imageuser_scan(test):
        super().__init__()
        lst_str =  str(test.lst)
        if lst_str == '[]':
            imageuser_output_cmd = 'image not found'
        else:
            
            for im in (images):
                container_user_cmd = "docker image inspect -f 'User={{.Config.User}}' $(docker images --format '{{ .Repository }}:{{ .Tag }}')"

            
            container_user_output = os.popen(container_user_cmd).read()
            images_output = os.popen(test.images_cmd).read()
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
