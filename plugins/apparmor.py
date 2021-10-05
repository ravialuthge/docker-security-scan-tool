###Profile containers#
###CIS_Version 1.0.0:1.6#

from termcolor import colored
from tabulate import tabulate
from sdk.containers_id_list import *

class ApparmorPlugin(containerlist):
    """Verify AppArmor Profile, if applicable"""
    def __init__(test):
        test.lst_con_img=[]
        test.lst_con_apparmor=[]
        test.lst_apparmor_co=[]
        test.lst_apparmor_co_st=[]
    
    def apparmor_scan(test):
        super().__init__()
        lst_str =  str(test.lst)
        lst_con_img_name = test.con_img_lst
        if lst_str == '[]':
            apparmor_output_cmd = 'containers not running'
        else:
           
            lst_con_img_a = "\n".join(lst_con_img_name)
            images_output = lst_con_img_a
            
            apparmor_profile_str_a_s = test._container_appar_list 
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

