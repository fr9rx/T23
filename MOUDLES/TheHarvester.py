import subprocess
def Run_TheHarvester():
    Domain = input("Write an Domain:")
    source = input("Write an Engine For Searching:")
    subprocess.run(f"theharvester -d {Domain} -b {source}", shell= True)
    