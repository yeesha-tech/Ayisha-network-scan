import nmap

scanner = nmap.PortScanner()

target = input("Enter target IP or range (e.g. 192.168.1.1 or 192.168.1.0/24): ")

print("Scanning network... please wait")

scanner.scan(hosts=target, arguments='-sn')

print("\nActive hosts found:")

for host in scanner.all_hosts():
    print(f"Host: {host} ({scanner[host].hostname()})")
