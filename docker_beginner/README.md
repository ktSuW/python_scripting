# Docker Beginner course notes

## Docker Intro
- Why we need docker? Testing
- End to end application stacks
  - web server - nodejs, express
  - DB - mongoDB
  - Messaging - reddis
  - Orchestration e.g. Ansible
- Compatibility 
  - with different OS
  - libraries and dependencies
  - long setup time
  - different dev/test/prod environments
  - Application 
-  docker -> OS -> Hardwaree Infrastcture - run inside each container, with each own dependency and all libraries, all on same vm
- What are containers?

## Install Docker in Kali Linux
- Installing docker on Kali linux command, https://www.kali.org/docs/containers/installing-docker-on-kali/
- `either sudo su --> not a good security practice` : 
- `sudo apt update` : 
    - superuser do
    - apt - advanced package tool- it is a commendline for handling packages on debian based package
    - update - This option tells apt to refresh the local package index with the latest changes made in the repos
- `sudo apt install -y docker.io`   : 
    - install a new package called docker.io using apt
- `sudo systemctl enable docker --now`  : 
    - systemctl is a command-line tool for controlling the systemd system and service manager
    - enable - this options tells `systemctl` to enable docker so that it starts automatically at boot time
    - systemctl
        - command line utility in Linux used to control the systemd system and service manager.
        - systemd is an init system and system manager that has become the stand for many linux distributions.
        - It is responsible for initializing the system, starting services, and managing system processes
        - systemctl is an essential tool for system administration in linux environments that use `systemd`
        - systemctl command provides a way to interact with systemd to perform various tasks such as below:
            - starting, stopping, restarting and checking the status of the services
            - enabling and disabling services to start automatically at boot time
            - managing system states like rebooting, shutting down and suspending the system
            - Viewing logs and status of the system and services

            ```
                sudo systemctl start servicename
                sudo systemctl stop servicename
                sudo systemctl enable servicename => to enable a service to start at boot
                sudo systemctl status servicename => check the status of a service
            ```
- `sudo usermod -aG docker $USER`   : 
- `echo "deb [arch=amd64 signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/debian bookworm stable" | \ sudo tee /etc/apt/sources.list.d/docker.list`    : 
- `curl -fsSL https://download.docker.com/linux/debian/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg`    : 
- `sudo apt update` : 
- `sudo apt install -y docker-ce docker-ce-cli containerd.io` : 
- `start docker` : 
- `docker version` : 
