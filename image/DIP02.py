from PIL import Image
img = Image.open("t1.jpg")
'''
r,g,b = img.split()
img1 = Image.merge("RGB",(r,r,r))
img2 = Image.merge("RGB",(g,g,g))
img3 = Image.merge("RGB",(b,b,b))
'''
w, h = img.size
imR = Image.new("RGB",(w,h),(0,0,0))
imG = Image.new("RGB",(w,h),(0,0,0))
imB = Image.new("RGB",(w,h),(0,0,0))
imMax = Image.new("RGB",(w,h),(0,0,0))
imMin = Image.new("RGB",(w,h),(0,0,0))
imMean = Image.new("RGB",(w,h),(0,0,0))
sumimg = Image.new("RGB",(w*3,h*2),(0,0,0))

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


sumimg.paste(imR,(0,0))
sumimg.paste(imG,(w,0))
sumimg.paste(imB,(w*2,0))
sumimg.paste(imMax,(0,h))
sumimg.paste(imMin,(w,h))   
sumimg.paste(imMean,(w*2,h))

sumimg.show()
