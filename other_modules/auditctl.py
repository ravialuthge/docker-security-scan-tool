class Audit(object):
    
    def __init__(test):
        from tmp.audit_filepath import AUDITFILEPATH
        au = "/etc/audit/audit.rules" 
        auf = AUDITFILEPATH
        fi = open(au, "r")
        mystring  = fi.read()

        for item in mystring.split("\n"):
                if auf in item:
                    _item = item
        test._item = _item
    def auditfile_scan(test):
        test._item = test._item       
        return test._item
