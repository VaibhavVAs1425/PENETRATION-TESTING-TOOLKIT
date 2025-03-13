# Penetration Testing Toolkit - Basic Version

This is a basic Penetration Testing Toolkit built in Python for learning purposes.

## Modules Included:

1.  **Port Scanner:**
    -   Scans TCP ports on a target IP address to determine if they are open or closed.
    -   **Usage:** Run `toolkit.py`, choose module 1, and enter the target IP and port range when prompted.

2.  **Brute Forcer (HTTP Basic Authentication):**
    -   Attempts to brute-force HTTP Basic Authentication by trying username and password combinations from wordlists.
    -   **Usage:** Run `toolkit.py`, choose module 2, and enter the target URL, path to username list file, and path to password list file when prompted.
    -   **Wordlist Files:** You need to create `usernames.txt` and `passwords.txt` files in the same directory as the scripts. Each line in these files should be a username or password respectively.

## How to Run:

1.  Make sure you have Python 3.x installed.
2.  Install the `requests` library if you plan to use the Brute Forcer module: `pip install requests` or `pip3 install requests`.
3.  Save all Python files (`toolkit.py`, `port_scanner.py`, `brute_forcer.py`, and `README.md`, `usernames.txt`, `passwords.txt` if needed) in the same directory.
4.  Open your command prompt or terminal, navigate to that directory, and run: `python toolkit.py` or `python3 toolkit.py`.
5.  Follow the prompts to use the toolkit modules.

## Important Notes:

-   **Ethical Use:** This toolkit is for educational purposes and for testing systems you have explicit permission to test. **Do not use it for illegal activities or to test systems without permission.**
-   **Basic Version:** This is a very basic version of a penetration testing toolkit. More modules and features can be added in the future.
-   **Wordlists for Brute Forcer:** The effectiveness of the brute-forcer depends heavily on the quality and size of your username and password wordlists. For testing, small wordlists are sufficient, but real-world brute-forcing often requires much larger lists.

## Further Development:

-   Add more modules (e.g., directory scanner, more advanced vulnerability scanners).
-   Improve error handling and user interface.
-   Add features to save scan results to files.
-   Explore using command-line arguments for `toolkit.py` for more flexibility (as we discussed earlier with `argparse`).