#Resize all images that are .png and jpg into a GIF
import glob
import os

import imageio
images = []

#root_dir='C:/Users/mevin/fyp_project3/Mover/list/output/'  
#gif_path='C:/Users/mevin/fyp_project3/Mover/list/output/movie.gif'
root_dir='list/output/'
gif_path='list/output/movie.gif'

print(root_dir)
for filename in glob.iglob(root_dir + '**/*.png', recursive=True):
    print(filename)
    images.append(imageio.imread(filename))

for filename in glob.iglob(root_dir + '**/*.jpg', recursive=True):
    print(filename)
    images.append(imageio.imread(filename))
    
imageio.mimsave(gif_path, images, fps=3, duration=0.5)
