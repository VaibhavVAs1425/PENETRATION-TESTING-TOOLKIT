import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import threading
import sys

# Import modules directly to ensure compatibility with PyInstaller (.exe)
import port_scanner
import dir_scanner
import brute_forcer

class RedirectText:
    """
    A helper class to redirect the 'print' statements from the console
    to the GUI text box.
    """
    def __init__(self, text_widget):
        self.output = text_widget

    def write(self, string):
        # Use .after() to ensure thread safety when updating the GUI
        if string:
            self.output.after(0, lambda: self._append(string))

    def _append(self, string):
        self.output.config(state='normal')
        self.output.insert(tk.END, string)
        self.output.see(tk.END) # Auto-scroll to the bottom
        self.output.config(state='disabled')

    def flush(self):
        pass # Required for file-like objects

class PentestToolkitGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Penetration Testing Toolkit (v2.0)")
        self.root.geometry("700x600")
        
        # --- Header Section ---
        header_frame = tk.Frame(self.root, bg="#2c3e50", pady=10)
        header_frame.grid(row=0, column=0, sticky="ew")
        tk.Label(header_frame, text="Cybersecurity Toolkit Dashboard", 
                 font=("Helvetica", 16, "bold"), bg="#2c3e50", fg="white").pack()

        # --- Main Content Section ---
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=1, column=0, sticky="nsew")

        # Module Selection Radio Buttons
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

        # Configuration/Inputs Area
        self.input_frame = ttk.LabelFrame(main_frame, text="Configuration", padding="10")
        self.input_frame.grid(row=2, column=0, columnspan=2, sticky="ew", pady=10)
        
        # Target Field (Always visible)
        ttk.Label(self.input_frame, text="Target (IP/URL):").grid(row=0, column=0, sticky="w", pady=5)
        self.target_entry = ttk.Entry(self.input_frame, width=40)
        self.target_entry.grid(row=0, column=1, sticky="w", pady=5)

        # Placeholder for dynamic inputs (changes based on module)
        self.dynamic_widgets = []
        self.update_inputs() 

        # Execution Button
        self.run_btn = tk.Button(main_frame, text="RUN MODULE", command=self.start_thread, 
                                 bg="#27ae60", fg="white", font=("Arial", 11, "bold"), padx=20, pady=5)
        self.run_btn.grid(row=3, column=0, columnspan=2, pady=10)

        # Output Log Window
        ttk.Label(main_frame, text="Execution Log:", font=("Arial", 10, "bold")).grid(row=4, column=0, sticky="w")
        self.output_area = scrolledtext.ScrolledText(main_frame, height=15, width=80, state='disabled', bg="#1e1e1e", fg="#00ff00")
        self.output_area.grid(row=5, column=0, columnspan=2, sticky="nsew", pady=5)
        
        # Configure grid weights for resizing
        main_frame.rowconfigure(5, weight=1)
        main_frame.columnconfigure(1, weight=1)

    def clear_dynamic_inputs(self):
        """Removes module-specific inputs when switching tools."""
        for widget in self.dynamic_widgets:
            widget.destroy()
        self.dynamic_widgets = []

    def update_inputs(self):
        """Adds the correct input fields based on the selected module."""
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
            lbl_u = ttk.Label(self.input_frame, text="Username File:")
            lbl_u.grid(row=1, column=0, sticky="w", pady=5)
            self.user_entry = ttk.Entry(self.input_frame, width=40)
            self.user_entry.insert(0, "usernames.txt")
            self.user_entry.grid(row=1, column=1, sticky="w", pady=5)
            
            lbl_p = ttk.Label(self.input_frame, text="Password File:")
            lbl_p.grid(row=2, column=0, sticky="w", pady=5)
            self.pass_entry = ttk.Entry(self.input_frame, width=40)
            self.pass_entry.insert(0, "passwords.txt")
            self.pass_entry.grid(row=2, column=1, sticky="w", pady=5)
            self.dynamic_widgets.extend([lbl_u, self.user_entry, lbl_p, self.pass_entry])

    def start_thread(self):
        """Runs the tool in a background thread to prevent GUI freezing."""
        self.run_btn.config(state="disabled")
        threading.Thread(target=self.run_tool, daemon=True).start()

    def run_tool(self):
        """Executes the selected module logic."""
        target = self.target_entry.get()
        if not target:
            messagebox.showerror("Error", "Target is required!")
            self.run_btn.config(state="normal")
            return

        # Redirect standard output (print) to the GUI text box
        old_stdout = sys.stdout
        sys.stdout = RedirectText(self.output_area)
        
        module = self.module_var.get()
        print(f"\n--- Starting {module} on {target} ---")

        try:
            # Call the specific function from the imported module
            if module == "port_scanner":
                port_scanner.main_scan_function(target, self.ports_entry.get(), "gui_report.txt")
            elif module == "dir_scanner":
                dir_scanner.main_dir_scan_function(target, self.wordlist_entry.get(), "gui_report.txt")
            elif module == "brute_forcer":
                brute_forcer.main_brute_force_function(target, self.user_entry.get(), self.pass_entry.get(), "gui_report.txt")
        except Exception as e:
            print(f"Error: {e}")
        finally:
            print("\n--- Task Completed ---")
            # Restore standard output and re-enable button
            sys.stdout = old_stdout
            self.root.after(0, lambda: self.run_btn.config(state="normal"))

if __name__ == "__main__":
    root = tk.Tk()
    app = PentestToolkitGUI(root)
    root.mainloop()
