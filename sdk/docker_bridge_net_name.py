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
                netlist_opt.append(_netlist_opt)
        test.netlist_output_lst = sorted(netlist_output_lst)
    def net(test):
        test.netlist_output_lst = test.netlist_output_lst
        return test.netlist_output_lst