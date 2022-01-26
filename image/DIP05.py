from PIL import Image

im = Image.open("WatWaAram.jpg")

red, green, blue = im.split()

r = red.histogram()
print("R :: Max : %d\t Min : %d\t Avg : %0.3f" %(max(r),min(r),sum(r)/len(r)))

g = green.histogram()
print("G :: Max : %d\t Min : %d\t Avg : %0.3f" %(max(g),min(g),sum(g)/len(g)))

b = blue.histogram()
print("B :: Max : %d\t Min : %d\t Avg : %0.3f" %(max(b),min(b),sum(b)/len(b)))

