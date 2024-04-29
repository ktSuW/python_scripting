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

- Architectur of unix
  - hardware (Processor ALU - arithmic logical unit) <--> kernel (core component of OS) <--> shell (interpreter - convert to machine language) <--> commands (predefined programs) <--> executed by users
  - RHEL - BASH shell 

- Kernel types
    - monolithic kernel - Linux
    - micro - windows 
- Kernel manages : device info, multitasking info, file system info. 
    - Resource management - Kernel manages and allocates system resources like CPU time, memory, and disk space to various processes running on the computer
    - process management - It handles the creation, execution and termination of processes. Each command you run in Bash, for instance, results in the kernel creating and managing processes
    - device drivers - kernel includes drivers that allow it to work with different hardware devices
    - System calls - 
- Virtulisation
    - Window -> Hyper-V - Hyper-V is Microsoft's hardware virtualization product. It lets you create and run a software version of a computer, called a virtual machine. Each virtual machine acts like a complete computer, running an operating system and programs. Hyper-V runs directly on the hardware, or can be hosted in Windows, making it a Type 1 or Type 2 hypervisor depending on the configuration.
    - Linux - KVM (Kernel based virtual machine)
    - Oracle -> virtual Box
    - VMware -> workstation 

## Thurs 18 April 
- systemd
- journald
- Installation

## Fri 19 April 

- File System Hierarchy 
- <img src="../img/linux_file_system_hierarchy.png">
- <img src="../img/fhs.png">
- Window
    - Mount point - there is no drive letters concept in linux 
    - Window - top level directory \  it means harddisk C:\, D:\
