from PIL import Image

im = Image.open("t1.jpg")
'''
width, height = im.size
print(im.format, im.size, im.mode)
print(width, height)


r,g,b = img.getpixel((0,0))
print ( r, g, b )
c = int((r+g+b)/3)
img.putpixel((0,0),int(c))
print(c)
img.save("tmp.jpg")


width, height = im.size
for i in range(width):
    for j in range(height):
        r,g,b = im.getpixel((i,j))
        c = int((r+g+b)/3)
        im.putpixel((i,j),(g,b,r))

im.show()        
'''

width, height = im.size
for i in range(width):
    for j in range(height):
            r, g, b = im.getpixel((i, j))
            
            red = int(r * 0.393 + g * 0.769 + b * 0.189)
            green = int(r * 0.349 + g * 0.686 + b * 0.168)
            blue = int(r * 0.272 + g * 0.534 + b * 0.131)
            
            if red > 255 :
                red == 255
            elif green > 255 :
                 green == 255
            elif blue > 255 :
                 blue == 255
                
            im.putpixel((i, j), (red, green, blue))

im.show() 
