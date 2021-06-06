import os
import subprocess
import re
from termcolor import colored

class dockeruserscan:
    def scan(test):
        trusted_users_cmd = "cat /etc/group | grep docker"
        health_ch_output_output = os.popen(trusted_users_cmd).read()
        trusted_users_cmd_str = re.split(':',health_ch_output_output)
        trusted_users_output_a = trusted_users_cmd_str[3]
        trusted_users_output = "user=" + trusted_users_output_a

        if trusted_users_output == "user=":
            print (colored('PASS   ', 'green') + "allowed trusted users to control Docker daemon")
        else:
            print (colored('WARN   ', 'red') + "Only allow trusted users to control Docker daemon")
