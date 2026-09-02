# Network Intrusion Detection System (IDS) Implementation

## 1. System Setup
* **Tool Used:** Snort v2.9 (Open Source IDS) on Windows.
* **Deployment:** Snort was configured in NIDS mode, actively sniffing traffic on the primary Wi-Fi network interface using Npcap. 

## 2. Rule Configuration
Custom rules were implemented in `local.rules` to detect:
1. **Reconnaissance:** ICMP Ping floods indicating Nmap network scanning.
2. **Access Attacks:** SSH brute-force attempts targeting port 22.
3. **Web Attacks:** Cleartext SQL injection signatures (`UNION SELECT`) targeting port 80.

## 3. Continuous Monitoring Strategy
* Snort was executed in quiet console mode (`snort.exe -q -i 4 -c local.rules -A console`), bypassing default warnings to continuously capture raw packets.
* Output was monitored in real-time, successfully detecting simulated ICMP attacks.

## 4. Incident Response Mechanism
When a critical alert is triggered:
1. **Identification:** Snort logs the source IP and payload signature.
2. **Containment:** The SOC analyst adds the offending source IP to the Windows Defender Firewall blocklist.
3. **Recovery:** The analyst reviews the packet capture (PCAP) to ensure no internal systems were successfully exploited.

## 5. Visualization (Optional Dashboarding)
* Snort logs can be forwarded to **Splunk** (or an ELK stack) to parse the alert severity, plotting source IPs on a geographic map and charting attack frequencies over time.