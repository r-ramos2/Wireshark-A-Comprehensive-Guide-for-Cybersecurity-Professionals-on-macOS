# **Wireshark: A Comprehensive Guide for Cybersecurity Professionals on macOS**

## **Introduction**

In today’s cybersecurity landscape, the ability to analyze network traffic is crucial. **Wireshark** is a premier network protocol analyzer that enables professionals to capture and inspect data packets in real-time. This guide provides a step-by-step approach for using Wireshark effectively on macOS, covering everything from installation to advanced features.

---

## **Table of Contents**

- [Installation](#installation)
- [How to Use Wireshark](#how-to-use-wireshark)
- [Advanced Features](#advanced-features)
- [TLS Handshake Analysis](#tls-handshake-analysis)
- [Decrypting TLS Traffic](#decrypting-tls-traffic)
- [Capturing Wireless Traffic Using Monitor Mode](#capturing-wireless-traffic-using-monitor-mode)
- [Tracking IP Locations with GeoLite2](#tracking-ip-locations-with-geolite2)
- [Python Automation Project: Network Tracking with Wireshark & Google Maps](#python-automation-project-network-tracking-with-wireshark-and-google-maps)
- [Conclusion](#conclusion)
- [References](#references)
- [Contributing](#contributing)

---

## **Installation**

1. **Visit the Wireshark Website**  
   Go to the official Wireshark website: [Wireshark Download](https://www.wireshark.org/download.html).

2. **Download Wireshark**  
   Select the latest stable release for macOS.

3. **Install Wireshark**  
   Open the downloaded `.dmg` file and drag Wireshark into your Applications folder. Launch the application once the installation is complete.

---

## **How to Use Wireshark**

1. **Open Wireshark**  
   Launch Wireshark from your Applications folder.

2. **Select a Network Interface**  
   Under the **Capture** section, select the desired network connection (e.g., Ethernet or Wi-Fi).

3. **Start Capturing Traffic**  
   Click the **shark fin icon** to begin capturing network traffic. You can stop or restart the capture as needed. Captured data will include source IP, destination IP, and packet length.

4. **Filter Traffic**  
   Use the search bar to apply filters and view specific types of traffic:
   - **TCP Traffic**: `tcp`
   - **UDP Traffic**: `udp`
   - **Website Traffic**: `tcp contains [website name]`
   - **IP Address Traffic**: `ip.addr == [ip_address]`

5. **Inspect Packet Details**  
   Click on any packet row to examine detailed information. Use the drop-down arrows to explore different protocol layers (e.g., Ethernet, Internet Protocol, Transmission).

6. **Identify Sensitive Information**  
   To demonstrate the risks of unencrypted connections, visit an HTTP site and search for sensitive data like passwords:
   ```plaintext
   tcp contains [password]
   ```
   *Note: This is for educational purposes and highlights the importance of using encrypted connections.*

---

## **Advanced Features**

### **Capture and Protocol Filters**

1. **Set Capture Filters**  
   To limit captured traffic, apply filters before starting the capture:
   ```plaintext
   tcp port 443 or tcp port 80 or host [ip_address]
   ```

2. **Modify Capture Options**  
   Navigate to **Capture > Options** to adjust filters prior to a new capture session.

3. **Enable/Disable Protocols**  
   Click on **Analyze > Enable Protocols** to selectively enable or disable protocols as needed.

---

## **TLS Handshake Analysis**

Understanding the TLS handshake is critical for analyzing encrypted communications between clients and servers.

### **Steps:**

1. **Start the Capture**  
   Begin capturing network traffic while accessing a secure website.

2. **Filter for TCP Handshake**  
   Use the filter:
   ```plaintext
   tcp.port == 443
   ```

3. **Examine the Handshake**  
   Look for the following packets:
   - **SYN**, **SYN-ACK**, **ACK**: TCP three-way handshake.
   - **ClientHello**, **ServerHello**: TLS handshake negotiation.
   - **Key Exchange and Certificate Validation**: Packets indicating encryption mechanisms.

4. **View Certificate Details**  
   Click on the lock icon next to the web address in your browser to view the server certificate.

5. **Verify Handshake Protocol**  
   Click on **Transport Layer Security** in the middle pane to verify the handshake protocol.

6. **Check Cipher Suite**  
   Confirm the encryption type (Cipher Suite) within the **Transport Layer Security** section.

7. **Verify Data Encryption**  
   Click on **Transport Layer Security > Encrypted Application Data** to confirm encryption.

---

## **Decrypting TLS Traffic**

### **Decrypting HTTPS Traffic with Wireshark (Using Pre-Master Secret Keys)**

1. **Set SSLKEYLOGFILE Environment Variable**  
   Open Terminal and run:
   ```bash
   export SSLKEYLOGFILE=~/Documents/ssl.log
   ```

2. **Verify SSL Log File Creation**  
   Browse the web to ensure the `ssl.log` file is created.

3. **Configure Wireshark**  
   Navigate to **Edit > Preferences > Protocols > TLS** and set the **Pre-Master-Secret log filename** to the path of your SSL log file.

4. **Restart Capture**  
   Begin a new capture without saving the previous one. You should now see decrypted HTTPS traffic.

---

## **Capturing Wireless Traffic Using Monitor Mode**

### **Steps for macOS**:

1. **Open Terminal**  
   Launch the Terminal application.

2. **Check for Conflicts**  
   Run:
   ```bash
   sudo airmon-ng check
   ```

3. **Start Monitor Mode**  
   Run:
   ```bash
   sudo airmon-ng start en0  # Replace 'en0' with your wireless interface
   ```

4. **Verify Interface**  
   Run:
   ```bash
   sudo iwconfig
   ```

5. **Stop Monitor Mode**  
   When finished, stop monitor mode:
   ```bash
   sudo airmon-ng stop wlan0mon  # Replace 'wlan0mon' with your interface
   ```

---

## **Tracking IP Locations with GeoLite2**

1. **Download GeoLite2 Databases**  
   Visit [MaxMind's website](https://dev.maxmind.com/geoip/geolite2-free-geolocation-data) to download the **GeoLite2 ASN** and **GeoLite2 City** databases.

2. **Configure Wireshark**  
   Open Wireshark, navigate to **Edit > Preferences > Name Resolution**, and add the paths to the downloaded GeoLite2 databases.

3. **Start Capturing Traffic**  
   After starting the capture, click **Statistics > Endpoints**. You will see geographic data (e.g., city, country) based on the captured IP addresses.

---

## **Python Automation Project: Network Tracking with Wireshark & Google Maps**

### **Project Overview**  
This project automates network packet capture and visualizes the geographic locations of IP addresses using Wireshark and Python. The script parses packet data and plots IP addresses on Google Maps.

### **Steps**:

1. **Capture Network Traffic**  
   Use Wireshark to capture traffic and export the packet capture file (`.pcap`).

2. **Run the Python Script**  
   The Python script analyzes the packet data, extracts IP addresses, and queries the GeoLite2 databases for location information.

3. **Visualize IP Locations on Google Maps**  
   The script integrates with the Google Maps API to plot the IP addresses and their geographic locations.

---

## **Conclusion**

This guide provides a comprehensive overview of using Wireshark on macOS for network analysis in cybersecurity. Mastering Wireshark equips professionals with essential skills for monitoring network traffic, analyzing security events, and understanding encryption.

---

## **References**

- [Wireshark Official Documentation](https://www.wireshark.org/docs/)
- [MaxMind GeoLite2 Databases](https://dev.maxmind.com/geoip/geolite2-free-geolocation-data)
- [Network Tracking using Wireshark and Google Maps](https://github.com/devincapriola/Network-Tracking-using-Wireshark-and-Google-Maps)

---

## **Contributing**

Contributions are welcome! If you have suggestions for improvements or find any errors, please open an issue or submit a pull request.
