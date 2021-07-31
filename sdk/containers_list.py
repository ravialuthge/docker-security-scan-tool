import docker

class containerlist(object):
    def __init__(self): 
        lst=[]
        client = docker.from_env()
        for container in client.containers.list():
                    container_ch_cmd_a = container.id
                    lst.append(container_ch_cmd_a)
        self.lst = lst 
    def container(self):
        self.lst = self.lst        
        return self.lst