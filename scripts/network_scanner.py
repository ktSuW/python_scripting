#!/usr/bin/env python 
"""
Network Scanner
- discover all devices on the network
- display their IP address
- display MAC addresses

- nmap
- https://nmap.org/
- Nmap ("Network Mapper") is a free and open source utility for network discovery and security auditing. Many systems and network administrators also find it useful for tasks such as network inventory, managing service upgrade schedules, and monitoring host or service uptime. Nmap uses raw IP packets in novel ways to determine what hosts are available on the network, what services (application name and version) those hosts are offering, what operating systems (and OS versions) they are running, what type of packet filters/firewalls are in use, and dozens of other characteristics.

- Another tool is netdiscover - built in in kali linux
- To run this command, you must have root priviledges or 
sudo netdiscover -r 1.2.3.4/24

- ARP protocol - link IP address to Mac address
- ARP request - broadcast - send 
- ARP response - I have 10.0.02.6 and my MAC address is 00:11:22:33:44:55

- What is Scapy, https://scapy.readthedocs.io/en/latest/introduction.html
- arping() - The fastest way to discover hosts on a local ethernet network is to use the ARP Ping method
- Scapy is a Python program that enables the user to send, sniff, dissect and forge network packets. 
- This capability allows construction of tools that can probe, scan or attack networks.

route -n 
- single IP sending 1 packet => "10.0.2.1"
- Multiple IP sending 256 packet => "10.0.2.1/24" - 24 subnetmask
- ARP poisioning 

Network scanner algorithm
- create  arp reuest directed to broadcast MAC asking for IP
    - Use ARP to ask who has specific IP
    - Set destination MAC to broadcast MAC
- send packet and receive response
- parse the response
- print the result


hwtype     : XShortEnumField                     = 1               ('1')
ptype      : XShortEnumField                     = 2048            ('2048')
hwlen      : FieldLenField                       = None            ('None')
plen       : FieldLenField                       = None            ('None')
op         : ShortEnumField                      = 1               ('1')
hwsrc      : MultipleTypeField (SourceMACField, StrFixedLenField) = '00:0c:22:3c:f7:e8' ('None')
psrc       : MultipleTypeField (SourceIPField, SourceIP6Field, StrFixedLenField) = '192.168.0.50'  ('None')
hwdst      : MultipleTypeField (MACField, StrFixedLenField) = '00:00:00:00:00:00' ('None')
pdst       : MultipleTypeField (IPField, IP6Field, StrFixedLenField) = '0.0.0.0'       ('None')

hwtype: Hardware Type - This field specifies the type of hardware used for the network, for example, Ethernet. The value '1' typically represents Ethernet.

ptype: Protocol Type - This field specifies the type of protocol used for the network. The value '2048' represents IPv4.

hwlen: Hardware Length - This field specifies the length of the hardware address. In the case of Ethernet, this is usually 6 bytes.

plen: Protocol Length - This field specifies the length of the protocol address. For IPv4, this is usually 4 bytes.

op: Operation - This field specifies the operation that the ARP packet is performing. The value '1' typically represents an ARP request, while '2' represents an ARP reply.

hwsrc: Hardware Source - This field contains the MAC address of the sender (source) of the packet.

psrc: Protocol Source - This field contains the IP address of the sender (source) of the packet.

hwdst: Hardware Destination - This field contains the MAC address of the intended recipient (destination) of the packet. In an ARP request, this is usually set to all zeroes.

pdst: Protocol Destination - This field contains the IP address of the intended recipient (destination) of the packet.
"""
import scapy.all as scapy 

def scan_test(ip):
    # scapy.arping(ip)
    # APR object
    arp_request = scapy.ARP(pdst=ip)
    # arp_request.show()
    # Instead of setting separately, you can set like above
    # arp_request.pdst = ip
    # print(arp_request.summary())
    # scapy.ls(scapy.ARP())
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    # broadcast.show()
    # scapy.ls(scapy.Ether())
    # print(broadcast.summary())
    arp_request_broadcast = broadcast/arp_request # Append /
    # print(arp_request_broadcast.summary())
    # arp_request_broadcast.show()
    # Send packets - srp - send and receive packets with custom Ether part
    # They return a couple of two lists
    # answered_list, unanswered_list =  scapy.srp(arp_request_broadcast, timeout=1)
    answered_list =  scapy.srp(arp_request_broadcast, timeout=1, verbose = False)[0]
    # print(answered_list.summary())
    # print(unanswered_list.summary())
    print("IP\t\t\tAT MAC Address\n-------------------------------------------------------")
    for element in answered_list:
        print(element[1].psrc + "\t\t", element[1].hwsrc)

# list index and dictionary key to access mac and ip addresses respectively
def scan_create(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
    
    clients_list = []
    for element in answered_list:
        clients_ip_mac_dic = {"ip" : element[1].psrc, "mac" : element[1].hwsrc}
        clients_list.append(clients_ip_mac_dic)
    return clients_list

def print_ip_mac_addresses_result(clients_list):
    print("IP\t\t\tMAC Address\n--------------------------------------")
    for client in clients_list:
       print(client["ip"] , "\t\t", client["mac"])
    
def main():
    clients_list = scan_create("192.168.0.1/24")
    print_ip_mac_addresses_result(clients_list)
        
if __name__ == "__main__":
    main()
