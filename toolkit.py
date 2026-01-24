import argparse
import port_scanner
import brute_forcer
import dir_scanner

def main():
    """
    Main controller for the CLI (Command Line Interface).
    Parses user arguments and directs them to the appropriate module.
    """
    # Create the argument parser
    parser = argparse.ArgumentParser(description="Penetration Testing Toolkit v2.0")
    
    # Argument: Module selection (Required)
    parser.add_argument("module", choices=['port_scanner', 'brute_forcer', 'dir_scanner'], 
                        help="Select the module to run")
    
    # Arguments: Configuration (Optional depending on module)
    parser.add_argument("--target", help="Target IP address or URL")
    parser.add_argument("--ports", help="Port range for port scanner (e.g., 1-100)")
    parser.add_argument("--usernames", help="Path to username list file for brute-forcer")
    parser.add_argument("--passwords", help="Path to password list file for brute-forcer")
    parser.add_argument("--wordlist", help="Path to directory wordlist for dir_scanner")
    parser.add_argument("--output", help="Path to save results (e.g., results.txt)")

    args = parser.parse_args()

    # Logic to select and run the correct module
    if args.module == 'port_scanner':
        if not args.target or not args.ports:
            print("Error: Port scanner requires --target and --ports arguments.")
            return
        port_scanner.main_scan_function(args.target, args.ports, args.output)
        
    elif args.module == 'brute_forcer':
        if not args.target or not args.usernames or not args.passwords:
            print("Error: Brute-forcer requires --target, --usernames, and --passwords arguments.")
            return
        brute_forcer.main_brute_force_function(args.target, args.usernames, args.passwords, args.output)
        
    elif args.module == 'dir_scanner':
        if not args.target or not args.wordlist:
            print("Error: Directory scanner requires --target and --wordlist arguments.")
            return
        dir_scanner.main_dir_scan_function(args.target, args.wordlist, args.output)
        
    else:
        print("Invalid module selected.")

if __name__ == "__main__":
    main()
