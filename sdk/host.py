import docker

class GetHost(object):
    client = docker.from_env()
    
    def docker_dir():
        _dae = __class__.client.info()
        dae = str(_dae)
        dir =  dae.split(",")
        return dir
    
    def docker_version():
        _ver = __class__.client.version(api_version=True)
        dae = str(_ver)
        lst_ver =  dae.split(",")
        return lst_ver