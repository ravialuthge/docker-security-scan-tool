import os
import re
from termcolor import colored

class userland:
	def scan(test):
	    userland_cmd = "ps -ef | grep dockerd | grep userland-proxy"
	    userland_output = os.popen(userland_cmd).read()

	    if userland_output == '':
		    userland_re = colored('WARN   ', 'red') + "Disable Userland Proxy"
	    else:
		    userland_re = colored('PASS   ', 'green') + "Userland Proxy disabled"
	    print (userland_re)