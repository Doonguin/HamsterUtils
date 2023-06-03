# imports
import tkinter as tk
from tkinter import filedialog, colorchooser

# Buttons
def createSelectFolderButton(parent):
    folderButton = tk.Button(
                                parent, 
                                text="select", 
                                background="green", 
                                foreground="white",
                                relief="flat",
                                font=('Arial 12')
                            )
    folderButton.grid(row=1, column=0, padx=20, pady=0, sticky="w")
    folderButton.configure(cursor="hand2")

    return folderButton

def createColorButton(parent):
    colorButton = tk.Button(
                                parent, 
                                text="pick color", 
                                background="green", 
                                foreground="white",
                                relief="flat",
                                font=('Arial 12')
                            )
    colorButton.grid(row=3, column=0, padx=20, pady=0, sticky="w")
    colorButton.configure(cursor="hand2")

    return colorButton