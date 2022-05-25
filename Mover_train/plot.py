# code for displaying multiple images in one figure

#import libraries
import cv2
from matplotlib import pyplot as plt
from PIL import Image
import glob
import os
from os import listdir

# create figure
fig = plt.figure(figsize=(10, 7))

# setting values to rows and column variables
rows = 4
columns = 5

list = [] 

  
original = '/output/A/' 
current_path = os.getcwd()
print("current_path", current_path)

#Reformat path by replacing \ to /
new_path = current_path.replace("\\", "/")
print("new path", new_path)

#Add original to current path
original = new_path + original
print("new original", original)


 
for images in os.listdir(original):
  if(images.endswith(".png") or images.endswith(".jpg")):
    print(images)
    x=original+images
    print(x)
    Image1 = Image.open(x).convert('RGB') 
    list.append(Image1)
 
print()
print(list) 
print()


total_img=len(list)
print(total_img)
for i in range(total_img):
  fig.add_subplot(rows, columns, i+1)
  plt.imshow(list[i])
  plt.axis('off')
  plt.title(i)



#add dpi to adjust resolution 
fig.savefig('lineplot.png')






