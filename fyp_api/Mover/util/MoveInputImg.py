#Rename and move the image to another folder 
#1)Get current file path
#2)Replace '\' to '/' for the filepath
#3)Add original file path to current file path
#4)Add target file path to current file path
import glob
import shutil
import os
from os import listdir
from PIL import Image

#original = 'C:/Users/mevin/fyp_project3/Mover/upload_img/input/A/'
#target = 'C:/Users/mevin/fyp_project3/Mover/list/output/'
original = '/upload_img/input/A/'
target = '/list/output/'

#Get current path
current_path = os.getcwd()
print("current_path", current_path)

#Reformat path by replacing \ to /
new_path = current_path.replace("\\", "/")
print("new path", new_path)

#Add original to current path
original = new_path + original
print("new original", original)

#Add target to current path
target = new_path + target
print("new target", target)

#change Directory base on orginal file path
os.chdir(original)
for images in os.listdir(original):
  if(images.endswith(".png") or images.endswith(".jpg")):
    print(images)
    # rename the image and move image
    os.rename(original + images, target + '0000' + ".png")
    print("rename successful")
  else:
    print("file not found")
    
    

    
    
    
    
    
    