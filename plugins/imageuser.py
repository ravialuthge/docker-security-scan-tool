import os
import docker
from termcolor import colored
from tabulate import tabulate
from sdk.images_list import *

class ImageUser(imageslist):
    """Create a user for the container"""
    def __init__(test):
        test.lst_image_user_cmd=[]
        test.lst_imageuser_output_cmd=[]
        test.lst_img_user_co_st=[]
        test.lst_img_name=[]

    def imageuser_scan(test):
        super().__init__()
        lst_str =  str(test.lst)
        client = docker.from_env()
        for image in client.images.list():
                    images_ch_cmd_a_s = image.tags
                    images_ch_cmd_str = str(images_ch_cmd_a_s)
                    bbc = images_ch_cmd_str.replace("[",'')
                    bbcdr = bbc.replace("]",'')
                    test.lst_img_name.append(bbcdr)
        img_name_lst_str = test.lst_img_name
        images_output = "\n".join(img_name_lst_str)
        if lst_str == '[]':
            imageuser_output = 'image not found'
        else:
            for im in (lst_str):
                image_user_cmd = "docker image inspect" + im + "-f 'User={{.Config.User}}'"
                image_user_cmd_output = os.popen(image_user_cmd).read()
                image_user = image_user_cmd_output.rstrip()
                image_user_str = str(image_user)
                test.lst_image_user_cmd.append(image_user_str)
            image_user_str_a_s = test.lst_image_user_cmd
            for i in (image_user_str_a_s):
                if i == 'User=' or i == 'User=root':
                        imageuser_output_cmd = 'not user for the container has been created'
                        img_user_co_st = colored('WARN  ', 'red')
                        test.lst_imageuser_output_cmd.append(imageuser_output_cmd)
                        test.lst_img_user_co_st.append(img_user_co_st)
                else:
                        imageuser_output_cmd = 'user for the container has been created'
                        img_user_co_st = colored('PASS  ', 'green')
                        test.lst_imageuser_output_cmd.append(imageuser_output_cmd)
                        test.lst_img_user_co_st.append(img_user_co_st)
            f_user = "\n".join(test.lst_imageuser_output_cmd)
            f_st_user = "\n".join(test.lst_img_user_co_st)
            img_user_co_f = f_user
            img_user_co_f_st = f_st_user
            table_img_user = [[img_user_co_f_st , images_output , img_user_co_f]]
            imageuser_output = tabulate(table_img_user)
        return imageuser_output
            
