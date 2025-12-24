#!/usr/bin/env python3
"""
IP Finder - Convert domain name to IP address
"""
import socket

def get_ip(domain):
    try:
        ip = socket.gethostbyname(domain)
        return ip
    except socket.gaierror:
        return "domain isnt valid"
    
site = input("Enter domain (e.g., github.com): ")
ip_address = get_ip(site)
print(f"IP {site}: {ip_address}")
