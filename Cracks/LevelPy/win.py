import sys
from unittest.mock import MagicMock

# 1. Trick Python into thinking Tkinter is fine
sys.modules['_tkinter'] = MagicMock()
import tkinter
from tkinter import messagebox

# 2. Define the 'entry' mock so the function doesn't crash
entry = MagicMock()
entry.get.return_value = "Saad_79_Percent"

# 3. Your actual logic pulled from the level
def check():
    if entry.get() == "Saad_79_Percent":
        print("WINNER!")
        print("Flag: {CYTH0N_TR4NSL4T10N_2026}")
    else:
        print("Fail")

# 4. Execute the win
check()
