import docker

class containerimagelist(object):
    def __init__(test):
        con_img_lst=[]
        client = docker.from_env()
        for container in client.containers.list():
                    container_image_list = container.image.tags
                    for ci in container_image_list:
                        con_img_lst.append(ci)
        test.con_img_lst = con_img_lst
    def container_img(test):
        test.con_img_lst = test.con_img_lst
        return test.con_img_lst