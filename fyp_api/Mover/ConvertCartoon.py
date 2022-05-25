#1)Clear all output
#2)Resize all input Image
#3)Generate cartoon Images
#4)Move orginal Image to output folder
#5)Resize all output Image
#6)Convert all output Image to GIF

import subprocess
import sys

print('Clear all ouput Images')
subprocess.call(['python', 'util/DeleteOutputImg.py'])

print('Resize all input Image')
subprocess.call(['python', 'util/ResizeInputImg.py'])

print('Generate cartoon Images')
subprocess.call(['python', 'gan/StyleGan/inference.py'])

print('Move orginal Image to output folder')
subprocess.call(['python', 'util/MoveInputImg.py'])

print('Resize all output Image')
subprocess.call(['python', 'util/ResizeOutputImg.py'])

print('Convert all output Image to GIF')
subprocess.call(['python', 'util/ConvertToGif.py'])
