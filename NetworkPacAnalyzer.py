import os
import platform
import subprocess
import pyshark
from tqdm import tqdm
import colored

# Check and install required packages
def check_install_package(package):
    try:
        __import__(package)
    except ImportError:
        print(f"Installing {package}...")
        subprocess.check_call(["pip", "install", package])

# Check and install required packages
required_packages = ['pyshark', 'colored', 'tqdm']
for package in required_packages:
    check_install_package(package)

# Function to display ASCII art welcome banner
def display_welcome_banner():
    print(colored.fg("cyan"))
    print("                 ___====-_  _-====___                  ")
    print("           _--^^^#####//      \\#####^^^--_            ")
    print("        _-^##########// (    ) \\##########^-_         ")
    print("       -############//  |\^^/|  \\############-        ")
    print("     _/############//   (@::@)   \\############\_      ") 
    print("    /#############((     \\//     ))#############\	   ")
    print("   -###############\\    (oo)    //###############-    ")
    print("  -#################\\  / VV \  //#################-   ")
    print(" -###################\\/      \//###################-  ")
    print("_#/|##########/\######(   /\   )######/\##########|\#_ ")
    print("|/ |#/\#/\#/\/  \#/\##\  |  |  /##/\#/  \/\#/\#/\#| \| ")
    print("`  |/  V  V  `   V  \#\| |  | |/#/  V   '  V  V  \|  ' ")
    print("   `   `  `      `   / | |  | | \   '      '  '   '    ")
    print("                    (  | |  | |  )   Welcome to the Network Packet")
    print("                   __\ | |  | | /__         Capture/Analyzer Tool!")
    print("                  (vvv(VVV)(VVV)vvv)                   ")
    print("                                                 //by-oxploited19")
    print("╚══════╝ ╚═════╝ ╚═╝ ╚══════╝ ╚═════╝ ╚═╝ ╚══════╝ ╚═════╝╚══════╝")
    print("Before we begin, please ensure you have the given permissions/-Enjoy-Capturing[^_^]")
    print(colored.attr("reset"))

# Function to display thank you message
def display_thank_you_message():
    print(colored.fg("cyan") + "Thank you for using my tool oxploited19" + colored.attr("reset"))

# Function to greet the user with their username
def greet_user():
    username = os.getlogin()
    print(colored.fg("cyan") + f"Welcome, {username}!\n" + colored.attr("reset"))

# Function to request user permission
def request_permission():
    print(colored.fg("red") + "Prodigy-InfoTech\n" + colored.attr("reset"))
    print("Before we begin, please ensure you have the given permissions/-Enjoy-Capturing[^_^]")

# Function to get list of network interfaces
def get_interfaces():
    try:
        result = subprocess.run(['ifconfig'], capture_output=True, text=True)
        interfaces = [line.split(':')[0] for line in result.stdout.split('\n') if 'UP' in line]
        return interfaces
    except Exception as e:
        print(colored.fg("red") + f"An unexpected error occurred: {e}" + colored.attr("reset"))
        return []

# Function to ask the user if they want to capture or analyze packets
def get_action_choice():
    while True:
        action_choice = input(colored.fg("yellow") + "Do you want to capture (c) or analyze (a) packets, or exit (e)? " + colored.attr("reset")).lower()
        if action_choice in ["c", "a", "e"]:
            return action_choice
        else:
            print(colored.fg("red") + "Invalid input. Please enter 'c' for capture, 'a' for analyze, or 'e' to exit." + colored.attr("reset"))

