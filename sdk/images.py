import docker

class imageslist:
    def images():
        client = docker.from_env()
        for image in client.images.list():
                    images_ch_cmd_a = image.id
                    return images_ch_cmd_a