# PENETRATION TESTING TOOLKIT v2.0

> **A Modular, Multi-Threaded Network Security Assessment Suite with GUI**

- **Company:** CODTECH IT Solutions
- **Intern Name:** Vaibhav Kumar Sahu
- **Intern ID:** CT08VYD
- **Domain:** Cybersecurity & Ethical Hacking
- **Duration:** 4 Weeks
- **Mentor:** Neela Santosh

---

## 📖 Project Description

The **Penetration Testing Toolkit** is a Python-based security suite designed to automate essential ethical hacking tasks. Unlike simple scripts, this toolkit uses a modular architecture, allowing users to switch between tools (modules) seamlessly.

**Version 2.0** represents a major upgrade, introducing **multi-threading** for high-speed scanning, a **Graphical User Interface (GUI)** for ease of use, and automated **file reporting**.

### Key Objectives
* **Education:** To demonstrate how security tools interact with network protocols (TCP, HTTP).
* **Automation:** To replace manual checks with fast, automated scripts.
* **Usability:** To provide both a command-line interface (CLI) for scripts and a GUI for visual users.

---

## 🚀 Features & Technical Implementation

### 1. 🖥️ Graphical User Interface (GUI)
* **What it does:** Provides a dashboard to configure and run attacks without typing commands.
* **How it works:** Built with `tkinter`. It acts as a "wrapper," collecting user input and running the backend scripts in a separate thread to keep the interface responsive.

### 2. ⚡ Multi-Threaded Port Scanner
* **What it does:** Scans a target server to find open ports (e.g., 80, 443, 22).
* **Technical Depth:** Unlike traditional scanners that check ports one by one (Sequential), this module uses `concurrent.futures` to check **100 ports simultaneously**.
* **Performance:** Scans 1,000 ports in ~10 seconds (vs. 15 minutes sequentially).

### 3. 📂 Directory Scanner (Web Enumeration)
* **What it does:** Hunts for hidden web directories that aren't linked on the homepage (e.g., `/admin`, `/backup`, `/config`).
* **Logic:** It performs a "dictionary attack" using a wordlist. It analyzes HTTP Status Codes:
    * `200 OK`: Directory exists (Found).
    * `403 Forbidden`: Directory exists but is protected (Found).
    * `404 Not Found`: Directory does not exist.

### 4. 🔐 Basic Auth Brute-Forcer
* **What it does:** Tests the strength of credentials on websites using "HTTP Basic Authentication."
* **Logic:** Iterates through username and password lists, sending encoded headers to the target until a `200 OK` response is received.

### 5. 📝 Automated Reporting
* **What it does:** Every scan automatically generates a text file report.
* **Benefit:** Critical for professional penetration testing documentation.

---

## 🛠️ Installation

### Prerequisites
* **Python 3.x** must be installed.

### Step 1: Clone or Download
Download the project files to your local machine. Ensure you have the following file structure:
```text
/Project_Folder
  ├── toolkit.py           (Main Controller)
  ├── port_scanner.py      (Module)
  ├── dir_scanner.py       (Module)
  ├── brute_forcer.py      (Module)
  ├── gui_app.py           (GUI Launcher)
  ├── requirements.txt     (Dependencies)
  └── wordlists/           (Optional folder for txt files)
```

### Step 2: Install Dependencies
Open your terminal/command prompt in the project folder.

For Windows:
```text
Bash

pip install -r requirements.txt
```

For Linux (Kali/Ubuntu): Linux users often need to install tkinter separately.

```text
Bash

sudo apt-get update
sudo apt-get install python3-tk
pip3 install -r requirements.txt
```

### 💻 Usage Guide
**A. Using the GUI (Recommended)**
This is the easiest way to use the toolkit.

1. Run the application:

```text
Bash

python gui_app.py
```

2. Select a Module (e.g., "Port Scanner").

3. Enter Target (e.g., scanme.nmap.org or http://example.com).

4. Configure Options (Port range or Wordlist file).

5. Click RUN MODULE.

6. The results will appear in the black log window and be saved to gui_report.txt.

**B. Using the Command Line (CLI)**
For advanced users who prefer the terminal.

1. Run Port Scanner

```text
Bash

python toolkit.py port_scanner --target <IP_ADDRESS> --ports 1-1000 --output scan_results.txt
```

2. Run Directory Scanner

```text
Bash

python toolkit.py dir_scanner --target <URL> --wordlist dirs.txt --output dir_results.txt
```

3. Run Brute Forcer

```text
Bash

python toolkit.py brute_forcer --target <URL> --usernames users.txt --passwords pass.txt
```

### ⚠️ Disclaimer

This tool is for educational purposes and ethical testing only. Do not use this toolkit on networks or websites you do not own or do not have explicit permission to test. Unauthorized access is illegal. The developer is not responsible for misuse.

### 🔮 Future Roadmap
[ ] Vulnerability Scanner: Integrate CVE lookup for open ports.

[ ] Subdomain Enumeration: Add DNS reconnaissance capabilities.

[ ] PDF Reporting: Generate professional PDF reports instead of text files.
