class Audit(object):
    
    def __init__(test):
        _auditcontainerd_cmd = "/usr/bin/docker-containerd" 
        _au = "/etc/audit/audit.rules"
        _auditcontainerd_output=[]
        _fi = open(_au, "r")
        _mystring  = _fi.read()
        for it in _mystring.split("\n"):
            if _auditcontainerd_cmd in it:
                _auditcontainerd_output.append(it)
        test._auditcontainerd_output = _auditcontainerd_output		  
    def auditfile_scan(test):
        test._auditcontainerd_output = test._auditcontainerd_output      
        return test._auditcontainerd_output
