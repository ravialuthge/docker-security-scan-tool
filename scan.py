import os
import subprocess
import re

latest_version_cmd = "yum list docker-ce | sort -r | awk '{print $2}' | sed -n 6p"
install_version_output = subprocess.check_output(["docker", "version" , "--format" , "'{{.Server.Version}}'"])
install_version_x = install_version_output.decode("utf-8")
install_version = install_version_x.replace("'",'')
latest_version_output = os.popen(latest_version_cmd).read()
latest_version_str = latest_version_output.rstrip()
latest_version_str_x = re.split(':|-',latest_version_str)
latest_version = latest_version_str_x[1]

if install_version == latest_version:
	print ("Docker is up to date")
elif install_version != latest_version:
	print ("Docker not update")
else:
    print ("Docker not install")
