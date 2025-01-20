# Packet Sniffer Tool

<p align="center">
  <a href="#introduction">Introduction</a> •
  <a href="#features">Features</a> •
  <a href="#installation">Installation</a> •
  <a href="#usage">Usage</a> •
  <a href="#working">Working</a> •
  <a href="#future-enhancements">Future Enhancements</a> •
  <a href="#disclaimer">Disclaimer</a>
</p>

---

## Introduction

The **Packet Sniffer Tool** is a Python-based utility that uses the `Scapy` library to capture and analyze network packets in real-time. This tool helps in monitoring HTTP traffic, detecting sensitive keywords like `username` and `password`, and provides insights into network activity for educational or penetration testing purposes.



## Screenshots

<h1 align="left">
  <img src="image.png" alt="Packet Sniffer" width="700px"></a>
  <br>
</h1>

---

## Features

- **Real-Time Packet Capture**: Captures and analyzes packets from a specified network interface.
- **HTTP Request Monitoring**: Extracts URLs from HTTP requests and displays them in a readable format.
- **Keyword Detection**: Highlights sensitive data like `username`, `password`, and `email` in intercepted packets.
- **Rich Integration**: Beautifies the output using the `Rich` library for better readability.
- **Command-Line Interface**: Easily configurable through command-line arguments.

---

## Installation

### Prerequisites

To run this project, you need:

- **Python**: Version 3.6 or higher.
- **Scapy Library**: Install it using pip:
  ```bash
  pip install scapy
  pip install rich

  git clone https://github.com/your-repo/packet-sniffer.git
  cd packet-sniffer



---

## Usage
- Run the script with the required arguments:
  
      python packet_sniffer.py -i <interface>
  Replace <`interface`> with your network interface (e.g., `eth0` , `wlan0` ).



  - Example:
    
         python packet_sniffer.py -i eth0
- Press `Ctrl+C` to stop the tool gracefully.
  



---

## Working
- Packet Capture: The script listens to packets on the specified network interface using Scapy.
- HTTP Monitoring: It checks for HTTP requests in the captured packets and extracts URLs.
- Keyword Detection: Analyzes packet payloads for sensitive keywords such as `username` or `password`.
- Formatted Output: The tool displays captured data with styled and color-coded formatting using the `Rich` library.

---


## Future Enhancements
- Add support for saving intercepted data to a file (CSV or JSON).
- Implement HTTPS packet decryption (with proper permissions).
- Expand keyword detection with a customizable list of terms.
- Add multi-threading for more efficient packet processing.
- Include support for analyzing non-HTTP protocols (e.g., FTP, DNS).


---

## Disclaimer
This tool is for educational purposes only. Unauthorized packet capturing or intercepting network traffic without proper consent is illegal. Ensure you have permission to monitor any network you use this tool on. Use responsibly.
