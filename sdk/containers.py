import docker

class containerlist:
    def container(container_ch_cmd_a):
        client = docker.from_env()
        for container in client.containers.list():
                    container_ch_cmd_a = container.id
                    return container_ch_cmd_a