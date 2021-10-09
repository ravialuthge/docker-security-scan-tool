import docker
from other_modules.severity import *
from other_modules.print import *

class ContainerList(Serverity):
    client = docker.from_env()
    def container_id(test):
        con_id_lst=[]

        for container in __class__.client.containers.list():
                    container_ch_cmd_a = container.id
                    con_id_lst.append(container_ch_cmd_a)
        test.con_id_lst = con_id_lst

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
    
    def container_appar(test):
        _container_appar_list=[]
        lst_apparmor_co=[]
        lst_apparmor_co_st=[]
        for container in __class__.client.containers.list():
            container_appar_list = container.attrs['AppArmorProfile']
            _container_appar_list.append("AppArmorProfile="+container_appar_list)
        apparmor_profile_str_a_s = _container_appar_list
        con_id_lst = test.con_id_lst
        _con_id_lst = str(con_id_lst) 
        if _con_id_lst == '[]':
            apparmor_output = 'containers not running'

        else: 
            for i in (apparmor_profile_str_a_s):
                    if i == 'AppArmorProfile=':
                            apparmor_co = 'Verify AppArmor Profile, if applicable'
                            apparmor_co_st = Serverity.wan()
                            lst_apparmor_co.append(apparmor_co)
                            lst_apparmor_co_st.append(apparmor_co_st)
                    else:
                            apparmor_co = 'AppArmor Profile available'
                            apparmor_co_st = Serverity.pas()
                            lst_apparmor_co.append(apparmor_co)                      
                            lst_apparmor_co_st.append(apparmor_co_st)
        Print().container_appar_print(apparmor_output,lst_apparmor_co,lst_apparmor_co_st)
    
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