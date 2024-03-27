#!/usr/bin/env python 

import subprocess
import optparse

parser = optparse.OptionParser()
parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC address")
parser.parse_args()

interface = input("Interface : ")
new_mac_address = input("Enter new MAC address : ")
# subprocess.call(f"ifconfig {interface} down", shell=True)
# subprocess.call(f"ifconfig {interface} hw ether {new_mac_address}", shell=True)
# subprocess.call(f"ifconfig {interface} up", shell=True)

subprocess.call(["ifconfig", interface, "down"])
subprocess.call(["ifconfig", interface, "hw" , "ether", new_mac_address])
subprocess.call(["ifconfig", interface, "up"])