#Resize all images under output folder

import PIL
import os
import os.path
from PIL import Image

#dict = r'C:\Users\mevin\fyp_project3\Mover\list\output'
dict = 'list/output'

#Default/High resolution (Quality=95)
#Medium Resolution (Quality=25)
#Low Resolution (Quality=1)
for file in os.listdir(dict):
    f_img = dict+"/"+file
    img = Image.open(f_img)
    img = img.resize((256,256))
    img.save(f_img, quality=95)