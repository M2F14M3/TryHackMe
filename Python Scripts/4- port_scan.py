# Libraries import.
import sys
import socket
import pyfiglet

# Variables declaration.
ascii_banner = pyfiglet.figlet_format("TryHackMe\n Python 4 Pentesters\n Port Scanner")
# Change from "Target_IP" to your actual target IP (for example 192.168.0.1).
ip = "Target_IP"
open_ports = []
# Range for all the possible ports
ports = range(1, 65535)

print(ascii_banner)

# Creation of the function to test for open ports on the target IP
def probe_port(ip, port, result = 1):
	try:
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.settimeout(0.5)
		r = sock.connect_ex((ip, port))
		if r == 0:
			result = r
			sock.close()
	except Exception as e:
		pass
	return result

for port in ports:
	sys.stdout.flush()
	response = probe_port(ip, port)
	if response == 0:
		open_ports.append(port)

if open_ports:
	print ("Open Ports are: ")
	print (sorted(open_ports))
else:
	print ("Looks like no ports are open :(")