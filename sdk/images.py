import docker

class ImagesList(object):
    client = docker.from_env()
    def images_id():
        lst=[]
        for image in __class__.client.images.list():
                    images_ch_cmd_a = image.id
                    x = images_ch_cmd_a.split(":")
                    ff = x[1]
                    lst.append(ff)
        return lst
        
    def images_name():
        lst_img_name=[]
        for image in __class__.client.images.list():
            images_ch_cmd_a_s = image.tags
            images_ch_cmd_str = str(images_ch_cmd_a_s)
            bbc = images_ch_cmd_str.replace("[",'')
            bbcdr = bbc.replace("]",'')
            bbcf = bbcdr.replace("'",'')
            lst_img_name.append(bbcf)
        return lst_img_name

    def images_user():
        _lst_img_user=[]
        for image in __class__.client.images.list():
            lst_img_user = image.attrs['Config']['User']
            _lst_img_user.append("User="+lst_img_user)
        return _lst_img_user

    def images_off(img_name):
        images_off = __class__.client.images.search(img_name)
        __images_off = str(images_off)
        a__images_off_ch =  __images_off.split(",")    
        return a__images_off_ch

    def images_update():
        _images_ch_cmd_a=[]
        for image in __class__.client.images.list():
            a__images_ch_cmd_a = image.history()
            __images_ch_cmd_a = str(a__images_ch_cmd_a)
            _images_ch_cmd_a.append(__images_ch_cmd_a)
        return _images_ch_cmd_a
