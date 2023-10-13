#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
from src.lan_scanner import lan_scan
from src.nmap_automation import nmap_script

os.system("clear")
print("""
██████╗ ███╗   ██╗███╗   ███╗ █████╗ ██████╗ 
██╔══██╗████╗  ██║████╗ ████║██╔══██╗██╔══██╗
██████╔╝██╔██╗ ██║██╔████╔██║███████║██████╔╝
██╔═══╝ ██║╚██╗██║██║╚██╔╝██║██╔══██║██╔═══╝ 
██║     ██║ ╚████║██║ ╚═╝ ██║██║  ██║██║     
╚═╝     ╚═╝  ╚═══╝╚═╝     ╚═╝╚═╝  ╚═╝╚═╝     
          Developed by @mkdirlove 
""")

print('-' * 46)
print("[*] ~ 1. Discover all devices on your network.")
print("[*] ~ 2. NMAP Automation tool.")
print('-' * 46)

try:
    USER_INPUT = input("[+] Enter your option: ")
    
    if USER_INPUT == '1':
        lan_scan()
    elif USER_INPUT == '2':
        nmap_script()
except KeyboardInterrupt:
    print("\n\n[*] Exiting...")
