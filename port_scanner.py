import socket
import concurrent.futures

def scan_port(target_ip, port, timeout=1):
    """
    Scans a single TCP port to check if it is open.
    Args:
        target_ip: The IP address of the target.
        port: The port number to scan.
        timeout: How long to wait for a response (seconds).
    Returns:
        The port number if open, None if closed or error.
    """
    try:
        # Create a socket object
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)
        # Attempt connection (returns 0 if successful)
        result = sock.connect_ex((target_ip, port))
        sock.close()
        if result == 0:
            return port
    except:
        pass
    return None

def main_scan_function(target_ip, ports_to_scan, output_file=None):
    """
    Main function to handle multi-threaded port scanning.
    """
    try:
        start_port, end_port = map(int, ports_to_scan.split('-'))
    except ValueError:
        print("Error: Invalid port range. Use format 'start-end' (e.g., 1-100).")
        return

    print(f"\n[*] Scanning target: {target_ip}")
    print(f"[*] Scanning ports: {start_port}-{end_port} (Threaded Mode)")

    open_ports = []
    
    # Use ThreadPoolExecutor to run 100 scans concurrently
    # This significantly speeds up the process compared to sequential scanning
    with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
        futures = {executor.submit(scan_port, target_ip, port): port for port in range(start_port, end_port + 1)}
        
        for future in concurrent.futures.as_completed(futures):
            port = futures[future]
            if future.result():
                print(f"[+] Port {port}: Open")
                open_ports.append(port)

    print(f"\n[*] Scan completed. Found {len(open_ports)} open ports.")
    
    # Save results to file
    if output_file:
        try:
            with open(output_file, 'a') as f:
                f.write(f"\n--- Port Scan Results for {target_ip} ---\n")
                for p in sorted(open_ports):
                    f.write(f"Port {p}: Open\n")
                f.write("--------------------------------------\n")
            print(f"[*] Results saved to {output_file}")
        except IOError as e:
            print(f"Error saving to file: {e}")
