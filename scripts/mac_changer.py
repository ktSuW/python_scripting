#!/usr/bin/env python 

import subprocess
import optparse

def get_arguments():
    """Take input from user

    Returns:
        _type_: options (interface and new mac address entered by the user
    """
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC address")
    parser.add_option("-m", "--mac", dest="new_mac_address", help="New MAC Address")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("[-] Please specify interface. Use --help for more info.")
    elif not options.new_mac_address:
        parser.error("[-] Please specify a new mac. Use --help for more info.")
    return options

def change_mac(interface, new_mac_address):
    print(f"[+] Changing MAC address for {interface} to {new_mac_address}")
    # security risk
    # subprocess.call(f"ifconfig {interface} down", shell=True)
    # subprocess.call(f"ifconfig {interface} hw ether {new_mac_address}", shell=True)
    # subprocess.call(f"ifconfig {interface} up", shell=True)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw" , "ether", new_mac_address])
    subprocess.call(["ifconfig", interface, "up"])
    

options = get_arguments()
change_mac(options.interface, options.new_mac_address)