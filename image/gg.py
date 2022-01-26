from PIL import Image
img = Image.open("cloud38.jpg")

w, h = img.size
imR = Image.new("RGB",(w,h),(0,0,0))
imG = Image.new("RGB",(w,h),(0,0,0))
imB = Image.new("RGB",(w,h),(0,0,0))
imMax = Image.new("RGB",(w,h),(0,0,0))
imMin = Image.new("RGB",(w,h),(0,0,0))
imMean = Image.new("RGB",(w,h),(0,0,0))


for i in range(w):
    for j in range(h):
        r, g, b = img.getpixel((i, j))
        maxi = max(r,g,b)
        mini = min(r,g,b)
        mean = int((r+g+b)//3)
        imR.putpixel((i,j),(r,r,r))
        imG.putpixel((i,j),(g,g,g))
        imB.putpixel((i,j),(b,b,b))
        imMax.putpixel((i,j), (maxi,maxi,maxi))
        imMin.putpixel((i,j), (mini,mini,mini))
        imMean.putpixel((i,j), (mean,mean,mean))


imMean.save("ImageGavg.jpg")
imMin.save("ImageGang.jpg")
imMax.save("ImageGaxg.jpg")
imR.save("R.jpg")
imG.save("g.jpg")
imB.save("b.jpg")
