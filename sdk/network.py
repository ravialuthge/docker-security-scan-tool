import docker

class NetList(object):
    client = docker.from_env()
    def net_bridge():
        netlist_output_lst=[]
        for network in __class__.client.networks.list(filters={'driver' : 'bridge'}):
            if network.name != 'ingress':
                netlist_output = network.name
                netlist_output_lst.append(netlist_output)
        return netlist_output_lst
    
    def net_option():
        netlist_opt=[]
        for network in __class__.client.networks.list(filters={'driver' : 'bridge'}):
            if network.name != 'ingress':
                _netlist_opt = network.attrs['Options']
                __netlist_opt = str(_netlist_opt)
                a__netlist_opt = __netlist_opt.split(",")
                netlist_opt.append(a__netlist_opt)
        return netlist_opt
