# Libs
import tkinter as tk

# Create the window
def createWindow():
    mainWindow = tk.Tk()

    mainWindow.title("Hamster utils")
    mainWindow.geometry("800x600")
    mainWindow.resizable(False, False)
    mainWindow.configure(background="#2b2b3b")

    return mainWindow