- Linux 
    - Without drive letters, we can identify the device
    - Use mount point
    - forward slash / is a top level directory, parent directory for all other directories
    - users
        - Admin (window) -> root (linux) - home directory for root user
        - Guest (window) -> normal (linux)\
    - / top level dir
    - /root for root user
    - /home for normal user
    - /boot - static files of the boot loader
        - GRUB2 -> RHEL 7.0, 8.0 & 9.0
        - GRUB -> RHEL 6.0
        - LILO -> 5.0, 4.0, 3.0, 2.0
    - /etc contains host specific system configuration files e.g. httpd
    - /bin  contains normal user executable commands 
    - /sbin contains super user executable commands 
    - /usr UNIX resource repositorycontains program file 
    - /opt optional for usr 
    - /var contains - /var is a standard subdirectory of the root directory in Linux and other Unix-like operating systems that contains files to which the system writes data during the course of its operation.
    - /run - real time information, media, 
    - /proc - contains background running processes (background running processes)
        - like Task Manager in window
        - #cat/proc/cpuinfo
        - #cat/proc/meminfo
    - ram, swap
        - dynamic ram
        - swap- virtual ram
    - [Linux Filesystem Hierarchy](https://tldp.org/LDP/Linux-Filesystem-Hierarchy/html/index.html)
     - https://refspecs.linuxfoundation.org/FHS_3.0/fhs/index.html




- Networking, https://www.youtube.com/playlist?list=PL7zRJGi6nMRzg0LdsR7F3olyLGoBcIvvg

</details>

----

<details>
  <summary> Week-2-Intro</summary>

## Mon 22 April 
- /mnt contains empty dir. By default, mnt dir will be created. To create a mount point for any partition
- /lib contains library files. In windows, we have got dll files. Sharable objects
- /sys  contains system related config files. OS related files 
- /srv - /srv directory contains data for servers. If you are running a web server from your Linux box, your HTML files for your sites would go into /srv/http (or /srv/www). If you were running an FTP server, your files would go into /srv/ftp
- /tmp contains temporary files 
- symbolic links -> equivalent of shortcuts
- Shortcuts
    - /bin -> /usr/bin
    - /sbin -> /usr/sbin
    - /lib -> /usr/lib
    - /lib64 -> /usr/lib64
- `sudo apt install tree`
- `tree / -L 1`
    - tree - list the contents of directories in a tree like format
    - / specifies the root directory as a starting point for the tree command
    - L level 
    - 1 specifies a single level of directories , if you don't specify it , it will show all sub directories 
- su - root
    - switch user
- Absolute vs relative paths
    - Absolute path
        - Starts from the root directory: On Unix-like systems, this is indicated by the leading slash (/), and on Windows, it starts with a drive letter followed by a colon and a backslash (e.g., C:\).
        - Unambiguous: Because it starts from the root directory and includes all necessary directory names, an absolute path directly points to its location on the filesystem without any ambiguity.
        - Example on Unix/Linux: /home/user/documents/file.txt
    - Relative paths
        - A relative path points to a file or directory in relation to the current working directory (CWD) of the user or application. It does not begin with a root directory. 
        - Dependent on the current directory: Its effectiveness depends on the directory from which it is referenced.
        - Simpler and shorter: Often used to avoid typing long paths, especially when working deeply nested within a directory structure.- May include special characters: Such as . (current directory) and .. (parent directory) to navigate the filesystem.
        - Example: If your current directory is /home/user, and you want to refer to file.txt inside documents, the relative path would be documents/file.txt. If you need to move up to the parent directory, you might use ../otheruser/file.txt.
- command option argument 
- $ means normal user, # means root user
- uname -r or -a => to find out the kernel version
    - display kernel release of the operating system
    - -a provides all available system information -a stands for all
    - kernel name
    - node name (host name of the system)
    - kernel release (version number)
    - kernel version (additional detail about kernel build)
    - machine (hardware name)
- Predefined variables (environmental variables)
- `echo $HOME` - predefined variable => capital letters
    - `pwd` vs `echo $HOME`
    - `echo $SHELL` - to findo out the shell version
- **Shell types**
    - Bash (Bourne Again SHell): The most widely used shell on Linux. It's known for its user-friendliness and powerful scripting capabilities.
    - sh (Bourne Shell): The original Unix shell, now less commonly used directly but still influential.
    - zsh (Z Shell): Known for its interactive use features like improved tab completion and shared history.
    - csh (C Shell): Its syntax is praised for being more C-like, making it appealing to programmers familiar with C.
    - tcsh: An enhanced version of csh, with additional interactive features.

- Shell
    - is a ommand line interpreter that provides a user interface for access to OS' services
- Readings:
    - https://www.linuxfoundation.org/blog/blog/classic-sysadmin-the-linux-filesystem-explained#:~:text=The%20%2Fsrv%20directory%20contains%20data,go%20into%20%2Fsrv%2Fftp.
    - https://en.wikipedia.org/wiki/Unix_filesystem#Conventional_directory_layout

## Tue 23 April
- `date`, `date +%T`, `date +%D`
- `date --h`
- `timedatectl status` : display the current timezone along with other information about the system clock and synchronization status.
    - RTC - real time clock
    - NTP network time protocol - sync with NTP server
- `timedatectl list-timezones | grep -i australia/sydney` - search for australia/sydney
- `sudo timedatectl set-timezone Australia/Sydney`
- `timedatectl status`
- `time` + tab 
    - All words start with time
    - `time-admin`, `timedatectl`, `timed-read`, `timed-run`
- `id username` - displays the user and group IDs (UID and GID) along with the groups a user belongs to.
- `id root`
    - `id -u` only user ID, `id -g username` - show only primary group ID, `id -G username` - show all groups as IDs
- `tty`
    - text only terminal 
    - Each TTY in Linux is represented as a device file located in the /dev directory (e.g., /dev/tty1, /dev/ttyS0).
    - `who` : see who is logged in on which TTY.
    - `who -a`
        - run-level 5 means GUI
- `cat` : Concatenate FILE(s) to standard output.
    - read, create, and concatenate files. display text files, combine files, and redirect output in terminal or scripts.
    - `cat > file1.txt` : create a new file by redirecting the output of cat to a file
    - After you are done, `ctrl + d` : to save the text and exit 
    - `cat >> file1.txt `: >> append text tot the end of the existing file without overwriting the original content
    - `cat < file1.txt` : print the file 
    - `cat -n file1.txt` : See the line number for each line of the output 
- `touch` : change tile timestamps
    - change file timestamps—specifically, the access and modification times of files and directories.
    - `touch yourfilename{1..4}.txt` 
    - `touch -d "yesterday" filename`: Why change file timestamp?
        - Forensic or testing purposes: When simulating file activity from different times for testing or forensic analysis.
        - Preserve chronological order: In a scenario where file timestamps need to reflect a specific sequence, despite the actual creation times.
        - Scripting and automation: Adjust file timestamps as part of a larger scripted process or system setup.
- `mkdir`
    - -m, --mode=MODE  set file mode (as in chmod), not a=rwx - umask
    - -p, --parents  no error if existing, make parent directories as needed, with their file modes unaffected by any -m option.
    - -v, --verbose print a message for each created directory
    - -Z   set SELinux security context of each created directory to the default type
    - `mkdir -p japan/osaka/kansai/namba`
    - `tree -L 1` : print tree structure 

## Wed 24 April 2024

-  `mkdir -p OSAKA/{Linux/{Rhcsa,Rhce},Windows/{osaka,kyoto}}`
    ```
        └── OSAKA
            ├── Linux
            │   ├── Rhce
            │   └── Rhcsa
            └── Windows
                ├── kyoto
                └── osaka
    ````
- `total 12` - blob count 
    - typical block sizes for many filesystems, which means each directory takes up one block
    - Each directory (Rhce and Rhcsa) occupies 4096 bytes.
- `cp -rvf dir1 dir2`
    - "force." It tells the cp command to overwrite files without asking for confirmation if a file with the same name exists at the destination.
    - v - verbose
    - r - recursive 
- `mv` 
- `rm f*` 
- Soft Links (Symbolic Links):
    - A symbolic link, or soft link, is a type of file that is a reference or shortcut to another file or directory. It doesn't contain the data in the file it links to but rather a path to it.
    - To create a soft link, use the ln -s command.
- Hard Links:A hard link is another name for an existing file on the same filesystem. Unlike a symbolic link, a hard link is indistinguishable from the original file. Creating a hard link effectively creates another entry for the same file in the filesystem's table, so changes to the file are reflected in all hard links.
    - To create a hard link, use the ln command without the -s option.
    - Both the original and the link share the same inode (the filesystem's internal identifier for files), meaning they are essentially the same file.
- Key Differences:
    - Persistence: If you delete the original file, a soft link to it becomes a broken link and no longer works. A hard link, however, remains fully functional.
    - Cross-filesystem: Soft links can point to files on different filesystems, whereas hard links can only link to files on the same filesystem.
    - Directories: Soft links can link to directories. Hard links to directories are typically not allowed (except for special links like . and .. inside directories themselves), due to the potential for creating filesystem loops.

## Thurs 25 April 

- Files Types
    - hyphen Normal file
    - d for directory
    - c for character files (keyboard, mouse)
    - b for block files - HDD, DVD, CD, etc.
    - l for link files
        - soft link ==> shortcut 
        - hard link ==> backup file 
- `cd dev/` - dev contains device files, `ls -l`
    - check for files starts with b, c, d, l, etc.
- `file filename` - to get the type of file
    - `file dev`
    - `file lib`
    - `file tmp` : sticky, directory
- How to create a softlink
    - `ln -s /home/kali/tokyo tokyo_shortcut`
    - `cat >> tokyo_shortcut` - append the contents to the file
    - `du -h` 
        - du => disk usage 
        - h => human readable format
    - `inode` - identification part of the file , identify the file, contains properties of file apart from name
    - `ls -i` - inode number of files
- Hard link is ONLY for file, not for directory
    - `ln /home/student/hardl hl`
    - `ls -i hl`
- `ls`
    - `ls .hiddenfile` - . will hide fil/directory
    - `ls -al` - can see hidden files/dirs
    - How to unhide the files/dir - `mv .hidden hidden`
    - `ls -ld dirname` - find out directory
    - `ls -al [kf]*` - find files start with k or f
    - `ls -al [!kf]*` - find files start with k or f
- `touch bat mat rat hat cat fat lat`
    - `ls -al *at` vs `ls -al ?at`
    - `ls -l ?` - one letter file
    - `ls -l ??` - two letter file
    - `ls -l ???` - three letter file
    - `ls -l ????` - four letter file 
    - `ls -l [a-d]*`- any files starts with a to d

## Fri 26 April 

</details>