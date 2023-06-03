from PIL import Image
import tkinter as tk
from tkinter import messagebox
import shutil
import os

def recolorImage(reR, reG, reB, path, imgPreview):
    ballfiles = ["BallBorder.png", "HamsterBall.png", "HamsterBall-Mip1.png", "HamsterBall-Mip2.png", "HamsterBall-Mip3.png"]

    try:
        for img in ballfiles:
            shutil.copy2(os.path.join(path, f"backedup/{img}"), path)
    except:
        messagebox.showerror("An error occured", "Something has happened and I am also not sure what, sorry")
        return

    for img in ballfiles:
        image = Image.open(os.path.join(path, img))
        image = image.convert('RGBA')

        pixels = image.load()
        for x in range(image.width):
            for y in range(image.height):
                r, g, b, a = pixels[x, y]
                
                luminance = 0.299 * r + 0.587 * g + 0.114 * b
                
                recolored_r = int(reR * luminance)
                recolored_g = int(reG * luminance)
                recolored_b = int(reB * luminance)

                recolored_pixel = (recolored_r, recolored_g, recolored_b, a)

                pixels[x, y] = recolored_pixel

        hamsterBallEdited = os.path.join(path, img)

        image.save(hamsterBallEdited)

        hamsterballpng = os.path.join(path, "HamsterBall.png")
        image = tk.PhotoImage(file=hamsterballpng)

        imgPreview.configure(image=image)
        imgPreview.image = image