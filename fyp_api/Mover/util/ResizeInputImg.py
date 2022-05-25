#Resize all images under A folder

import PIL
import os
import os.path
from PIL import Image

#dict = r'C:\Users\mevin\fyp_project3\Mover\upload_img\input\A'
dict = 'upload_img/input/A'

#Default/High resolution (Quality=95)
#Medium Resolution (Quality=25)
#Low Resolution (Quality=1)
for file in os.listdir(dict):
    f_img = dict+"/"+file
    img = Image.open(f_img)
    img = img.resize((256,256))
    img.save(f_img, quality=95)