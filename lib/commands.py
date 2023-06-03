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
        
        imgPreview.configure(image=image, background="white")
        imgPreview.image = image
    else:
        messagebox.showerror("Missing file", "Hamsterball.exe could not be found in this folder")

def openColorPicker(location, path, imgPreview):
    if (location.cget('text') == "[not yet selected]"):
        messagebox.showerror("No image file", "Please select the main directory first")
        return

    color = colorchooser.askcolor(title="Select a color")
    
    if (color[0] is None):
        return
    
    r, g, b = color[0]

    r /= 255.0
    g /= 255.0
    b /= 255.0

    textures = os.path.join(path, "textures")

    recolorImage(r, g, b, textures, imgPreview)

def resetColors(path, imgPreview):
    if (path == "[not yet selected]"):
        messagebox.showerror("No image file", "Please select the main directory first")
        return
    
    textures = os.path.join(path, "textures")
    backups = os.path.join(textures, "backedup")

    try:
        for img in ballfiles:
            shutil.copy2(os.path.join(backups, img), textures)

        hamsterballpng = os.path.join(textures, "HamsterBall.png")
        image = tk.PhotoImage(file=hamsterballpng)

        imgPreview.configure(image=image)
        imgPreview.image = image
    except Exception as e:
        print(e)
        messagebox.showerror("An error occured", "Something has happened and I am also not sure what, sorry")