###Profile host#
###CIS_Version 1.1.0:1.1.0#

import os
from termcolor import colored
from tabulate import tabulate
from sdk.docker_bridge_net_name import *

class defaultbridge(netlist):
    """Ensure network traffic is restricted between containers on the default bridge"""
    def __init__(test):
            #test.lst_defaultbridge_name=[]
            test._defaultbridge_ch_co=[]
            test._defaultbridge_ch_co_st=[]

            
    def defaultbridge_scan(test):
            super().__init__()
            _netlist_output_lst = test.netlist_output_lst
            defaultbridge_ch_output = "\n".join(_netlist_output_lst)

            #for d in (_netlist_output_lst):
                
            #    defaultbridge_cmd = "docker network inspect " + d + " --format '{{.Name}} {{.Options}}'"
            #    defaultbridge_output = os.popen(defaultbridge_cmd).read()
            #    defaultbridge_name = defaultbridge_output.rstrip()
            #    defaultbridge_name_str = str(defaultbridge_name)
            #    test.lst_defaultbridge_name.append(defaultbridge_name_str)
            defaultbridge_ch = test.netlist_opt
            word = """'com.docker.network.bridge.enable_icc':", "'true',"""
            for en in (defaultbridge_ch):
                        if word in en:
                                defaultbridge_ch_co = 'Network traffic is restricted between containers on the default bridge'
                                defaultbridge_ch_co_st = colored('PASS  ', 'green')
                                test._defaultbridge_ch_co.append(defaultbridge_ch_co)
                                test._defaultbridge_ch_co_st.append(defaultbridge_ch_co_st)
                                
                        else:
                                defaultbridge_ch_co = 'network traffic is not restricted between containers on the default bridge'
                                defaultbridge_ch_co_st = colored('WARN  ', 'red')
                                test._defaultbridge_ch_co.append(defaultbridge_ch_co)
                                test._defaultbridge_ch_co_st.append(defaultbridge_ch_co_st)   
            defaultbridge_ch_co_f_st = "\n".join(test._defaultbridge_ch_co_st)
            defaultbridge_ch_co_f = "\n".join(test._defaultbridge_ch_co)  
            table_defaultbridge = [[defaultbridge_ch_co_f_st , defaultbridge_ch_output, defaultbridge_ch_co_f]]
            table_defaultbridge_out = tabulate(table_defaultbridge)
            return table_defaultbridge_out