# Function to capture network packets
def run_packet_capture(interface, packet_count):
    try:
        file_path = input(colored.fg("yellow") + "Enter the path to save the captured packets (press Enter for default 'captured_packets.pcap'): " + colored.attr("reset")).strip() or "captured_packets.pcap"
        print(colored.fg("green") + f"Capturing {packet_count} packets from interface {interface}. Press Ctrl+C to stop capturing." + colored.attr("reset"))
        # Use tqdm to create a progress bar
        with tqdm(total=packet_count, desc="Capturing packets", unit="packet") as pbar:
            process = subprocess.Popen(["sudo", "tcpdump", "-i", interface, "-c", str(packet_count), "-w", file_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
            for line in process.stderr:
                if "packets captured" in line:
                    pbar.update(int(line.split()[0]))
                    break
            process.communicate()  # Wait for tcpdump to finish
        print(colored.fg("green") + f"Packets captured successfully and saved to: {os.path.abspath(file_path)}" + colored.attr("reset"))
        return file_path
    except KeyboardInterrupt:
        print(colored.fg("red") + "\nPacket capture process terminated by user." + colored.attr("reset"))
    except Exception as e:
        print(colored.fg("red") + f"An unexpected error occurred: {e}" + colored.attr("reset"))

# Function to analyze captured packets
def analyze_packets(file_path):
    try:
        if not os.path.exists(file_path):
            print(colored.fg("red") + f"Error: File '{file_path}' does not exist." + colored.attr("reset"))
            return
        # Check if the file is a valid PCAP file
        capture = pyshark.FileCapture(file_path)
        print(colored.fg("green") + "Analyzing captured packets..." + colored.attr("reset"))
        for packet in capture:
            print(packet)
    except KeyboardInterrupt:
        print(colored.fg("red") + "\nAnalysis process terminated by user." + colored.attr("reset"))
    except Exception as e:
        print(colored.fg("red") + f"An unexpected error occurred: {e}" + colored.attr("reset"))

# Function to display IP source and destination addresses
def display_ip_addresses(file_path):
    try:
        if not os.path.exists(file_path):
            print(colored.fg("red") + f"Error: File '{file_path}' does not exist." + colored.attr("reset"))
            return
        # Check if the file is a valid PCAP file
        capture = pyshark.FileCapture(file_path)
        print(colored.fg("green") + "Displaying IP source and destination addresses:" + colored.attr("reset"))
        for packet in capture:
            print("Source IP:", packet.ip.src)
            print("Destination IP:", packet.ip.dst)
    except KeyboardInterrupt:
        print(colored.fg("red") + "\nAnalysis process terminated by user." + colored.attr("reset"))
    except Exception as e:
        print(colored.fg("red") + f"An unexpected error occurred: {e}" + colored.attr("reset"))

# Function to display protocols
def display_protocols(file_path):
    try:
        if not os.path.exists(file_path):
            print(colored.fg("red") + f"Error: File '{file_path}' does not exist." + colored.attr("reset"))
            return
        # Check if the file is a valid PCAP file
        capture = pyshark.FileCapture(file_path)
        print(colored.fg("green") + "Displaying protocols:" + colored.attr("reset"))
        for packet in capture:
            print("Protocol:", packet.transport_layer)
    except KeyboardInterrupt:
        print(colored.fg("red") + "\nAnalysis process terminated by user." + colored.attr("reset"))
    except Exception as e:
        print(colored.fg("red") + f"An unexpected error occurred: {e}" + colored.attr("reset"))

# Function to display payload data
def display_payload(file_path):
    try:
        if not os.path.exists(file_path):
            print(colored.fg("red") + f"Error: File '{file_path}' does not exist." + colored.attr("reset"))
            return
        # Check if the file is a valid PCAP file
        capture = pyshark.FileCapture(file_path)
        print(colored.fg("green") + "Displaying payload data:" + colored.attr("reset"))
        for packet in capture:
            print("Payload data:", packet.data)
    except KeyboardInterrupt:
        print(colored.fg("red") + "\nAnalysis process terminated by user." + colored.attr("reset"))
    except Exception as e:
        print(colored.fg("red") + f"An unexpected error occurred: {e}" + colored.attr("reset"))

# Function to handle analysis options
def analysis_options(file_path):
    while True:
        print(colored.fg("yellow") + "\nAnalysis Options:\n" + colored.attr("reset"))
        print("1. Display IP source and destination addresses")
        print("2. Display protocols")
        print("3. Display payload data")
        print("4. Exit analysis options\n")
        choice = input(colored.fg("yellow") + "Select an analysis option (1, 2, 3, or 4): " + colored.attr("reset"))
        if choice == "1":
            display_ip_addresses(file_path)
        elif choice == "2":
            display_protocols(file_path)
        elif choice == "3":
            display_payload(file_path)
        elif choice == "4":
            break
        else:
            print(colored.fg("red") + "Invalid option. Please select 1, 2, 3, or 4." + colored.attr("reset"))

# Main function
def main():
    try:
        display_welcome_banner()
        greet_user()
        request_permission()
        
        while True:
            action_choice = get_action_choice()

            if action_choice == "c":
                interfaces = get_interfaces()
                for idx, interface in enumerate(interfaces):
                    print(f"{idx + 1}. {interface}")
                selected_interface = int(input("Select the interface to capture packets (Enter interface number): ")) - 1
                interface = interfaces[selected_interface]

                packet_count = int(input("Enter the number of packets to capture: "))

                file_path = run_packet_capture(interface, packet_count)

            elif action_choice == "a":
                file_path = input("Enter the path to the captured packets file: ").strip()
                analyze_packets(file_path)
                analysis_options(file_path)

            elif action_choice == "e":
                break

        display_thank_you_message()

    except KeyboardInterrupt:
        print(colored.fg("red") + "\nExiting..." + colored.attr("reset"))
    except Exception as e:
        print(colored.fg("red") + f"An unexpected error occurred: {e}" + colored.attr("reset"))

if __name__ == "__main__":
    main()
