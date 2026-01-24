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

**Version 2.0** represents a major upgrade, introducing **multi-threading** for high-speed scanning, a **Graphical User Interface (GUI)** for ease of use, and a standalone **Executable (.exe)** for instant deployment.

### Key Objectives
* **Education:** To demonstrate how security tools interact with network protocols (TCP, HTTP).
* **Automation:** To replace manual checks with fast, automated scripts.
* **Usability:** To provide both a command-line interface (CLI) for scripts and a GUI for visual users.

---

## 🚀 Features & Technical Implementation

### 1. 🖥️ Graphical User Interface (GUI)
* **Functionality:** A dashboard to configure and run attacks without typing commands.
* **Implementation:** Built with `tkinter`. It runs backend scripts in separate threads to keep the interface responsive during long scans.

### 2. ⚡ Multi-Threaded Port Scanner
* **Functionality:** Scans a target server to find open ports (e.g., 80, 443, 22).
* **Technical Depth:** Uses `concurrent.futures` to check **100 ports simultaneously**, reducing scan time by over 90% compared to sequential scanning.

### 3. 📂 Directory Scanner (Web Enumeration)
* **Functionality:** Hunts for hidden web directories (e.g., `/admin`, `/backup`, `/config`) using a dictionary attack.
* **Logic:** Analyzes HTTP Status Codes:
    * `200 OK`: Found.
    * `403 Forbidden`: Found (Protected).
    * `404 Not Found`: Does not exist.

### 4. 🔐 Basic Auth Brute-Forcer
* **Functionality:** Tests credentials on websites using "HTTP Basic Authentication."
* **Logic:** Iterates through username/password lists until a valid login (`200 OK`) is found.

### 5. 📝 Automated Reporting
* **Functionality:** Every scan automatically generates a text file report (e.g., `gui_report.txt`) for documentation.

---

## 📥 Installation & Usage

### Option 1: Run the Executable (Recommended for Users)
*No Python installation required.*
1.  Go to the **Releases** section of this repository.
2.  Download `PenetrationToolkit_v2.zip`.
3.  **Extract the zip file** (Important: The `.exe` needs the `wordlists` folder to be in the same location).
4.  Double-click `PenetrationToolkit.exe` to launch.

## Project Structure:
```
/Penetration-Testing-Toolkit
  ├── README.md           <-- The documentation
  ├── requirements.txt    <-- The library list
  ├── toolkit.py          <-- Main command-line tool
  ├── gui_app.py          <-- The GUI (Source code)
  ├── port_scanner.py     <-- Scanner Module
  ├── dir_scanner.py      <-- Directory Module
  ├── brute_forcer.py     <-- Brute Force Module
  └── wordlists/          <-- Folder containing your .txt files
      ├── dirs.txt
      ├── usernames.txt
      └── passwords.txt
```
      

### Option 2: Run from Source Code (For Developers)
1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/VaibhavVAs1425/PENETRATION-TESTING-TOOLKIT.git](https://github.com/VaibhavVAs1425/PENETRATION-TESTING-TOOLKIT.git)
    ```
2.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
3.  **Run the GUI:**
    ```bash
    python gui_app.py
    ```

---

## 💻 Command Line Usage (CLI)

If you prefer the terminal, you can run `toolkit.py` directly:

**1. Run Port Scanner**
```bash
python toolkit.py port_scanner --target <IP_ADDRESS> --ports 1-1000 --output scan_results.txt
```

2. Run Directory Scanner

```Bash

python toolkit.py dir_scanner --target <URL> --wordlist wordlists/dirs.txt
```

3. Run Brute Forcer

```Bash

python toolkit.py brute_forcer --target <URL> --usernames wordlists/usernames.txt --passwords wordlists/passwords.txt
```

## Screenshot:


## ⚠️ Disclaimer
This tool is for educational purposes and ethical testing only. Do not use this toolkit on networks or websites you do not own or do not have explicit permission to test. Unauthorized access is illegal. The developer is not responsible for misuse.


