from PIL import Image,ImageChops

im = Image.open("tmp.jpg")
w, h = im.size

imcp = im.copy()
if imcp.mode == "RGB":
    cmyk_im = imcp.convert("CMYK")

imcp.show()
print(imcp.mode)
cmyk_im.show()
print(cmyk_im.mode)

sepia_im = Image.new("RGB",(w,h),(0,0,0))

graysc = Image.new("RGB",(w,h),(0,0,0))

for i in range(w):
    for j in range(h):
            r, g, b = im.getpixel((i, j))
            
            red = int(r * 0.393 + g * 0.769 + b * 0.189)
            green = int(r * 0.349 + g * 0.686 + b * 0.168)
            blue = int(r * 0.272 + g * 0.534 + b * 0.131)
            if red > 255 :red == 255
            elif green > 255 :green == 255
            elif blue > 255 :blue == 255   
            sepia_im.putpixel((i, j), (red, green, blue))

            c = int((r+g+b)//3)
            graysc.putpixel((i, j), (c,c,c))
 
sepia_im.show()

invim = ImageChops.invert(graysc)
cyncl = Image.new("RGB",(w,h),(5,35,100))
cyn_im = ImageChops.add(cyncl,invim)
cyn_im.show()
