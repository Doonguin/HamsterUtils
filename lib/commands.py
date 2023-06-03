# Imports
from tkinter import filedialog, messagebox, colorchooser
from lib.filter import recolorImage
import tkinter as tk
import shutil
import os

# Global vars
filename = "Hamsterball.exe"
backedup = "textures/backedup"
ballfiles = ["BallBorder.png", "HamsterBall.png", "HamsterBall-Mip1.png", "HamsterBall-Mip2.png", "HamsterBall-Mip3.png"]

# Commands
def fileSelect(target, imgPreview):
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

        hamsterballpng = os.path.join(textures, "HamsterBall.png")
        image = tk.PhotoImage(file=hamsterballpng)

        target.configure(text=loc)
        
        imgPreview.configure(image=image)
        imgPreview.image = image
    else:
        messagebox.showerror("Missing file", "Hamsterball.exe could not be found in this folder")

def openColorPicker(location):
    if (location.cget('text') == "[not yet selected]"):
        messagebox.showerror("No image file", "Please select the main directory first")
        return

    color = colorchooser.askcolor(title="Select a color")
    r, g, b = color[0]

    r /= 255.0
    g /= 255.0
    b /= 255.0

    recolorImage(r, g, b)