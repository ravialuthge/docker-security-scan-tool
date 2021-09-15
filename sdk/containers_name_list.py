import docker

class containerlist(object):
    def __init__(test):
        lst=[]
        client = docker.from_env()
        for container in client.containers.list():
                    container_ch_cmd_a = container.name
                    lst.append(container_ch_cmd_a)
        test.lst = lst
    def container(test):
        test.lst = test.lst
        return test.lst