import subprocess 
def Run_ping():
    Target = input("Write an Domain or Dns")
    subprocess.run(f"ping {Target}", shell= True)