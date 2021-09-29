import docker

class dockerversion(object):
    def __init__(test):
        client = docker.from_env()
        _dae = client.info()
        dae = str(_dae)
        vv =  dae.split(",")
        test.lst_version = vv
    
    def docker_version(test):
        test.lst_version = test.lst_version
        return test.lst_version