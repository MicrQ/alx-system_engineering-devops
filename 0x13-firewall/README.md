# 0x13. Firewall

A firewall is a network security device that monitors and controls incoming and outgoing network traffic based on predetermined security rules.
It establishes a barrier between a trusted network and an untrusted network, such as the internet, to prevent unauthorized access into or out of a computer network. Firewalls can filter unknown traffic and block outsiders from gaining access to private data.

This project is part of <b>ALX Software Engineering Program.</b> It is all about UFW(Uncomplicated FireWall) and how to set it up and running, how to prevent unauthorized access to a server, and more.....

## What I learned?
* How to install UFW on my web server(s).
* How to allow/deny access to the server(s).
* How to filter requests.
* How to redirect from one port to another.
* and Everything I should know about UFW.


## What to do?

The file <a href="https://github.com/MicrQ/alx-system_engineering-devops/blob/master/0x13-firewall/0-block_all_incoming_traffic_but">0-block_all_incoming_traffic_but</a> contains the UFW command you should run right after you install UFW using `sudo apt-get install ufw -y` command.
`BE CAREFULL`: if you do not run the command immediately, You may got locked out of your server and may not be able to connect using SSH.

The file <a href="https://github.com/MicrQ/alx-system_engineering-devops/blob/master/0x13-firewall/100-port_forwarding">100-port_forwarding</a> contains the UFW's `before.rules` content which is located in `/etc/ufw/before.rules`.
The first four lines added to forward any incoming traffic from port 8080 to 80. After addind those lines, to reload the UFW is required.
Use the command `sudo ufw reload` to reload the UFW.


## DoHardThings! - ALX
