import docker

class containerlist:
    def container():
        client = docker.from_env()
        for container in client.containers.list():
                    container_ch_cmd_a = container.id
                    return container_ch_cmd_a