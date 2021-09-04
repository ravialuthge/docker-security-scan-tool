import docker

class imageslist(object):
    def __init__(test): 
        lst=[]
        lst_img_name=[]
        client = docker.from_env()
        for image in client.images.list():
                    images_ch_cmd_a = image.id
                    x = images_ch_cmd_a.split(":")
                    ff = x[1]
                    lst.append(ff)
        test.lst = lst
        for image in client.images.list():
                    images_ch_cmd_a_s = image.tags
                    images_ch_cmd_str = str(images_ch_cmd_a_s)
                    lst_img_name.append(images_ch_cmd_str)
        test.lst_img_name = lst_img_name
    def images_id(test):
        test.lst = test.lst        
        return test.lst
    def images_name(test):
        test.lst_img_name = test.lst_img_name        
        return test.lst_img_name