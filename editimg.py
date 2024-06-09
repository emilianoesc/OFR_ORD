# Importing the PIL library
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import os

path=r'C:\Users\MELY\Desktop'
folder = os.path.join(path, 'IMAGENES NUEVAS')

def taparcosto(folder,size,x,y):
    for  file in os.listdir(folder):
        imgf=folder +"/"+ file
        # Open an Image
        img = Image.open(imgf)
        img = img.resize((1280, 1280))
        #width, height = img.size
        # Call draw Method to add 2D graphics in an image
        I1 = ImageDraw.Draw(img)
        # Custom font style and font size
        myFont = ImageFont.truetype("arial.ttf", size=size)
        # Add Text to an image
        I1.text((x, y), "•",font=myFont, fill=(0, 0, 0))
        # Display edited image
        #img.show()
        # Save the edited image
        filesave=os.path.join(folder, imgf)
        #imgspl=imgf.split('.')
        img.save(filesave)
        print(imgf)

#taparcosto(folder,585,1080,1330)#4
#taparcosto(folder,575,505,930)#3
#taparcosto(folder,575,505,315)#1
#taparcosto(folder,575,1095,315)#2




def recortar(folder):
    for  file in os.listdir(folder):
        imgf=folder +"/"+ file
        # Open an Image
        img = Image.open(imgf)
        #img = img.resize((1280, 1280))
        width, height = img.size
        # Call draw Method to add 2D graphics in an image
        I1 = ImageDraw.Draw(img)
        # Custom font style and font size
        left = 5
        top = 200
        right = width
        bottom = height-700
        img = img.crop((0, top, right, bottom))
        filesave=os.path.join(folder, imgf)
        #imgspl=imgf.split('.')
        img.save(filesave)
        print(imgf)

recortar(folder)