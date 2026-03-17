import sys
from unittest.mock import MagicMock

# 1. Neutralize the broken Tkinter system
sys.modules['_tkinter'] = MagicMock()
import tkinter as tk
from tkinter import messagebox

# 2. Mock the Entry widget so it 'contains' the password
entry = MagicMock()
entry.get.return_value = "Saad_79_Percent"

# 3. The Logic (extracted from your level.py)
def check():
    if entry.get() == "Saad_79_Percent":
        print("\n[✔] WINNER!")
        print("[✔] Flag: {CYTH0N_TR4NSL4T10N_2026}")
    else:
        print("\n[✘] Fail")

# 4. Trigger the logic immediately
check()
