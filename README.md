# Raft VIP manager

This project is based on RAFT-lite (https://github.com/nikwl/raft-lite). It hase some improvements in the RAFT implementation.

`Usage: vip.py [-h] -n NODE -v VIP -i INTERFACE [-V] -l LIST`

The options are:
 - **-h, --help**                   Help
 -  **-n NODE, --node NODE**        This node name
 -  **-v VIP, --virtual-ip VIP**    Virtual IP
 -  **-i INTERFACE, --interface INTERFACE** Interface to listen
 -  **-V, --verbose**               Be verbose
 -  **-l LIST, --list LIST**        List of nodes in format nodename:IP[:port],...

## RAFT-Lite
A simple and lightweight implementation of RAFT Consensus in Python. There are several other implementations out there but for the most part I found other implementations difficult to understand or lacking networking components. The goal of this repo is the RAFT algorithm as simple (and as localized) as possible. All of the state transition code is defined in a single file and the networking components are abstracted away such that it would be easy to adapt the system to use something like ROS, or another python library, to handle networking. Originially I wanted to use the the servers (or nodes as they're called here) as a kind of failure detector for a distrubuted system. As a result servers can be spawned within a single python program or can span multiple programs. Intercommunication parameters are loaded using a single json file, or can be passed in a dictionary.

### Installation and Testing
Clone the repo, create a new python environment and then run:
```bash
pip install -r requirements.txt
```

To test the system, edit the test script with your ip and then run:
```bash 
python test.py
```
