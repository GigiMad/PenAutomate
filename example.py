import nmap
import socket

def get_ip_address(url):
    return socket.gethostbyname(url)

def scan_host(ip):
    scanner = nmap.PortScanner()
    # Le scan OS nécessite des privilèges d'administrateur pour envoyer des paquets ICMP
    scanner.scan(ip, arguments="-O")
    if 'osclass' in scanner[ip]:
        for osclass in scanner[ip]['osclass']:
            print(f"OS Type: {osclass['type']}")
            print(f"Vendor: {osclass['vendor']}")
            print(f"OS Family: {osclass['osfamily']}")
            print(f"OS Generation: {osclass['osgen']}")
    else:
        print("OS information not available.")

if __name__ == "__main__":
    target = input("Enter IP address or URL: ")
    if target.startswith('http://') or target.startswith('https://'):
        target = target.split("//")[1]
    try:
        ip_address = get_ip_address(target)
        print(f"IP Address: {ip_address}")
        scan_host(ip_address)
    except socket.gaierror:
        print("Hostname could not be resolved.")
    except Exception as e:
        print(str(e))
