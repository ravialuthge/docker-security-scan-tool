import os
install_version = os.system('docker version --format "{{.Server.Version}}"')
latest_version_cmd = os.system('yum list docker-ce --showduplicates | sort -r | awk "{print $2}" | sed -n 6p')
latest_version_str = str(latest_version_cmd)
latest_version_str_x = latest_version_str.split() 
latest_version = latest_version_str_x[1]
print(latest_version)
print(latest_version_str_x)
print(latest_version_str)
print(latest_version_cmd)
print(install_version)
if install_version == latest_version:
	print ("Docker is up to date")
else:
	print ("Docker not update")
