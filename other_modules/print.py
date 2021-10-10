from tabulate import tabulate
from sdk.containers import *
from sdk.host import *
from sdk.network import *
from sdk.images import *
from .severity import *
import os
import psutil
import grp

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
    
    def container_contenttrust_print(contenttrust_value,contenttrust_env):
        contenttrust_cmd = contenttrust_value
        contenttrust_version_cmd = os.environ.get(contenttrust_env)
        contenttrust_output = contenttrust_version_cmd

        if contenttrust_output == contenttrust_cmd:
            contenttrust_re = Serverity.pas() + "Enabled Content trust for Docker"
        else:
            contenttrust_re = Serverity.wan() + "Enable Content trust for Docker"
        return contenttrust_re
    
    def container_datadir_print():
        mountdir=[]
        word = " 'DockerRootDir':"
        vv = GetHost.docker_dir()
        for h in vv:
            if word in h:
              _h = h.split(":")
              _root_dir  = _h[1]
              bbc = _root_dir.replace(" '",'')
              root_dir_ch_output = bbc.replace("'",'')
        partitions = psutil.disk_partitions()
        for p in partitions:
             if (p.mountpoint) == root_dir_ch_output:
                 mountdir.append(p.mountpoint)
        _root_dir = str(mountdir)
        bbc = _root_dir.replace("[",'')
        bbcdr = bbc.replace("]",'')
        root_dir = bbcdr.replace("'",'')
        if root_dir_ch_output == root_dir:
            datadir_output =  Serverity.pas() + "crated separate partition for docker root directory"
        else:
            datadir_output = Serverity.wan() + "not crated separate partition for docker root directory"
        return datadir_output
    
    def container_defaultbridge_print():
            _defaultbridge_ch_co=[]
            _defaultbridge_ch_co_st=[]
            _netlist_output_lst = NetList.net_bridge()
            defaultbridge_ch_output = "\n".join(_netlist_output_lst)

            defaultbridge_ch = NetList.net_option()
            word = "{'com.docker.network.bridge.enable_icc': 'false'"
            for en in (defaultbridge_ch):
                        if word in en:
                                defaultbridge_ch_co = 'Network traffic is restricted between containers on the default bridge'
                                defaultbridge_ch_co_st = Serverity.pas()
                                _defaultbridge_ch_co.append(defaultbridge_ch_co)
                                _defaultbridge_ch_co_st.append(defaultbridge_ch_co_st)
                                
                        else:
                                defaultbridge_ch_co = 'network traffic is not restricted between containers on the default bridge'
                                defaultbridge_ch_co_st = Serverity.wan()
                                _defaultbridge_ch_co.append(defaultbridge_ch_co)
                                _defaultbridge_ch_co_st.append(defaultbridge_ch_co_st)   
            defaultbridge_ch_co_f_st = "\n".join(_defaultbridge_ch_co_st)
            defaultbridge_ch_co_f = "\n".join(_defaultbridge_ch_co)  
            table_defaultbridge = [[defaultbridge_ch_co_f_st , defaultbridge_ch_output, defaultbridge_ch_co_f]]
            table_defaultbridge_out = tabulate(table_defaultbridge)
            return table_defaultbridge_out
        
    def container_defaultbridge_print():
        _trusted_users_output=[]
        groups = grp.getgrall()
        for group in groups:
            for user in group[3]:
                if group[0] == "docker" and user != "root":
                    _trusted_users_output.append(user)
        trusted_users_output = str(_trusted_users_output)
        if trusted_users_output == "[]":
            dockeruserscan =  Serverity.pas() + "allowed trusted users to control Docker daemon"
        else:
            dockeruserscan =  Serverity.wan() + "Only allow trusted users to control Docker daemon"
        return dockeruserscan
    
    def container_dockerversion_print(_latest_version):
        a_h=[]
        vv = GetHost.docker_version()
        word = " 'Version':"
        for h in vv:
          if word in h:
            a_h.append(h)
        __h = a_h[0]
        _h = __h.split(":")
        _install_version  = _h[1]
        bbc =  _install_version.replace(" '",'')
        install_version = bbc.replace("'",'')
        latest_version = _latest_version
        if install_version == latest_version:
            docker_version_re = Serverity.pas() + "Docker is up to date"
        elif install_version != latest_version:
            docker_version_re = Serverity.info() + "Docker not update"
        else:
            docker_version_re = "docker: command not found... please install Docker"
        return docker_version_re
    
    def container_encryptnet_print():
        _encryptnet_ch_co=[]
        _encryptnet_ch_co_st=[]
        _netlist_output_lst = NetList.net_overlay()
        encryptnet_ch_output = "\n".join(_netlist_output_lst)

        encryptnet_ch = NetList.net_overlay_option()
        word = " 'encrypted': ''}"
        for en in (encryptnet_ch):
                    if word in en:
                            encryptnet_ch_co = 'Encrypted data exchanged between containers on different nodes on the overlay network'
                            encryptnet_ch_co_st = Serverity.pas()
                            _encryptnet_ch_co.append(encryptnet_ch_co)
                            _encryptnet_ch_co_st.append(encryptnet_ch_co_st)
                            
                    else:
                            encryptnet_ch_co = 'Encrypt data exchanged between containers on different nodes on the overlay network'
                            encryptnet_ch_co_st = Serverity.wan()
                            _encryptnet_ch_co.append(encryptnet_ch_co)
                            _encryptnet_ch_co_st.append(encryptnet_ch_co_st)   
        encryptnet_ch_co_f_st = "\n".join(_encryptnet_ch_co_st)
        encryptnet_ch_co_f = "\n".join(_encryptnet_ch_co)  
        table_encryptnet = [[encryptnet_ch_co_f_st , encryptnet_ch_output, encryptnet_ch_co_f]]
        table_encryptnet_out = tabulate(table_encryptnet)
        return table_encryptnet_out
    
    def container_healthcheck_print():
        lst_health_ch_co=[]
        lst_health_ch_co_st=[]
        lst = ContainerList.container_id()
        lst_str =  str(lst)
        if lst_str == '[]':
            table_he_output = 'containers not running'
        else:
            
            lst_con_img_name = ContainerList.container_img_name()
            lst_con_img_a = "\n".join(lst_con_img_name)
            container_image_output = lst_con_img_a
            _container_name_output = ContainerList.container_name()
            container_name_output = "\n".join(_container_name_output)
            health_ch = ContainerList.container_hel()

            for h in (health_ch):
                    if h == '<nil>':
                            health_ch_co = 'not added health check instructions'
                            health_ch_co_st = Serverity.wan()
                            lst_health_ch_co.append(health_ch_co)
                            lst_health_ch_co_st.append(health_ch_co_st)
                    else:
                            health_ch_co = 'added health check instructions'
                            health_ch_co_st = Serverity.pas()
                            lst_health_ch_co.append(health_ch_co)
                            lst_health_ch_co_st.append(health_ch_co_st)
            health_ch_co_f = "\n".join(lst_health_ch_co)
            health_ch_co_f_st = "\n".join(lst_health_ch_co_st)
            table_he = [[health_ch_co_f_st , container_image_output , container_name_output , health_ch_co_f]]
            table_he_output = tabulate(table_he)
        return table_he_output
    
    def container_imageuser_print():
        lst_imageuser_output_cmd=[]
        lst_img_user_co_st=[]
        lst_str =  ImagesList.images_id()
        _img_name = ImagesList.images_name()
        img_name = "\n".join(_img_name)
        if lst_str == '[]':
            imageuser_output = 'image not found'
        else:
        
            image_user_str_a_s = ImagesList.images_user()
            for i in (image_user_str_a_s):
                if i == 'User=' or i == 'User=root':
                        imageuser_output_cmd = 'not user for the container has been created'
                        img_user_co_st = Serverity.wan()
                        lst_imageuser_output_cmd.append(imageuser_output_cmd)
                        lst_img_user_co_st.append(img_user_co_st)
                else:
                        imageuser_output_cmd = 'user for the container has been created'
                        img_user_co_st = Serverity.pas()
                        lst_imageuser_output_cmd.append(imageuser_output_cmd)
                        lst_img_user_co_st.append(img_user_co_st)
            f_user = "\n".join(lst_imageuser_output_cmd)
            f_st_user = "\n".join(lst_img_user_co_st)
            img_user_co_f = f_user
            img_user_co_f_st = f_st_user
            table_img_user = [[img_user_co_f_st , img_name , img_user_co_f]]
            imageuser_output = tabulate(table_img_user)
        return imageuser_output



