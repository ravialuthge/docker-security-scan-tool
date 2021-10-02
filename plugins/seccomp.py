###Profile containers#
###CIS_Version 1.0.0:1.11.0#

from termcolor import colored
from tabulate import tabulate
from sdk.containers_id_list import *

class seccomp(containerlist):
    """Do not disable default seccomp profile""" 
    def __init__(test):
        
         test.lst_seccomp_ch_co=[]
         test.lst_seccomp_ch_co_st=[]

    def seccomp_scan(test):
        super().__init__()
        lst_str =  str(test.lst)
        if lst_str == '[]':
            table_seccomp_out = 'containers not running'
        else:
            
            lst_con_img_name = test.con_img_lst
            lst_con_img_a = "\n".join(lst_con_img_name)
            container_image_output = lst_con_img_a
            _container_name_output = test.con_name_lst
            container_name_output = "\n".join(_container_name_output)
            seccomp_ch = test._container_secc_list

            for h in (seccomp_ch):
                    if h == 'None':
                            seccomp_ch_co = 'Do not disable default seccomp profile'
                            seccomp_ch_co_st = colored('WARN  ', 'red')
                            test.lst_seccomp_ch_co.append(seccomp_ch_co)
                            test.lst_seccomp_ch_co_st.append(seccomp_ch_co_st)
                    else:
                            seccomp_ch_co = 'enabled default seccomp profile'
                            seccomp_ch_co_st = colored('PASS  ', 'green')
                            test.lst_seccomp_ch_co.append(seccomp_ch_co)
                            test.lst_seccomp_ch_co_st.append(seccomp_ch_co_st)

            seccomp_ch_co_f = "\n".join(test.lst_seccomp_ch_co)
            seccomp_ch_co_f_st = "\n".join(test.lst_seccomp_ch_co_st)
            table_seccomp = [[seccomp_ch_co_f_st , container_image_output , container_name_output , seccomp_ch_co_f]]
            table_seccomp_out = tabulate(table_seccomp)
        return table_seccomp_out