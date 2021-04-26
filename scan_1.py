import os
import subprocess

root_dir_ch_cmd = "df -h | grep $(docker info -f '{{ .DockerRootDir }}') | awk '{print $6}'"
root_dir_output = subprocess.check_output(["docker", "info" , "--format" , "'{{.DockerRootDir}}'"])
root_dir_x = root_dir_output.decode("utf-8")
root_dir = root_dir_x.replace("'",'')
root_dir_ch_output = os.popen(root_dir_ch_cmd).read()
root_dir_ch = root_dir_ch_output.rstrip()

if root_dir == root_dir_ch:
	print ("crated separate partition for docker root directory")
else:
    print ("not crated separate partition for docker root directory")
