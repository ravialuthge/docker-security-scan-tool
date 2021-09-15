import os
from termcolor import colored
from tabulate import tabulate
from sdk.docker_net_name import *

class encryptnet(netlist):
    """Encrypt data exchanged between containers on different nodes on the overlay network"""
    def __init__(test):
            test.lst_encryptnet_name=[]
            test._encryptnet_ch_co=[]
            test._encryptnet_ch_co_st=[]

            
    def encryptnet_scan(test):
            super().__init__()
            _netlist_output_lst = test.netlist_output_lst
            encryptnet_ch_output = "\n".join(_netlist_output_lst)

            for d in (_netlist_output_lst):
                
                encryptnet_cmd = "docker network inspect " + d + " --format '{{.Name}} {{.Options}}'"
                encryptnet_output = os.popen(encryptnet_cmd).read()
                encryptnet_name = encryptnet_output.rstrip()
                encryptnet_name_str = str( encryptnet_name)
                test.lst_encryptnet_name.append(encryptnet_name_str)
            encryptnet_ch = test.lst_encryptnet_name
            word = 'encrypted:'
            for en in (encryptnet_ch):
                        if word in en:
                                encryptnet_ch_co = 'Encrypted data exchanged between containers on different nodes on the overlay network'
                                encryptnet_ch_co_st = colored('PASS  ', 'green')
                                test._encryptnet_ch_co.append(encryptnet_ch_co)
                                test._encryptnet_ch_co_st.append(encryptnet_ch_co_st)
                                
                        else:
                                encryptnet_ch_co = 'Encrypt data exchanged between containers on different nodes on the overlay network'
                                encryptnet_ch_co_st = colored('WARN  ', 'red')
                                test._encryptnet_ch_co.append(encryptnet_ch_co)
                                test._encryptnet_ch_co_st.append(encryptnet_ch_co_st)   
            encryptnet_ch_co_f_st = "\n".join(test._encryptnet_ch_co_st)
            encryptnet_ch_co_f = "\n".join(test._encryptnet_ch_co)  
            table_encryptnet = [[encryptnet_ch_co_f_st , encryptnet_ch_output, encryptnet_ch_co_f]]
            table_encryptnet_out = tabulate(table_encryptnet)
            return table_encryptnet_out