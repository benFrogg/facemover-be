#1)Clear all output
#2)Generate eye correction Images
#3)Move orginal Image to output folder
#4)Resize all output Image
#5)Convert all output Image to GIF

import argparse
import subprocess
import sys

print('Clear all ouput Images')
subprocess.call(['python', 'util/DeleteOutputImg.py'])

print('update eye_test.txt base on input img')
subprocess.call(['python', 'gan/GazeGan/eye_location.py'])

print('Generate eye correction Images')
subprocess.call(['python', 'gan/GazeGan/test.py', 
                '--gpu_id', '0',
                '--exper_name', 'list',                 
                '--batch_size', '1',
                '--test_sample_dir', 'output'
])

print('Move orginal Image to output folder')
subprocess.call(['python', 'util/MoveInputImg.py'])

print('Resize all output Image')
subprocess.call(['python', 'util/ResizeOutputImg.py'])

print('Convert all output Image to GIF')
subprocess.call(['python', 'util/ConvertToGif.py'])