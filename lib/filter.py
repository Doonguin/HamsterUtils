from PIL import Image

image = Image.open("./TEST IMAGES/HamsterBall.png")
image = image.convert('RGBA')

pixels = image.load()

for x in range(image.width):
    for y in range(image.height):
        r, g, b, a = pixels[x, y]
        
        luminance = 0.299 * r + 0.587 * g + 0.114 * b
        
        recolored_r = int(0.4 * luminance)
        recolored_g = int(0 * luminance)
        recolored_b = int(0.3 * luminance)

        recolored_pixel = (recolored_r, recolored_g, recolored_b, a)

        pixels[x, y] = recolored_pixel

print("Image generated in ./TEST IMAGES/")
image.save('./TEST IMAGES/recolored.png')