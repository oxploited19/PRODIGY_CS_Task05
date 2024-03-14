# PRODIGY_CS_Task05
Network Pac Analyzer

Overview
      Network Pac Analyzer is a Python-based tool designed for capturing and analyzing network packets. It provides a user-friendly interface for monitoring network traffic, identifying potential threats, and          troubleshooting network issues. This tool is suitable for both network administrators and security professionals who need to monitor and analyze network traffic.

Features:
  Packet Capture: Capture network packets from specified interfaces with customizable packet count. The tool uses the tcpdump command-line utility for packet capture, providing flexibility and reliability.
  Packet Analysis: Analyze captured packets to display IP addresses, protocols, and payload data. The tool leverages the pyshark library for parsing captured packet data and extracting relevant information.
  User-Friendly Interface: Utilize colored text and formatting for improved readability. The tool employs colored text to highlight important messages and prompts, enhancing the user experience.
  Compatibility: Compatible with both Linux and Windows operating systems. The tool's codebase is designed to be platform-agnostic, allowing it to run seamlessly on different operating systems.
  Visual Appeal: Incorporates ASCII art welcome banner for visual appeal. The tool displays an ASCII art banner upon startup, adding a touch of personality to the user interface.
  
Installation
  Ensure Python is installed on your system. You can download Python from the official website.
  
Clone the repository:   git clone https://github.com/yourusername/network-pac-analyzer.git

Usage
  Run the main script:  python network_pac_analyzer.py
  Follow the on-screen prompts to select desired actions (capture, analyze, or exit). The tool provides clear instructions and guidance at each step to help users navigate through the functionality.
  
