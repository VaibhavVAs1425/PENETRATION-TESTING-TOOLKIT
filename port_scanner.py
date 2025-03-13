import socket

def scan_port(target_ip, port):
    """Scans a single port on the target IP."""
    try:
        # Create a socket object
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Set a timeout for connection attempts (in seconds)
        sock.settimeout(1)

        # Attempt to connect to the port
        result = sock.connect_ex((target_ip, port))

        if result == 0:
            print(f"Port {port}: Open")
        else:
            print(f"Port {port}: Closed")
        sock.close()

    except socket.gaierror:
        print("Hostname could not be resolved.")
        return
    except socket.error:
        print("Could not connect to server")
        return

if __name__ == "__main__":
    target_ip = input("Enter target IP address: ")
    ports_to_scan = input("Enter port range to scan (e.g., 1-100): ")
    start_port, end_port = map(int, ports_to_scan.split('-'))

    print(f"\nScanning target: {target_ip}")
    print("Scanning ports in range", start_port, "-", end_port)

    for port in range(start_port, end_port + 1):
        scan_port(target_ip, port)

    print("Port scanning completed.")

    # ... (rest of port_scanner.py code from before, including imports and scan_port function) ...

def main_scan_function(target_ip_input, ports_to_scan_input): # Renamed and made into a function that takes arguments
    target_ip = target_ip_input # Use the input directly
    ports_to_scan = ports_to_scan_input # Use the input directly
    start_port, end_port = map(int, ports_to_scan.split('-'))

    print(f"\nScanning target: {target_ip}")
    print("Scanning ports in range", start_port, "-", end_port)

    for port in range(start_port, end_port + 1):
        scan_port(target_ip, port)

    print("Port scanning completed.")


if __name__ == "__main__":
    target_ip = input("Enter target IP address: ") # Keep the input prompts here for direct execution of port_scanner.py
    ports_to_scan = input("Enter port range to scan (e.g., 1-100): ")
    main_scan_function(target_ip, ports_to_scan) # Call the function instead of direct code