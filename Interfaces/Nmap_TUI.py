def Run_Nmap():
    print("========================================")
    print("[1] Nmap Host Scan                      ")
    print("[2] Nmap Spesfic Ports Scan             ")
    print("[3] Nmap Full Ports Scan                ")
    print("[0] Exit                                ")
    print("========================================")
    from MOUDLES import Nmap_Full_Ports_Scan, Nmap_Host_Scan, Nmap_Port_Scan
    from Interfaces import Menu
    import msvcrt
    key = msvcrt.getch()
    match key:
        case "1":
            Nmap_Host_Scan()
        case "2":
            Nmap_Port_Scan()
        case "3":
            Nmap_Full_Ports_Scan()
        case "0":
            Menu()
        case _:
            print("Error Write a Number From 1 To 3")