# main.py

import tkinter as tk
from start_window import show_start_window

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()  # Masquer la fenêtre racine
    show_start_window(root) 
