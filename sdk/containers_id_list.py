import docker

class containerlist(object):
    def __init__(test): 
        lst=[]
        con_name_lst=[]
        client = docker.from_env()
        for container in client.containers.list():
                    container_ch_cmd_a = container.id
                    lst.append(container_ch_cmd_a)
                    container_name_ch_cmd_a = container.name
                    con_name_lst.append( container_name_ch_cmd_a)
        test.con_name_lst = con_name_lst
        test.lst = lst 
                    
    def container_id(test):
        test.lst = test.lst        
        return test.lst
    
    def container_name(test):
        test.con_name_lst = test.con_name_lst        
        return test.con_name_lst