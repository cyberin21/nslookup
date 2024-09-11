import socket
import os

dns = input("Enter the domain name only: ")
ip = socket.gethostbyname(dns)
print(f"DNS: {dns}")
print(f"IP: {ip}")