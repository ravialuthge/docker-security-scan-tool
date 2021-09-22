#Profile host
#CIS_Version 1.0.0:1.6

import grp
from termcolor import colored

class dockeruser(object):
    """Only allow trusted users to control Docker daemon"""
    def __init__(test):
        test._trusted_users_output=[]
    def dockeruserscan_scan(test):
        groups = grp.getgrall()
        for group in groups:
            for user in group[3]:
                if group[0] == "docker" and user != "root":
                    test._trusted_users_output.append(user)
        trusted_users_output = str(test._trusted_users_output)
        if trusted_users_output == "[]":
            dockeruserscan =  colored('PASS   ', 'green') + "allowed trusted users to control Docker daemon"
        else:
            dockeruserscan =  colored('WARN   ', 'red') + "Only allow trusted users to control Docker daemon"
        return dockeruserscan