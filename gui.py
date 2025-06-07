import tkinter as tk # Ensure tkinter is imported as 'tk'
from tkinter import ttk
from password_checker import check_password_strength # Import the logic from the other file

class PasswordStrengthApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Strength Checker")
        self.root.geometry("500x400") # Set initial window size
        self.root.resizable(True, True) # Allow resizing

        # Configure grid weights for responsive layout
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_rowconfigure(1, weight=1)
        self.root.grid_rowconfigure(2, weight=1)
        self.root.grid_rowconfigure(3, weight=1)
        self.root.grid_rowconfigure(4, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=1)

        # Styling
        style = ttk.Style()
        style.theme_use('clam') # Use a modern theme
        style.configure('TLabel', font=('Inter', 12))
        style.configure('TButton', font=('Inter', 12, 'bold'), padding=10)
        style.configure('TEntry', font=('Inter', 12), padding=5)
        style.configure('Strength.TLabel', font=('Inter', 14, 'bold'))
        style.configure('Feedback.TLabel', font=('Inter', 10), foreground='gray')

        # Password Entry Label
        self.password_label = ttk.Label(root, text="Enter Password:")
        self.password_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        # Password Entry Field
        self.password_entry = ttk.Entry(root, show="*", width=40) # show="*" hides the password
        self.password_entry.grid(row=0, column=1, padx=10, pady=10, sticky="ew")
        self.password_entry.bind("<KeyRelease>", self.update_strength) # Check on key release

        # Strength Label
        self.strength_label = ttk.Label(root, text="Strength: N/A", style='Strength.TLabel')
        self.strength_label.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="ew")

        # Feedback Label (using a Text widget for multi-line feedback)
        self.feedback_frame = ttk.LabelFrame(root, text="Feedback")
        self.feedback_frame.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")
        self.feedback_frame.grid_rowconfigure(0, weight=1)
        self.feedback_frame.grid_columnconfigure(0, weight=1)

        self.feedback_text = tk.Text(self.feedback_frame, wrap="word", height=8, font=('Inter', 10), state='disabled')
        self.feedback_text.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")

        self.feedback_scrollbar = ttk.Scrollbar(self.feedback_frame, orient="vertical", command=self.feedback_text.yview)
        self.feedback_scrollbar.grid(row=0, column=1, sticky="ns")
        self.feedback_text.config(yscrollcommand=self.feedback_scrollbar.set)

        # Show/Hide Password Checkbutton
        self.show_password_var = tk.BooleanVar()
        self.show_password_check = ttk.Checkbutton(root, text="Show Password",
                                                   variable=self.show_password_var,
                                                   command=self.toggle_password_visibility)
        self.show_password_check.grid(row=3, column=0, columnspan=2, padx=10, pady=5, sticky="w")

        # Initial update
        self.update_strength()

    def update_strength(self, event=None):
        """
        Retrieves the password from the entry field, checks its strength,
        and updates the GUI labels.
        """
        password = self.password_entry.get()
        if not password:
            self.strength_label.config(text="Strength: N/A", foreground="black")
            self.update_feedback(["Enter a password to check its strength."])
            return

        result = check_password_strength(password)
        strength_text = f"Strength: {result['strength']}"
        
        # Color code the strength label
        if result['strength'] == "Very Strong":
            color = "green"
        elif result['strength'] == "Strong":
            color = "forestgreen"
        elif result['strength'] == "Moderate":
            color = "orange"
        else: # Weak
            color = "red"
        
        self.strength_label.config(text=strength_text, foreground=color)
        self.update_feedback(result['feedback'])

    def update_feedback(self, feedback_list):
        """
        Updates the feedback Text widget with the provided list of messages.
        Includes error handling for TclError.
        """
        try:
            self.feedback_text.config(state='normal') # Enable editing
            self.feedback_text.delete(1.0, tk.END) # Clear existing text
            for msg in feedback_list:
                self.feedback_text.insert(tk.END, f"- {msg}\n")
            self.feedback_text.config(state='disabled') # Disable editing
        except tk.TclError as e:
            # This block catches errors related to Tkinter widget operations,
            # often occurring if a widget's underlying Tcl object becomes invalid.
            print(f"Error updating feedback text widget: {e}")
            # In a real application, you might want to display this error to the user
            # or attempt to gracefully recover. For now, it prints to the console.


    def toggle_password_visibility(self):
        """
        Toggles the visibility of the password in the entry field.
        """
        if self.show_password_var.get():
            self.password_entry.config(show="") # Show characters
        else:
            self.password_entry.config(show="*") # Hide characters

if __name__ == "__main__":
    # Create the main window
    root = tk.Tk()
    # Create an instance of the app
    app = PasswordStrengthApp(root)
    # Start the Tkinter event loop
    root.mainloop()