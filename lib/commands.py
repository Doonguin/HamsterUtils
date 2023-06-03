# Imports
import tkinter as tk
from tkinter import filedialog

# Commands
def fileSelect(target):
    loc = filedialog.askdirectory()

    if loc == "":
        loc = "[not yet selected]"

    target.configure(
                        text=loc
                    )
