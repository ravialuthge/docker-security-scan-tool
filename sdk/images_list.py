import docker

class imageslist(object):
    def __init__(test): 
        lst=[]
        client = docker.from_env()
        for image in client.images.list():
                    images_ch_cmd_a = image.id
                    lst.append(images_ch_cmd_a)
        test.lst = lst 
    def images(test):
        test.lst = test.lst        
        return test.lst