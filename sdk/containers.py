import docker

class ContainerList(object):
    client = docker.from_env()
    def container_id():
        con_id_lst=[]
        for container in __class__.client.containers.list():
                    container_ch_cmd_a = container.id
                    con_id_lst.append(container_ch_cmd_a)
        return con_id_lst

    def container_name():
        con_name_lst=[]
    
        for container in __class__.client.containers.list():
                    container_name_ch_cmd_a = container.name
                    con_name_lst.append(container_name_ch_cmd_a)
        
        return con_name_lst

    def container_img_name():
        con_img_lst=[]
    
        for container in __class__.client.containers.list():
                    container_image_list = container.attrs['Config']['Image']
                    con_img_lst.append(container_image_list)

        return con_img_lst
    
    def container_appar():
        _container_appar_list=[]
        for container in __class__.client.containers.list():
            container_appar_list = container.attrs['AppArmorProfile']
            _container_appar_list.append("AppArmorProfile="+container_appar_list)

        return _container_appar_list
        
    def container_secc():
        
        _container_secc_list=[]
        for container in __class__.client.containers.list():
            __container_secc_list = container.attrs['HostConfig']['SecurityOpt']
            container_secc_list = str(__container_secc_list)
            _container_secc_list.append(container_secc_list)
    
        return _container_secc_list

    def container_hel():
        
        _container_hel_list=[]
        for container in __class__.client.containers.list():
            try:
                container_hel_list = container.attrs['Config']['Healthcheck']['Test']
                _container_hel_list.append(container_hel_list)
            except KeyError:
                _container_hel_list.append("<nil>")
    
        return _container_hel_list