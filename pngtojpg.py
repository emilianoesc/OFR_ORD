from PIL import Image
import os
from pillow_heif import register_heif_opener
register_heif_opener()

def pngtojpg(file):
     if os.path.isfile(file):
            im1 = Image.open(file)
            f2=file.replace("png", "jpg")
            rgb_im = im1.convert('RGB')
            rgb_im.save(f2)
            return f2


def heictojpg(file):
    # Open HEIF or HEIC file
    image = Image.open(file)
    # Convert to JPEG
    f2=file.replace("heic", "jpg")
    image.convert('RGB').save(f2)


# assign directory


path=r'C:\Users\MELY\Desktop'
directory  = os.path.join(path, 'ENUMERAR')
for subdir, dirs, files in os.walk(directory):
    for filename in os.listdir(subdir):
        f = os.path.join(subdir, filename)
        # checking if it is a file
        print(f)
        #
        if f.endswith(".png"):
            pngtojpg(f)
            os.remove(os.path.join(subdir, filename))
        elif f.endswith(".heic"):
            heictojpg(f)
            os.remove(os.path.join(subdir, filename))
       
        


