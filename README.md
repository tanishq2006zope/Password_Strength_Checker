# 🔐 Password Strength Checker

A Python application that evaluates the strength of a password based on multiple security criteria. This project features both a **command-line interface (CLI)** and a modern **GUI built with Tkinter** for user-friendly interaction.

---

## 📦 Features

- ✅ Real-time strength evaluation
- ✅ Detailed feedback on password quality
- ✅ GUI built with `tkinter` and `ttk`
- ✅ Strength levels: Very Weak → Very Strong
- ✅ Feedback includes length, character types, and common pattern warnings
- ✅ Toggle password visibility
- ✅ Scrollable feedback window

---

## 🧠 Strength Evaluation Criteria

| Criteria                  | Points |
|---------------------------|--------|
| Password length (12+)     | +3     |
| Password length (8–11)    | +2     |
| Contains uppercase letter | +1     |
| Contains lowercase letter | +1     |
| Contains numbers          | +1     |
| Contains special chars    | +2     |
| Uses common patterns      | -2     |

---

## 🗂️ Project Structure

password-strength-checker/
├── gui.py # Tkinter-based GUI
├── password_checker.py # Main logic for strength evaluation
└── README.md # Project overview and usage guide

## ✅ Requirements

- Python 3.x
- Tkinter (comes with most Python distributions)

---

## 🙌 Acknowledgements
- Developed using Python’s built-in re and tkinter libraries.
- Inspired by best practices in password security evaluation.

