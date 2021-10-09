from tabulate import tabulate
from sdk.containers import *
from .severity import *

class Print(object):

    def container_appar_print():
        lst_apparmor_co=[]
        lst_apparmor_co_st=[]
        con_id_lst = ContainerList.container_id()
        _con_id_lst = str(con_id_lst)
        lst_con_img_name = ContainerList.container_img_name()
        lst_con_img_a = "\n".join(lst_con_img_name)
        images_output = lst_con_img_a 
        apparmor_profile_str_a_s = ContainerList.container_appar()
        if _con_id_lst == '[]':
            apparmor_output = 'containers not running'

        else: 
            for i in (apparmor_profile_str_a_s):
                    if i == 'AppArmorProfile=':
                            apparmor_co = 'Verify AppArmor Profile, if applicable'
                            apparmor_co_st = Serverity.wan()
                            lst_apparmor_co.append(apparmor_co)
                            lst_apparmor_co_st.append(apparmor_co_st)
                    else:
                            apparmor_co = 'AppArmor Profile available'
                            apparmor_co_st = Serverity.pas()
                            lst_apparmor_co.append(apparmor_co)                      
                            lst_apparmor_co_st.append(apparmor_co_st)
            f_app = "\n".join(lst_apparmor_co)
            f_st_app = "\n".join(lst_apparmor_co_st)
            apparmor_co_f = f_app
            apparmor_co_f_st = f_st_app
            table_apparmor = [[apparmor_co_f_st , images_output , apparmor_co_f]]
            apparmor_output = tabulate(table_apparmor)
        return apparmor_output