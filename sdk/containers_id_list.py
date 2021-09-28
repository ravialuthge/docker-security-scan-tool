import docker

class containerlist(object):
    def __init__(test): 
        lst=[]
        con_name_lst=[]
        con_img_lst=[]
        client = docker.from_env()
        for container in client.containers.list():
                    container_ch_cmd_a = container.id
                    lst.append(container_ch_cmd_a)
                    container_name_ch_cmd_a = container.name
                    con_name_lst.append( container_name_ch_cmd_a)
                    container_image_list = container.image.tags
                    for ci in container_image_list:
                        con_img_lst.append(ci)
        test.con_name_lst = con_name_lst
        test.lst = lst 
        test.con_img_lst = con_img_lst
                    
    def container_id(test):
        test.lst = test.lst        
        return test.lst
    
    def container_name(test):
        test.con_name_lst = test.con_name_lst        
        return test.con_name_lst
    
    def container_img_name(test):
        test.con_img_lst = test.con_img_lst        
        return test.con_img_lst