from PIL import Image
img = Image.open("Image1.jpg")
width, height = img.size

w25 = int((width*25)/100)
h25 = int((height*25)/100)
img25 = img.resize((w25,h25))

w50 = int((width*50)/100)
h50 = int((height*50)/100)
img50 = img.resize((w50,h50))

w75 = int((width*75)/100)
h75 = int((height*75)/100)
img75 = img.resize((w75,h75))

img25.save("Image1-25.jpg")
img50.save("Image1-50.jpg")
img75.save("Image1-75.jpg")

