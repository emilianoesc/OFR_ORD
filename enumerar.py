import os
import shutil
from newname import *
import math

path=r'C:\Users\MELY\Desktop'
directory  = os.path.join(path, 'ENUMERAR')
i=0

for subdir, dirs, files in os.walk(directory):
    if i == 0:
        i=i+1
    else:
       #####
      # nname3(subdir,subdir)
       #####
       nname2(subdir,subdir) 
       shutil.move(subdir, os.path.join(path, 'ORDEN'))


