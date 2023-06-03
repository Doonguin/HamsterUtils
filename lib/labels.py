# Imports
import tkinter as tk

# Labels
def explainationFolder(parent):
    explainationFolderSelect = tk.Label(
                                            parent, 
                                            text="Select the folder where \"Hamsterball.exe\" is located:",
                                            foreground="white",
                                            background="#2b2b3b",
                                            font=("Arial 12")
                                        )
    explainationFolderSelect.grid(row=0, column=0, columnspan=10, pady=0, padx=20, sticky="w")

    return explainationFolderSelect

def selectedLocLabel(parent):
    filePathIndic = tk.Label(
                                parent, 
                                text="[not yet selected]", 
                                height=1,
                                foreground="white",
                                background="#2b2b3b",
                                font=("Arial 12")
                            )
    filePathIndic.grid(row=1, column=1, padx=0, pady=20)

    return filePathIndic

def createPreview(parent):
    image_label = tk.Label(parent)
    image_label.grid(row=2, column=0, padx=20, pady=0, sticky="w")

    return image_label