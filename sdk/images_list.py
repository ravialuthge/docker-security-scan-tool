import docker

class imageslist(object):
    def __init__(test): 
        from tmp.imagename import IMAGENAME
        lst=[]
        lst_img_name=[]
        _lst_img_user=[]
        _images_ch_cmd_a=[]
        client = docker.from_env()
        img_name = IMAGENAME
        images_off = client.images.search(img_name)
        __images_off = str(images_off)
        a__images_off_ch =  __images_off.split(",")
        for image in client.images.list():
                    images_ch_cmd_a = image.id
                    x = images_ch_cmd_a.split(":")
                    ff = x[1]
                    lst.append(ff)
                    images_ch_cmd_a_s = image.tags
                    images_ch_cmd_str = str(images_ch_cmd_a_s)
                    bbc = images_ch_cmd_str.replace("[",'')
                    bbcdr = bbc.replace("]",'')
                    bbcf = bbcdr.replace("'",'')
                    lst_img_name.append(bbcf)
                    lst_img_user = image.attrs['Config']['User']
                    _lst_img_user.append("User="+lst_img_user)
                    a__images_ch_cmd_a = image.history()
                    __images_ch_cmd_a = str(a__images_ch_cmd_a)
                    _images_ch_cmd_a.append(__images_ch_cmd_a)
        test.lst = lst
        test.lst_img_name = lst_img_name
        test._lst_img_user = _lst_img_user
        test.a__images_off_ch = a__images_off_ch
        test._images_ch_cmd_a = _images_ch_cmd_a
    def images_id(test):
        test.lst = test.lst        
        return test.lst
    def images_name(test):
        test.lst_img_name = test.lst_img_name        
        return test.lst_img_name
    def images_user(test):
        test._lst_img_user = test._lst_img_user        
        return test._lst_img_user
    def images_off(test):
        test.a__images_off_ch = test.a__images_off_ch     
        return test.a__images_off_ch
    def images_update(test):
        test._images_ch_cmd_a = test._images_ch_cmd_a    
        return test._images_ch_cmd_a