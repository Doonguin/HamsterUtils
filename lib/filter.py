from PIL import Image

def recolorImage(reR, reG, reB):
    image = Image.open("./TEST IMAGES/HamsterBall.png")
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

    print("Image generated in ./TEST IMAGES/")
    image.save('./TEST IMAGES/recolored.png')