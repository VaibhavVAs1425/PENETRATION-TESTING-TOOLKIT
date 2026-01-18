import socket
import concurrent.futures

def scan_port(target_ip, port, timeout=1):
    """
    Scans a single port.
    Returns the port number if open, None if closed.
    """
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)
        result = sock.connect_ex((target_ip, port))
        sock.close()
        if result == 0:
            return port  # Port is open
    except:
        pass
    return None

def main_scan_function(target_ip, ports_to_scan, output_file=None):
    """
    Orchestrates the threaded scan and handles reporting.
    """
    try:
        start_port, end_port = map(int, ports_to_scan.split('-'))
    except ValueError:
        print("Error: Invalid port range format. Use start-end (e.g., 1-100).")
        return

    print(f"\n[*] Scanning target: {target_ip}")
    print(f"[*] Scanning ports: {start_port}-{end_port} (Threaded Mode)")

    open_ports = []
    
    # Use ThreadPoolExecutor to scan 100 ports simultaneously
    with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
        # Create a dictionary of future tasks
        futures = {executor.submit(scan_port, target_ip, port): port for port in range(start_port, end_port + 1)}
        
        # As threads complete, check results
        for future in concurrent.futures.as_completed(futures):
            port = futures[future]
            if future.result():
                print(f"[+] Port {port}: Open")
                open_ports.append(port)

    print(f"\n[*] Scan completed. Found {len(open_ports)} open ports.")
    
    # Save results to file if requested
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
