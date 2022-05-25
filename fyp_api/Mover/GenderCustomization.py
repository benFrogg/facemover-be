#1)Clear all output
#2)Generate eye correction Images
#3)Select a gender to generate a female or male image using model with epoch 120
#4)Select a gender to generate a female or male image using model with epoch 160
#5)Select a gender to generate a female or male image using model with epoch 200
#6)Move orginal Image to output folder
#7)Resize all output Image
#8)Convert all output Image to GIF

import argparse
import subprocess
import sys

parser = argparse.ArgumentParser()
parser.add_argument('--type', type=str, default='f', help='gender f is m2f or m is f2m')
opt = parser.parse_args()
print(opt.type)
gender=opt.type

print('Clear all ouput Images')
subprocess.call(['python', 'util/DeleteOutputImg.py'])

#male to female
if gender=='f':
  #weight for this model is 120 epoch
  print('Generate female Images using weight 1')
  subprocess.call(['python', 'gan/CycleGan/test.py', 
                  '--dataroot', 'upload_img',
                  '--generator_B2A', 'logs/genderchange2@21.04.2022-19_01_42/42/netG_A2B.pth',                 
                  '--order', '1',
  ])
  #weight for this model is 160 epoch
  print('Generate female Images using weight 2')
  subprocess.call(['python', 'gan/CycleGan/test.py', 
                  '--dataroot', 'upload_img',
                  '--generator_B2A', 'logs/genderchange2@21.04.2022-19_01_42/88/netG_A2B.pth',
                  '--order', '2',
  ])
  #weight for this model is 200 epoch
  print('Generate female Images using weight 3')
  subprocess.call(['python', 'gan/CycleGan/test.py', 
                  '--dataroot', 'upload_img',
                  '--generator_B2A', 'logs/genderchange2@21.04.2022-19_01_42/93/netG_A2B.pth',
                  '--order', '3',
  ])

#female to male
elif gender=='m':
  #weight for this model is 120 epoch
  print('Generate male Images using weight 1')
  subprocess.call(['python', 'gan/CycleGan/test.py', 
                  '--dataroot', 'upload_img',
                  '--generator_B2A', 'logs/genderchange2@21.04.2022-19_01_42/42/netG_B2A.pth',
                  '--order', '1',
  ])
  #weight for this model is 160 epoch
  print('Generate male Images using weight 2')
  subprocess.call(['python', 'gan/CycleGan/test.py', 
                  '--dataroot', 'upload_img',
                  '--generator_B2A', 'logs/genderchange2@21.04.2022-19_01_42/88/netG_B2A.pth',
                  '--order', '2',
  ])
  #weight for this model is 200 epoch
  print('Generate male Images using weight 3')
  subprocess.call(['python', 'gan/CycleGan/test.py', 
                  '--dataroot', 'upload_img',
                  '--generator_B2A', 'logs/genderchange2@21.04.2022-19_01_42/93/netG_B2A.pth',
                  '--order', '3',
  ])
  
print('Move orginal Image to output folder')
subprocess.call(['python', 'util/MoveInputImg.py'])

print('Resize all output Image')
subprocess.call(['python', 'util/ResizeOutputImg.py'])

print('Convert all output Image to GIF')
subprocess.call(['python', 'util/ConvertToGif.py'])
