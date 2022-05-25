#1)Clear all output
#2)Generate happy Images
#3)Generate sad Images
#4)Move orginal Image to output folder
#5)Resize all output Image
#6)Convert all output Image to GIF

import subprocess
import sys

print('Clear all ouput Images')
subprocess.call(['python', 'util/DeleteOutputImg.py'])

#weight for this model is 220 epoch
print('Generate happy Images')
subprocess.call(['python', 'gan/CycleGan/test.py', 
                 '--dataroot', 'upload_img',
                 '--generator_B2A', 'logs/happy@07.04.2022-15_38_07/220/netG_B2A.pth',
                 '--order', '1',
])

#weight for this model is 160 epoch
print('Generate sad Images')
subprocess.call(['python', 'gan/CycleGan/test.py', 
                 '--dataroot', 'upload_img',
                 '--generator_B2A', 'logs/sad@14.04.2022-23_56_10/160/netG_B2A.pth',
                 '--order', '2',
])

print('Move orginal Image to output folder')
subprocess.call(['python', 'util/MoveInputImg.py'])

print('Resize all output Image')
subprocess.call(['python', 'util/ResizeOutputImg.py'])

print('Convert all output Image to GIF')
subprocess.call(['python', 'util/ConvertToGif.py'])