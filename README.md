# CodeAlpha_Basic_Network_Sniffer

## Overview
This repository contains a basic network sniffer developed as part of the CodeAlpha Cybersecurity Internship. The tool captures and analyzes live network traffic, extracting critical packet information such as Source IP, Destination IP, Protocol type, and payload data.

## Features
* **Real-time Packet Capture:** Utilizes the `scapy` library to intercept network traffic.
* **Protocol Identification:** Dynamically identifies TCP, UDP, and ICMP protocols.
* **Payload Extraction:** Displays raw payload data, demonstrating the difference between plain-text HTTP and encrypted HTTPS/TLS traffic.

## Technical Stack
* **Language:** Python 3.x
* **Libraries:** Scapy
* **Concepts Applied:** Network Protocols (OSI Model), Packet Analysis, Encryption Observation.

## Disclaimer
*This tool is for educational purposes only. It should only be run on networks where you have explicit permission to monitor traffic.*