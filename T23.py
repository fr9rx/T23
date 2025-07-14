from Interfaces import Menu
from Interfaces import Run_Nmap
from MOUDLES import Run_WireShark
from MOUDLES import Run_ping
from MOUDLES import Run_TheHarvester
import msvcrt

while True:
        Menu()
        key = msvcrt.getch().decode()
        match key:
            case "1":
                Run_Nmap()
            case "2":
                Run_WireShark()
            case "3":
                Run_ping()
            case "4":
                Run_TheHarvester()
            case "0":
                exit()
            case _:
                print("Error Write a Number From 1 To 2")
