import docker

class ContainerList(object):
    def __init__(test): 
        lst=[]
        con_name_lst=[]
        con_img_lst=[]
        _container_appar_list=[]
        _container_secc_list=[]
        _container_hel_list=[]
        client = docker.from_env()
        for container in client.containers.list():
                    container_ch_cmd_a = container.id
                    lst.append(container_ch_cmd_a)
                    container_name_ch_cmd_a = container.name
                    con_name_lst.append( container_name_ch_cmd_a)
                    container_image_list = container.attrs['Config']['Image']
                    con_img_lst.append(container_image_list)
                    container_appar_list = container.attrs['AppArmorProfile']
                    _container_appar_list.append("AppArmorProfile="+container_appar_list)
                    __container_secc_list = container.attrs['HostConfig']['SecurityOpt']
                    container_secc_list = str(__container_secc_list)
                    _container_secc_list.append(container_secc_list)
                    try:
                     container_hel_list = container.attrs['Config']['Healthcheck']['Test']
                     _container_hel_list.append(container_hel_list)
                    except KeyError:
                     _container_hel_list.append("<nil>")
        test.con_name_lst = con_name_lst
        test.lst = lst 
        test.con_img_lst = con_img_lst
        test._container_appar_list = _container_appar_list
        test._container_secc_list = _container_secc_list
        test._container_hel_list = _container_hel_list
                    
    def container_id(test):
        test.lst = test.lst        
        return test.lst
    
    def container_name(test):
        test.con_name_lst = test.con_name_lst        
        return test.con_name_lst
    
    def container_img_name(test):
        test.con_img_lst = test.con_img_lst        
        return test.con_img_lst
    
    def container_appar(test):
        test._container_appar_list = test._container_appar_list        
        return test._container_appar_list

    def container_secc(test):
        test._container_secc_list = test._container_secc_list        
        return test._container_secc_list
    
    def container_hel(test):
        test._container_hel_list = test._container_hel_list        
        return test._container_hel_list