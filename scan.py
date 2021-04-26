import os
install_version = os.popen('docker version --format "{{.Server.Version}}"')
current_version = '20.10.6'
if install_version == current_version:
	print ("Docker is up to date")
else:
	print ("Docker not update")
