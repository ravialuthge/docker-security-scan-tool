from tabulate import tabulate
from sdk.containers import *

class Print(object):

    def container_appar_print(apparmor_output,lst_apparmor_co,lst_apparmor_co_st):
            lst_con_img_name = ContainerList().container_img_name()
            lst_con_img_a = "\n".join(lst_con_img_name)
            images_output = lst_con_img_a
            
                
            lst_apparmor_co = lst_apparmor_co
            lst_apparmor_co_st = lst_apparmor_co_st
            f_app = "\n".join(lst_apparmor_co)
            f_st_app = "\n".join(lst_apparmor_co_st)
            apparmor_co_f = f_app
            apparmor_co_f_st = f_st_app
            
            table_apparmor = [[apparmor_co_f_st , images_output , apparmor_co_f]]
            apparmor_output = tabulate(table_apparmor)
            return apparmor_output