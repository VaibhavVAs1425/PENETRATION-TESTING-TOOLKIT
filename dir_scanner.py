import requests
import sys

def main_dir_scan_function(target_url, wordlist_path, output_file=None):
    """
    Scans a web server for hidden directories using a wordlist.
    """
    print(f"\n[*] Starting Directory Scan on: {target_url}")
    
    try:
        with open(wordlist_path, 'r') as file:
            directories = [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        print(f"Error: Wordlist file '{wordlist_path}' not found.")
        return

    found_dirs = []

    for directory in directories:
        # Construct full URL
        url = f"{target_url}/{directory}" if not target_url.endswith('/') else f"{target_url}{directory}"
        
        try:
            # Send HTTP GET request
            response = requests.get(url, timeout=3)
            
            # Check for success (200) or forbidden (403)
            if response.status_code == 200:
                print(f"[+] Found: {url} (Status: 200)")
                found_dirs.append(f"{url} (200)")
            elif response.status_code == 403:
                print(f"[!] Forbidden: {url} (Status: 403)")
                found_dirs.append(f"{url} (403)")
                
        except requests.RequestException:
            pass # Ignore connection errors

    print("[*] Directory scan completed.")

    # Save results
    if output_file:
        try:
            with open(output_file, 'a') as f:
                f.write(f"\n--- Directory Scan Results for {target_url} ---\n")
                if not found_dirs:
                    f.write("No directories found.\n")
                for d in found_dirs:
                    f.write(f"{d}\n")
                f.write("------------------------------------------\n")
            print(f"[*] Results saved to {output_file}")
        except IOError as e:
            print(f"Error saving to file: {e}")
