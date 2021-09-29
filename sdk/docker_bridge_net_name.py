import docker

class netlist(object):
    def __init__(test):
        netlist_output_lst=[]
        netlist_opt=[]
        client = docker.from_env()
        for network in client.networks.list(filters={'driver' : 'bridge'}):
            if network.name != 'ingress':
                netlist_output = network.name
                netlist_output_lst.append(netlist_output)
                _netlist_opt = network.attrs['Options']
                __netlist_opt = str(_netlist_opt)
                a__netlist_opt = __netlist_opt.split(",")
                netlist_opt.append(a__netlist_opt)
        test.netlist_output_lst = netlist_output_lst
        test.netlist_opt = netlist_opt
    def net(test):
        test.netlist_output_lst = test.netlist_output_lst
        return test.netlist_output_lst
    def net_opt(test):
        test.netlist_opt = test.netlist_opt
        return test.netlist_opt