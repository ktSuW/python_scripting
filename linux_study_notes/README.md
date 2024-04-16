# Linux Notes


## Notes

<details>
  <summary> Week-1-Intro</summary>

## Tue 16 April

- Windows vs Linux
    - Windows 
        - Windows server 
        - Web server IIS - 30% GUI
        - .exe file (executable files), MSI, affected by malware easily - program or installer. 

    - Linux 
        - TUI - text user interface
        - .rpm -> redhat package manager, Red hat, Fedora, CentOS, rpm is used to distribute and install software on linux systems, it provides a standward way of packaging software and managing its dependencies with the operating system, ensuring that all necessary components are installed
- Types of OS
    - Single user - single tasking - original MS-DOS (Microsoft Disk Operating System) 
    - Single user - multi-tasking - Windows, macOS - clients
    - Multi user - multitasking - Linux, unix

- Client - Server 
    - Client - software app or computer that accesses a service made available by a server
        - request services, depend on the servers to host the services/resoures they need
    - Server - computer/system that provides resources, data services, or programs to other computers, known as computers(clients) over network
        - provide services
        - resource management
- Ports
    - 1 - 1023  - well known ports used by system-level or root processes or by programs executed by priviledged users 
    - Port 21 - File transfer protocol
    - Port 22 - SSH - secure shell for secure remote logins and file transfers
    - Port 25 - SMTP for email transmissions
    - Port 443 - HTTPS
    - 1024 - 65535 => open ports

- RHEL 
    - In a Linux environment like Red Hat Enterprise Linux (RHEL), installing and configuring specific server software allows the system to function as that type of server.
    - installing a DNS server involves setting up the BIND (Berkeley Internet Name Domain) software package, which is the most widely used DNS software on the Internet and commonly used on Linux systems. If you install BIND on a RHEL server, it can indeed function as a DNS server.
    - sudo dnf install bind bind-utils
    - The main configuration file for BIND is /etc/named.conf.
    - Define zones and zone files in the configuration to specify how DNS requests should be handled and responded to.
    - Zone files are stored in /var/named by default. These files contain DNS records for the domains that your server is authoritative for, such as SOA records, A records, MX records, etc.
    - sudo systemctl enable named
    - sudo systemctl start named
    - sudo firewall-cmd --add-service=dns --permanent
    - sudo firewall-cmd --reload
    - dig @localhost example.com

- DHCP server setup
    - install the dhcp package and configure it to allocate IP addresses to client machines within the network.
    - sudo dnf install dhcp




## Wed 17 April 

- systemd
- journald



- Networking, https://www.youtube.com/playlist?list=PL7zRJGi6nMRzg0LdsR7F3olyLGoBcIvvg

</details>

