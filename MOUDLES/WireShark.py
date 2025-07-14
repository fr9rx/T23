import subprocess
def Run_WireShark():
    subprocess.run("start-process \"wireshark", shell= True)
