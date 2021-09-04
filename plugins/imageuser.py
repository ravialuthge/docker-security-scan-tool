import os
from termcolor import colored
from tabulate import tabulate
from sdk.images_list import *
from sdk.images_name_list import *

class ImageUser(imageslist,imagesnamelist):
    """Create a user for the container"""
    def __init__(test):
        test.lst_image_user_cmd=[]
        test.lst_imageuser_output_cmd=[]
        test.lst_img_user_co_st=[]

    def imageuser_scan(test):
        super().__init__()
        lst_str =  test.lst
        _img_name = test.img_name_lst
        img_name = "\n".join(_img_name)
        if lst_str == '[]':
            imageuser_output = 'image not found'
        else:
            for im in (lst_str):
                image_user_cmd = "docker image inspect " + im + " -f 'User={{.Config.User}}'"
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
            table_img_user = [[img_user_co_f_st , img_name , img_user_co_f]]
            imageuser_output = tabulate(table_img_user)
        return imageuser_output
            
