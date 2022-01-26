from PIL import Image
img = Image.open("WatWaAram.jpg")

w, h = img.size

for i in range(w):
    for j in range(h):
        r, g, b = img.getpixel((i, j))
        mean = int((r+g+b)//3)
        if (mean > 127):
            img.putpixel((i,j),(255,255,255))
        else:
            img.putpixel((i,j),(0,0,0))

img.show()
