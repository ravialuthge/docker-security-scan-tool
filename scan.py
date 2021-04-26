import os
install_version = os.popen('docker version --format "{{.Server.Version}}"')
latest_version_str = os.popen('yum list docker-ce  | sort -r | awk "{print $2}" | sed -n 6p')
latest_version_str_x = latest_version_str.split(':','-') 
latest_version = latest_version_str_x[1]
if install_version == latest_version:
	print ("Docker is up to date")
else:
	print ("Docker not update")
