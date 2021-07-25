import docker

class containerlist(object):
    def container(self):
        client = docker.from_env()
        for container in client.containers.list():
                    self.container_ch_cmd_a = container.id
                    return self.container_ch_cmd_a