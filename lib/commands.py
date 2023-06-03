# Imports
from tkinter import filedialog, messagebox
import shutil
import os

# Global vars
filename = "Hamsterball.exe"
backedup = "textures/backedup"
ballfiles = ["BallBorder.png", "HamsterBall.png", "HamsterBall-Mip1.png", "HamsterBall-Mip2.png", "HamsterBall-Mip3.png"]

# Commands
def fileSelect(target):
    loc = filedialog.askdirectory()

    if loc == "":
            loc = "[not yet selected]"
            return

    filepath = os.path.join(loc, filename)
    textures = os.path.join(loc, "textures")
    dirpath = os.path.join(loc, backedup)

    if (os.path.isfile(filepath)):
        if (not os.path.isdir(dirpath)):
            try:
                os.mkdir(dirpath)

                for img in ballfiles:
                    shutil.copy2(os.path.join(textures, img), dirpath)
            except:
                messagebox.showerror("No permission", "Program doesn't have permission to change files in this directory. Quick fix: Run as administrator")
                return

        target.configure(
                        text=loc
                    )
    else:
        messagebox.showerror("Missing file", "Hamsterball.exe could not be found in this folder")
