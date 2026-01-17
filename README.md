# PENETRATION TESTING TOOLKIT v2.0

- **Company:** CODTECH IT Solutions
- **Intern Name:** Vaibhav Kumar Sahu
- **Intern ID:** CT08VYD
- **Domain:** Cybersecurity & Ethical Hacking
- **Duration:** 4 Weeks
- **Mentor:** Neela Santosh

# PROJECT DESCRIPTION
The **Penetration Testing Toolkit** is a comprehensive Python-based security suite designed for ethical hacking education. It provides a modular framework to perform essential network security assessments, including port scanning, directory enumeration, and authentication testing.

This project demonstrates the power of Python in cybersecurity, featuring both a command-line interface (CLI) for scripting and a Graphical User Interface (GUI) for ease of use.

# FEATURES & IMPLEMENTATION

### 1. Graphical User Interface (GUI)
* **Functionality:** A Tkinter-based dashboard that allows users to control all modules visually.
* **Benefit:** Eliminates the need to memorize complex command-line arguments.
* **Usage:** Run `python gui_app.py`.

### 2. Multi-Threaded Port Scanner
* **Functionality:** Scans TCP ports to identify open services.
* **Enhancement:** Implements `concurrent.futures` for multi-threading, increasing scan speed by over 1000% compared to sequential scanning.
* **Output:** Real-time terminal feedback and file-based reporting.

### 3. Directory Scanner (Web Enumeration)
* **Functionality:** Performs a dictionary attack on web servers to find hidden directories (e.g., `/admin`, `/login`, `/config`).
* **Logic:** Utilizes the `requests` library to check HTTP status codes (200 OK vs 403 Forbidden vs 404 Not Found).

### 4. Basic Authentication Brute-Forcer
* **Functionality:** Tests HTTP Basic Auth endpoints against username and password lists.
* **Safety:** Designed for educational testing on authorized targets.

### 5. Automated Reporting
* **Functionality:** All modules support an `--output` flag to save scan findings to a text file automatically.
* **Benefit:** Essential for professional penetration testing documentation.

# TECH STACK
* **Language:** Python 3.x
* **Libraries:** `socket`, `requests`, `threading`, `concurrent.futures`, `tkinter`, `argparse`
* **Tools:** VS Code, Git

# HOW TO RUN

1.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

2.  **Run via GUI (Recommended):**
    ```bash
    python gui_app.py
    ```

3.  **Run via Command Line:**
    * **Port Scanner:**
        ```bash
        python toolkit.py port_scanner --target <IP> --ports 1-1000 --output report.txt
        ```
    * **Directory Scanner:**
        ```bash
        python toolkit.py dir_scanner --target [http://example.com](http://example.com) --wordlist dirs.txt
        ```

# FUTURE ENHANCEMENTS PLANNED
* **Vulnerability Scanning:** Integration of CVE lookup based on open ports.
* **Subdomain Enumeration:** Adding DNS recon modules.
* **Network Sniffer:** Implementing a packet sniffer using `scapy`.
