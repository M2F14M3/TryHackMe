# Libraries import.
from scapy.all import ARP, Ether, srp

# Variables declaration.
# Change from "IP/Subnet" to your actual IP/Subnet (for example like: 192.168.0.1/24).
target_ip = "IP/Subnet"
# Creation of the ARP packet
arp = ARP(pdst = target_ip)
ether = Ether(dst = "ff:ff:ff:ff:ff:ff")
clients = []

# Creation of the packet
packet = ether / arp
result = srp(packet, timeout=3, verbose=0)[0]

for sent, received in result:
	clients.append({'ip': received.psrc, 'mac': received.hwsrc})

print("Detected Clients : ")
print("IP" + " " * 18 + "MAC")
for client in clients:
	print("{:16}    {}" . format(client['ip'], client['mac']))