import os
from termcolor import colored
from tabulate import tabulate

class updateins:
    def scan(test):
        images_cmd =  "docker images --format '{{ .Repository }}:{{ .Tag }}'"
        
        images_ch_cmd = "docker images -q  0> /dev/null"
        f_up = open("re_up.txt", "w")
        f_st_up = open("re_st_up.txt", "w")

        if os.popen(images_ch_cmd).read() == "":
            images_ch_co = 'images not found'
        else:
            images_output = os.popen(images_cmd).read()
            images = images_output.split()
            for im in (images):
                update_ins_cmd = 'docker history ' + im + " | grep -e 'update'"
                update_ins_output = os.popen(update_ins_cmd).read()
                update_ins_output_a = update_ins_output.splitlines()
                if update_ins_output_a  == []:
                        update_instruction_co = 'Ensure update instructions are not used alone in the Dockerfile'
                        update_instruction_co_st = colored('INFO  ', 'blue')
                    
                else:
                        update_instruction_co = 'update instructions are used in the Dockerfile'
                        update_instruction_co_st = colored('PASS  ', 'green')
                
                f_up.write(update_instruction_co)
                f_up.write("\n")
                f_st_up.write(update_instruction_co_st)
                f_st_up.write("\n")
            f_up= open("re_up.txt", "r")
            f_st_up= open("re_st_up.txt", "r")
            update_instruction_co_f = f_up.read()
            update_instruction_co_f_st = f_st_up.read()
            update_instruction_table = [[update_instruction_co_f_st , images_output , update_instruction_co_f]]
            print (tabulate(update_instruction_table))