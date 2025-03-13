import argparse
import port_scanner
import brute_forcer

def main():
    parser = argparse.ArgumentParser(description="Penetration Testing Toolkit")
    parser.add_argument("module", choices=['port_scanner', 'brute_forcer'], help="Module to run")
    parser.add_argument("--target", help="Target IP address or URL")
    parser.add_argument("--ports", help="Port range for port scanner (e.g., 1-100)")
    parser.add_argument("--usernames", help="Path to username list file for brute-forcer")
    parser.add_argument("--passwords", help="Path to password list file for brute-forcer")

    args = parser.parse_args()

    if args.module == 'port_scanner':
        if not args.target or not args.ports:
            print("Error: Port scanner requires --target and --ports arguments.")
            return
        port_scanner.main_scan_function(args.target, args.ports) # Assuming you'll adjust port_scanner.py
    elif args.module == 'brute_forcer':
        if not args.target or not args.usernames or not args.passwords:
            print("Error: Brute-forcer requires --target, --usernames, and --passwords arguments.")
            return
        brute_forcer.main_brute_force_function(args.target, args.usernames, args.passwords) # Assuming you'll adjust brute_forcer.py
    else:
        print("Invalid module selected.")

if __name__ == "__main__":
    main()