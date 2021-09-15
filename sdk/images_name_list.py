import docker

class imagesnamelist(object):
    def __init__(test): 
        lst_img_name=[]
        client = docker.from_env()
        for image in client.images.list():
                    images_ch_cmd_a_s = image.tags
                    images_ch_cmd_str = str(images_ch_cmd_a_s)
                    bbc = images_ch_cmd_str.replace("[",'')
                    bbcdr = bbc.replace("]",'')
                    lst_img_name.append(bbcdr)
        test.lst_img_name = lst_img_name 
    def images(test):
        test.img_name_lst = test.lst_img_name        
        return test.img_name_lst
