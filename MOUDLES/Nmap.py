import subprocess 
def Nmap_Host_Scan():
    IP = input("Write an Target")
    Arguments = input("Write The Arguments")
    subprocess.run(f"nmap {Arguments.split()} {IP}", shell= True)
def Nmap_Port_Scan():
    IP = input("Write an Target")
    Ports = input("Write The ports You Want To Scan")
    subprocess.run(f"nmap -p {Ports} {IP}", shell= True)
def Nmap_Full_Ports_Scan():
    IP = input("Write an Target")
    subprocess.run(f"nmap -p- {IP}", shell= True)
