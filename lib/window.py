# Libs
import tkinter as tk

# Create the window
def createWindow():
    mainWindow = tk.Tk()

    mainWindow.title("HamsterUtils")
    mainWindow.geometry("500x330")
    mainWindow.configure(background="#2b2b3b")

    return mainWindow