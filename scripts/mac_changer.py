#!/usr/bin/env python 



import subprocess
import argparse
import re 

def get_arguments():
    """Take input from user

    Returns:
        _type_: options (interface and new mac address entered by the user
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--interface", dest="interface", help="Interface to change its MAC address")
    parser.add_argument("-m", "--mac", dest="new_mac_address", help="New MAC Address")
    options = parser.parse_args()
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

# (\w{2}:){5}\w{2})
# \w{2}:\w{2}:\w{2}:\w{2}:\w{2}:\w{2}
def get_current_mac(interface):
    try:
        ifconfig_result = subprocess.check_output(["ifconfig", interface],encoding='utf-8')
        mac_address_search_result = re.search(r"(?P<mac_address>(\w{2}:){5}\w{2})", ifconfig_result)
        if mac_address_search_result:
            return mac_address_search_result.group("mac_address")
    except subprocess.CalledProcessError:
        print(f"Could not execute ifconfig for {interface}")
    print("Could not read MAC address.")


def main():
    options = get_arguments()
    current_mac_address = get_current_mac(options.interface)
    print(f"current_mac_address before changing: {current_mac_address}")
    change_mac(options.interface, options.new_mac_address)
    # Update the current_mac_address
    current_mac_address = get_current_mac(options.interface)
    print(f"current_mac_address after changing : {current_mac_address}")
    if current_mac_address == options.new_mac_address:
        print(f"Mac address was successfully changed to {current_mac_address}")
    else:
        print(f"Mac address did not get changed.")
        
if __name__ == "__main__":
    main()

"""
subprocess 
The subprocess module allows you to spawn new processes, connect to their input/output/error pipes, 
and obtain their return codes. This module intends to replace several older modules and functions

argparse - https://docs.python.org/3/library/argparse.html#module-argparse
The argparse module makes it easy to write user-friendly command-line interfaces. The program defines what arguments it requires, and argparse will figure out how to parse those out of sys.argv. The argparse module also automatically generates help and usage messages. The module will also issue errors when users give the program invalid arguments.

MAC address
- A MAC address (short for medium access control address) is a unique identifier assigned to a network interface controller (NIC) for use as a network address in communications within a network segment. 
- The 12-digit alphanumeric identifier comprises 48 bits, with the initial 24 bits allocated for the OUI (Organization Unique Identifier), while the remaining 24 bits are designated for NIC/vendor-specific data.
- It operates on the OSI models data link layer.
- It is supplied by the devices manufacturer and included in its NIC, which is ideally fixed and cannot be modified.
- https://www.securew2.com/blog/how-do-mac-spoofing-attacks-work


Check if MAC address was changed
- execute and read ifconfig
- read the macaddress from output
- check if mac in ifconfig is what the user requested
- print appropriate message

hw = hwardware, used to specify the hardware class of the interface.
In below code, hw followed by ether, which indicates that the hardware class being specified is Ethernet.
shell=True should not be used since it is a risk for shell injection attacks.

- Shell injection attack - is a type of security vulnerability that occurs when an attacker is able to execute arbitrary commands on a host OS through vulnerable application.
- This can happen when an application passes unsanitized input to the sheel or command interpreter.
- if we were to use shell=True, if an attacker sets 'new_mac_address' to '00:11:22:33:44:55; rm -rf /'
- The above command will change MAC address but also executes the rm -rf / - which would potentially delete all files on the root filesystem, causing significant damange to the system.

- Therefore, to mitigate this risk, it is recommended to use 'subprocess.call' with a list of arguments. This approach is to avoid the need for shell interpretation of the command, thus preventing shell injection attacks.
# このトピックについて新しいことを学びました!
"""