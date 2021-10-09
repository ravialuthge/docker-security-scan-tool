from tabulate import tabulate
from sdk.containers import *
from sdk.host import *
from .severity import *

class Print(object):

    def container_appar_print():
        lst_apparmor_co=[]
        lst_apparmor_co_st=[]
        con_id_lst = ContainerList.container_id()
        _con_id_lst = str(con_id_lst)
        lst_con_img_name = ContainerList.container_img_name()
        lst_con_img_a = "\n".join(lst_con_img_name)
        images_output = lst_con_img_a 
        apparmor_profile_str_a_s = ContainerList.container_appar()
        if _con_id_lst == '[]':
            apparmor_output = 'containers not running'

        else: 
            for i in (apparmor_profile_str_a_s):
                    if i == 'AppArmorProfile=':
                            apparmor_co = 'Verify AppArmor Profile, if applicable'
                            apparmor_co_st = Serverity.wan()
                            lst_apparmor_co.append(apparmor_co)
                            lst_apparmor_co_st.append(apparmor_co_st)
                    else:
                            apparmor_co = 'AppArmor Profile available'
                            apparmor_co_st = Serverity.pas()
                            lst_apparmor_co.append(apparmor_co)                      
                            lst_apparmor_co_st.append(apparmor_co_st)
            f_app = "\n".join(lst_apparmor_co)
            f_st_app = "\n".join(lst_apparmor_co_st)
            apparmor_co_f = f_app
            apparmor_co_f_st = f_st_app
            table_apparmor = [[apparmor_co_f_st , images_output , apparmor_co_f]]
            apparmor_output = tabulate(table_apparmor)
        return apparmor_output
    
    def container_audit_print(auditcontainerd_path):
        _auditcontainerd_cmd = auditcontainerd_path
        _au = "/etc/audit/audit.rules"
        _auditcontainerd_output=[]
        _fi = open(_au, "r")
        _mystring  = _fi.read()
        for it in _mystring.split("\n"):
            if _auditcontainerd_cmd in it:
                _auditcontainerd_output.append(it)
        _auditcontainerd_output = _auditcontainerd_output
        auditcontainerd_output = str(_auditcontainerd_output)
        if auditcontainerd_output == "[]":
            auditcontainerd_re = Serverity.wan() + "Add a rule for /usr/bin/docker-containerd file"
        else:
            auditcontainerd_re = Serverity.pas() + "Audit Docker files and directories"
        return auditcontainerd_re	

    def container_cgroup_print():
        word = " 'CgroupDriver':"
        vv = GetHost.docker_dir()
        for h in vv:
            if word in h:
              _h = h.split(":")
              _cgroup_output  = _h[1]
              bbc = _cgroup_output.replace(" '",'')
              cgroup_output = bbc.replace("'",'')
        
        if cgroup_output == "cgroup-parent":
            cgroup_output =  Serverity.pas() + "default cgroup used"
        else:
           cgroup_output = Serverity.wan() + "confirm default cgroup usage"
        return cgroup_output
