import docker

class dockerinfo(object):
    def __init__(test):
        client = docker.from_env()
        _dae = client.info()
        dae = str(_dae)
        dir =  dae.split(",")
        test.lst_dir = dir
        _ver = client.version(api_version=True)
        dae = str(_ver)
        _vv =  dae.split(",")
        test.lst_ver = _vv
    
    def docker_dir(test):
        test.lst_dir = test.lst_dir
        return test.lst_dir
    
    def docker_version(test):
        test.lst_ver = test.lst_ver
        return test.lst_ver