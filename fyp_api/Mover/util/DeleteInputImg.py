#Check if there any file in the Directory
#Images with format .png, .jpg, .gif, .mp4 are deleted in folder A
import os

#folder = r'C:/Users/mevin/fyp_project3/Mover/upload_img/input/A'
folder = 'upload_img/input/A'

dict = os.listdir(folder)

if len(dict) == 0:
  print("Directory is empty")
else:
  for images in dict:
      if images.endswith(".png") or images.endswith(".jpg") or images.endswith(".gif") or images.endswith(".mp4"):
          os.remove(os.path.join(folder, images))
          print(images + " is deleted")

