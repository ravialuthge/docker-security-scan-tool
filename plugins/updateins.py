###Profile images#
###CIS_Version 1.0.0:1.12.0#

import os
from termcolor import colored
from tabulate import tabulate
from sdk.images_list import *

class updateins(imageslist):
    """Do not use update instructions alone in the Dockerfile"""
    def __init__(test):
        test._update_instruction_co=[]
        test._update_instruction_co_st=[]

    def updateins_scan(test):
        
        super().__init__()
        lst_str =  test.lst
        _img_name = test.lst_img_name
        images_output = "\n".join(_img_name)
        if lst_str == '[]':
            update_instruction_output = 'image not found'
        else:
            images = lst_str
            for im in (images):
                update_ins_cmd = 'docker history ' + im + " | grep -e 'update'"
                update_ins_output = os.popen(update_ins_cmd).read()
                update_ins_output_a = update_ins_output.splitlines()
                if update_ins_output_a  == []:
                        update_instruction_co = 'Ensure update instructions are not used alone in the Dockerfile'
                        update_instruction_co_st = colored('INFO  ', 'blue')
                        test._update_instruction_co.append(update_instruction_co)
                        test._update_instruction_co_st.append(update_instruction_co_st)
                    
                else:
                        update_instruction_co = 'update instructions are used in the Dockerfile'
                        update_instruction_co_st = colored('PASS  ', 'green')
                        test._update_instruction_co.append(update_instruction_co)
                        test._update_instruction_co_st.append(update_instruction_co_st)
                
            update_instruction_co_f = "\n".join(test._update_instruction_co)
            update_instruction_co_f_st = "\n".join(test._update_instruction_co_st)
            update_instruction_table = [[update_instruction_co_f_st , images_output , update_instruction_co_f]]
            update_instruction_output = tabulate(update_instruction_table)
            return update_instruction_output