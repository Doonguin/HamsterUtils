# Imports
from tkinter import filedialog, messagebox
import os

# Global vars
filename = "Hamsterball.exe"

# Commands
def fileSelect(target):
    loc = filedialog.askdirectory()

    filepath = os.path.join(loc, filename)

    if (os.path.isfile(filepath)):
        try:
            os.mkdir(os.path.join(loc, "textures/backedup"))
        except:
            messagebox.showerror("No permission", "Program doesn't have permission to change files in this directory. Quick fix: Run as administrator")
            return

        if loc == "":
            loc = "[not yet selected]"

        target.configure(
                        text=loc
                    )
    else:
        messagebox.showerror("Missing file", "Hamsterball.exe could not be found in this folder")
