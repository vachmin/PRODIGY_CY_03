import tkinter as tk
from tkinter import ttk
import re

def check_strength(event=None):
    # ... [Your check_strength code stays unchanged]
    pass  # <-- you already wrote this whole function

def main():
    window = tk.Tk()
    window.title("Password Complexity Checker")
    window.geometry("400x350")
    window.resizable(False, False)

    title_label = ttk.Label(window, text="🔒 Password Complexity Checker", font=("Arial", 16))
    title_label.pack(pady=10)

    entry = ttk.Entry(window, show="*", width=30, font=("Arial", 14))
    entry.pack(pady=10)
    entry.bind("<KeyRelease>", check_strength)

    global strength_label, criteria_labels
    strength_label = ttk.Label(window, text="Start typing...", font=("Arial", 14))
    strength_label.pack(pady=5)

    criteria_texts = [
        "• At least 8 characters",
        "• Contains uppercase letter",
        "• Contains lowercase letter",
        "• Contains number",
        "• Contains special character (!@#$...)"
    ]
    criteria_labels = []
    for text in criteria_texts:
        lbl = ttk.Label(window, text=text, font=("Arial", 12), foreground="grey")
        lbl.pack(anchor="w", padx=30)
        criteria_labels.append(lbl)

    window.mainloop()

if __name__ == "__main__":
    main()

