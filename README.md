# PENETRATION TESTING TOOLKIT

- **Company:** CODTECH IT Solutions
- **Intern Name:** Vaibhav Kumar Sahu
- **Intern ID:** CT08VYD
- **Domain:** Cybersecurity & Ethical Hacking
- **Duration:** 4 Weeks
- **Mentor:** Neela Santosh

# PROJECT DESCRIPTION
The **Penetration Testing Toolkit** is a Python-based project designed to implement fundamental network security tools for penetration testing and ethical hacking education. This toolkit provides a modular and practical way to understand and utilize essential techniques used in cybersecurity assessments.

Penetration testing is a crucial aspect of cybersecurity, enabling security professionals to identify vulnerabilities and improve system defenses. This project aims to showcase the power of Python for security tooling and provides a command-line interface (CLI) for users to perform basic penetration testing operations in a controlled and ethical environment.

# TASK DETAILS

**Task Objective:** Develop a Python-based modular toolkit that includes at least a port scanner and a brute-force module for penetration testing education.

**Key Functionalities:**

*   Port Scanning: Identify open TCP ports on a target system.
*   Basic Authentication Brute-Forcing: Attempt to discover credentials for HTTP Basic Authentication protected resources.

**Tools & Technologies Used:**

*   **Python 3.x:** The primary programming language used for building the toolkit.
*   **Python `socket` Library:** For network socket operations in the Port Scanner module.
*   **Python `requests` Library:** For making HTTP requests in the Brute-Forcer module.
*   **Python `argparse` Module:** For creating a command-line interface for the toolkit.
*   **Text Editor/IDE:** (e.g., VS Code, Sublime Text, PyCharm) for code development.
*   **Command Prompt / Terminal:** For running the Python toolkit.

**Editor/Platform Used:**

*   VS Code (or IntelliJ IDEA / Eclipse / Sublime Text / Thonny) for development.
*   Command Prompt / PowerShell / Terminal for running the application.

# Features

**1. Port Scanner Module:**

*   **Functionality:** Scans a specified range of TCP ports on a target IP address or hostname.
*   **Output:** Reports the status of each scanned port as "Open" or "Closed".
*   **Usage:**  Run via the toolkit's command-line interface, specifying the `port_scanner` module, target IP, and port range.

**2. Brute-Forcer Module (Basic Authentication):**

*   **Functionality:** Attempts to brute-force HTTP Basic Authentication on a given URL using provided username and password lists.
*   **Input:** Takes a target URL, a file path to a username list, and a file path to a password list.
*   **Output:**  Reports successful username/password combinations if found, and indicates failed attempts.
*   **Usage:** Run via the toolkit's command-line interface, specifying the `brute_forcer` module and required arguments for target URL and wordlist files.

**Exit Option:**

*   The toolkit and individual modules are designed to complete their tasks and then exit gracefully. Users can terminate execution at any time using standard command-line interrupt methods (e.g., Ctrl+C).

# Applicability

*   **Cybersecurity Education:**  Provides a hands-on learning tool for understanding penetration testing fundamentals.
*   **Network Security Assessment (Ethical Use Only):**  Can be used in controlled environments to assess the security posture of systems you have permission to test.
*   **Security Tool Development Foundation:** Serves as a basic framework for building more complex and advanced security tools in Python.
*   **Scripting and Automation in Security:** Demonstrates the use of Python for automating security-related tasks.

# How to Run the Program

1.  **Ensure Python 3.x is installed** on your system. You can verify by running:
    ```bash
    python --version
    ```
    If Python is not installed, download it from [https://www.python.org/downloads/](https://www.python.org/downloads/).

2.  **Install the `requests` library** if you plan to use the Brute-Forcer module. Open a terminal or command prompt and run:
    ```bash
    pip install requests
    ```
    or
    ```bash
    pip3 install requests
    ```

3.  **Save the Python files** (`toolkit.py`, `port_scanner.py`, `brute_forcer.py`) in the same directory.  If you intend to use the Brute-Forcer module, also create `usernames.txt` and `passwords.txt` files in the same directory, with usernames and passwords listed line by line.

4.  **Open a terminal or command prompt** and navigate to the directory where the files are saved using the `cd` command.

5.  **Run the toolkit using:**
    ```bash
    python toolkit.py <module_name> <module_arguments>
    ```
    Replace `<module_name>` with either `port_scanner` or `brute_forcer`.
    Replace `<module_arguments>` with the arguments required for the chosen module (see examples below).

    **Example Usage:**

    *   **To run the Port Scanner:**
        ```bash
        python toolkit.py port_scanner --target scanme.nmap.org --ports 1-100
        ```
    *   **To run the Brute-Forcer (Basic Auth):**
        ```bash
        python toolkit.py brute_forcer --target [http://example.com](http://example.com) --usernames usernames.txt --passwords passwords.txt
        ```
        **(Remember to replace `http://example.com`, `usernames.txt`, and `passwords.txt` with your actual test URL and file paths.)**

6.  **Follow the on-screen prompts and output from the toolkit.**

# Future Enhancements

*   **Graphical User Interface (GUI):** Develop a GUI for improved user experience, potentially using libraries like Tkinter, PyQt, or Kivy.
*   **More Penetration Testing Modules:** Add modules for other common penetration testing tasks, such as:
    *   Directory Bruteforcing/Web Directory Scanning
    *   Service Version Detection
    *   Vulnerability Scanning
    *   Subdomain Enumeration
*   **Advanced Scan Options for Port Scanner:** Implement different scan types (SYN scan, UDP scan), speed optimization (threading/async), and more detailed port status reporting.
*   **More Authentication Methods for Brute-Forcer:**  Support form-based authentication, API authentication, and other authentication mechanisms.
*   **Output to File/Reporting:** Implement options to save scan results and brute-force output to files for reporting and analysis.
*   **Error Handling and Input Validation:** Enhance error handling and input validation to make the toolkit more robust and user-friendly.

# Conclusion

This Penetration Testing Toolkit is a foundational project for learning about cybersecurity and penetration testing techniques using Python. It provides practical experience in building modular security tools and understanding essential concepts like port scanning and brute-force attacks. This project serves as a valuable stepping stone for developers interested in pursuing cybersecurity, network security, and ethical hacking domains.

# OUTPUT

![INPUT BRUTE_FORCER](https://github.com/user-attachments/assets/8dc0f8b0-3eef-412c-b3e4-00698859fb52)
**This is Input of Brute_Forcer**
![OUTPUT BRUTE_FORCR](https://github.com/user-attachments/assets/afda43a4-05f5-43b8-b684-25c7ab242392)
**This is Output of Brute_Forcer**
![Input port_scanner](https://github.com/user-attachments/assets/4b16fe91-0439-48b8-a402-a4e6a9e8feea)
**This is Input of Port_scanner**
![Output Port_scanner](https://github.com/user-attachments/assets/46db3fe5-b31a-451c-93ce-f49fa182906e)
**This is Output of Port_scanner**
