import docker

class imagesnamelist(object):
    def __init__(test): 
        lst=[]
        client = docker.from_env()
        for image in client.images.list():
                    images_ch_cmd_a_s = image.tags
                    images_ch_cmd_str = str(images_ch_cmd_a_s)
                    bbc = images_ch_cmd_str.replace("[",'')
                    bbcdr = bbc.replace("]",'')
                    lst.append(bbcdr)
        test.lst = lst 
    def images(test):
        test.img_name_lst = test.lst        
        return test.img_name_lst
