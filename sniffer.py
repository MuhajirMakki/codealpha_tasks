from scapy.all import sniff
from scapy.layers.inet import IP, TCP, UDP, ICMP
from scapy.packet import Raw

def process_packet(packet):
    # Only process packets that have an IP layer
    if IP in packet:
        ip_src = packet[IP].src
        ip_dst = packet[IP].dst
        
        # Identify the protocol
        if TCP in packet:
            protocol = "TCP"
        elif UDP in packet:
            protocol = "UDP"
        elif ICMP in packet:
            protocol = "ICMP"
        else:
            protocol = "Other"

        print(f"[+] {protocol} Packet: {ip_src} -> {ip_dst}")

        # Extract and print raw payload data if it exists
        if packet.haslayer(Raw):
            try:
                payload = packet[Raw].load.decode('utf-8', 'ignore')
                print(f"    Payload: {payload[:50]}...") # Limit output to 50 chars
            except Exception as e:
                pass
        print("-" * 50)

print("Starting network sniffer... Press Ctrl+C to stop.")
# Sniff packets continuously. store=False prevents RAM overload.
sniff(prn=process_packet, store=False)