import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import subprocess
import threading
import sys

class PentestToolkitGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Penetration Testing Toolkit (v2.0)")
        self.root.geometry("700x600")
        
        # Configure Grid
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(1, weight=1)

        # --- Header ---
        header_frame = tk.Frame(self.root, bg="#2c3e50", pady=10)
        header_frame.grid(row=0, column=0, sticky="ew")
        tk.Label(header_frame, text="Cybersecurity Toolkit Dashboard", 
                 font=("Helvetica", 16, "bold"), bg="#2c3e50", fg="white").pack()

        # --- Main Content Area ---
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=1, column=0, sticky="nsew")

        # Module Selection
        ttk.Label(main_frame, text="Select Module:", font=("Arial", 10, "bold")).grid(row=0, column=0, sticky="w", pady=5)
        self.module_var = tk.StringVar(value="port_scanner")
        
        module_frame = ttk.Frame(main_frame)
        module_frame.grid(row=1, column=0, columnspan=2, sticky="w", pady=5)
        
        ttk.Radiobutton(module_frame, text="Port Scanner", variable=self.module_var, 
                        value="port_scanner", command=self.update_inputs).pack(side="left", padx=10)
        ttk.Radiobutton(module_frame, text="Directory Scanner", variable=self.module_var, 
                        value="dir_scanner", command=self.update_inputs).pack(side="left", padx=10)
        ttk.Radiobutton(module_frame, text="Brute Forcer", variable=self.module_var, 
                        value="brute_forcer", command=self.update_inputs).pack(side="left", padx=10)

        # Input Fields Frame
        self.input_frame = ttk.LabelFrame(main_frame, text="Configuration", padding="10")
        self.input_frame.grid(row=2, column=0, columnspan=2, sticky="ew", pady=10)
        
        # Target Input (Always visible)
        ttk.Label(self.input_frame, text="Target (IP/URL):").grid(row=0, column=0, sticky="w", pady=5)
        self.target_entry = ttk.Entry(self.input_frame, width=40)
        self.target_entry.grid(row=0, column=1, sticky="w", pady=5)

        # Dynamic Inputs (Ports, Wordlists, etc.)
        self.dynamic_widgets = []
        self.update_inputs() # Initialize inputs

        # Run Button
        self.run_btn = tk.Button(main_frame, text="RUN MODULE", command=self.run_tool, 
                                 bg="#27ae60", fg="white", font=("Arial", 11, "bold"), padx=20, pady=5)
        self.run_btn.grid(row=3, column=0, columnspan=2, pady=10)

        # Output Area
        ttk.Label(main_frame, text="Execution Log:", font=("Arial", 10, "bold")).grid(row=4, column=0, sticky="w")
        self.output_area = scrolledtext.ScrolledText(main_frame, height=15, width=80, state='disabled', bg="#1e1e1e", fg="#00ff00")
        self.output_area.grid(row=5, column=0, columnspan=2, sticky="nsew", pady=5)
        
        # Configure resizing
        main_frame.rowconfigure(5, weight=1)
        main_frame.columnconfigure(1, weight=1)

    def clear_dynamic_inputs(self):
        for widget in self.dynamic_widgets:
            widget.destroy()
        self.dynamic_widgets = []

    def update_inputs(self):
        """Updates the input fields based on the selected module."""
        self.clear_dynamic_inputs()
        module = self.module_var.get()

        if module == "port_scanner":
            lbl = ttk.Label(self.input_frame, text="Port Range (e.g., 1-1000):")
            lbl.grid(row=1, column=0, sticky="w", pady=5)
            self.ports_entry = ttk.Entry(self.input_frame, width=20)
            self.ports_entry.insert(0, "1-100")
            self.ports_entry.grid(row=1, column=1, sticky="w", pady=5)
            self.dynamic_widgets.extend([lbl, self.ports_entry])

        elif module == "dir_scanner":
            lbl = ttk.Label(self.input_frame, text="Wordlist Path:")
            lbl.grid(row=1, column=0, sticky="w", pady=5)
            self.wordlist_entry = ttk.Entry(self.input_frame, width=40)
            self.wordlist_entry.insert(0, "dirs.txt")
            self.wordlist_entry.grid(row=1, column=1, sticky="w", pady=5)
            self.dynamic_widgets.extend([lbl, self.wordlist_entry])

        elif module == "brute_forcer":
            # Username File
            lbl_u = ttk.Label(self.input_frame, text="Username File:")
            lbl_u.grid(row=1, column=0, sticky="w", pady=5)
            self.user_entry = ttk.Entry(self.input_frame, width=40)
            self.user_entry.insert(0, "usernames.txt")
            self.user_entry.grid(row=1, column=1, sticky="w", pady=5)
            
            # Password File
            lbl_p = ttk.Label(self.input_frame, text="Password File:")
            lbl_p.grid(row=2, column=0, sticky="w", pady=5)
            self.pass_entry = ttk.Entry(self.input_frame, width=40)
            self.pass_entry.insert(0, "passwords.txt")
            self.pass_entry.grid(row=2, column=1, sticky="w", pady=5)
            
            self.dynamic_widgets.extend([lbl_u, self.user_entry, lbl_p, self.pass_entry])

    def log(self, message):
        self.output_area.config(state='normal')
        self.output_area.insert(tk.END, message + "\n")
        self.output_area.see(tk.END)
        self.output_area.config(state='disabled')

    def run_tool(self):
        target = self.target_entry.get()
        if not target:
            messagebox.showerror("Error", "Target is required!")
            return

        module = self.module_var.get()
        command = [sys.executable, "toolkit.py", module, "--target", target]

        # Build command based on module
        if module == "port_scanner":
            ports = self.ports_entry.get()
            command.extend(["--ports", ports])
        elif module == "dir_scanner":
            wordlist = self.wordlist_entry.get()
            command.extend(["--wordlist", wordlist])
        elif module == "brute_forcer":
            users = self.user_entry.get()
            pwds = self.pass_entry.get()
            command.extend(["--usernames", users, "--passwords", pwds])
        
        # Add output file argument
        command.extend(["--output", "gui_report.txt"])

        self.log(f"\n--- Starting {module} on {target} ---")
        self.run_btn.config(state="disabled")
        
        # Run in a separate thread to keep GUI responsive
        threading.Thread(target=self.execute_command, args=(command,), daemon=True).start()

    def execute_command(self, command):
        try:
            process = subprocess.Popen(
                command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, bufsize=1, universal_newlines=True
            )
            
            for line in process.stdout:
                self.root.after(0, self.log, line.strip())
            
            process.wait()
            self.root.after(0, lambda: self.run_btn.config(state="normal"))
            self.root.after(0, lambda: self.log("--- Task Completed ---"))
            
        except Exception as e:
            self.root.after(0, lambda: self.log(f"Error: {str(e)}"))
            self.root.after(0, lambda: self.run_btn.config(state="normal"))

if __name__ == "__main__":
    root = tk.Tk()
    app = PentestToolkitGUI(root)
    root.mainloop()
