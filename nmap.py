# Scanner

import nmap

scanner = nmap.PortScanner()

print("Welcome to the NMAP scan")
print("_________________________________________________________________________")

# Input ip adress
adresse_ip = input("Enter the ip address :")

print("Your ip address is", adresse_ip)
type(adresse_ip)

# Type of scan
print("""\nChoose your type of scan
      - TCP
      - UDP
      - Other""")

