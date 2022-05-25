#1)Clear all output
#2)Generate eye correction Images
#3)Select an age to generate a old or young image using model with epoch 60
#4)Select an age to generate a old or young image using model with epoch 200
#5)Select an age to generate a old or young image using model with epoch 220
#6)Move orginal Image to output folder
#7)Resize all output Image
#8)Convert all output Image to GIF

import argparse
import subprocess
import sys

parser = argparse.ArgumentParser()
parser.add_argument('--type', type=str, default='o', help='aging o is young 2 old or y is old 2 young')
opt = parser.parse_args()
print(opt.type)
age=opt.type

print('Clear all ouput Images')
subprocess.call(['python', 'util/DeleteOutputImg.py'])

#young to old
if age=='o':
  #weight for this model is 60 epoch
  print('Generate old Images using weight 1')
  subprocess.call(['python', 'gan/CycleGan/test.py', 
                  '--dataroot', 'upload_img',
                  '--generator_B2A', 'logs/aging@12.04.2022-14_01_12/60/netG_A2B.pth',                 
                  '--order', '1',
  ])
  #weight for this model is 200 epoch
  print('Generate old Images using weight 2')
  subprocess.call(['python', 'gan/CycleGan/test.py', 
                  '--dataroot', 'upload_img',
                  '--generator_B2A', 'logs/aging@12.04.2022-14_01_12/200/netG_A2B.pth',                 
                  '--order', '2',
  ])
  #weight for this model is 220 epoch
  print('Generate old Images using weight 3')
  subprocess.call(['python', 'gan/CycleGan/test.py', 
                  '--dataroot', 'upload_img',
                  '--generator_B2A', 'logs/aging@12.04.2022-14_01_12/220/netG_A2B.pth',
                  '--order', '3',
  ])

#old to young
elif age=='y':
  #weight for this model is 60 epoch
  print('Generate young Images using weight 1')
  subprocess.call(['python', 'gan/CycleGan/test.py', 
                  '--dataroot', 'upload_img',
                  '--generator_B2A', 'logs/aging@12.04.2022-14_01_12/60/netG_B2A.pth',                 
                  '--order', '1',
  ])
  #weight for this model is 200 epoch
  print('Generate young Images using weight 2')
  subprocess.call(['python', 'gan/CycleGan/test.py', 
                  '--dataroot', 'upload_img',
                  '--generator_B2A', 'logs/aging@12.04.2022-14_01_12/200/netG_B2A.pth',
                  '--order', '2',
  ])
  #weight for this model is 220 epoch
  print('Generate young Images using weight 3')
  subprocess.call(['python', 'gan/CycleGan/test.py', 
                  '--dataroot', 'upload_img',
                  '--generator_B2A', 'logs/aging@12.04.2022-14_01_12/220/netG_B2A.pth',
                  '--order', '3',
  ])
  
print('Move orginal Image to output folder')
subprocess.call(['python', 'util/MoveInputImg.py'])

print('Resize all output Image')
subprocess.call(['python', 'util/ResizeOutputImg.py'])

print('Convert all output Image to GIF')
subprocess.call(['python', 'util/ConvertToGif.py'])
  