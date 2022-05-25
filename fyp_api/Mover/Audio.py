#1)Clear all output
#2)Select a sound to generate a video
#3)Clear input
import subprocess
import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--audio', type=int, default='0', help='audio[1-6]')
opt = parser.parse_args()
print(opt.audio)
sound=opt.audio

print('Clear all ouput Images')
subprocess.call(['python', 'util/DeleteOutputImg.py'])

#Generate a video using each sound
if sound==1:
  print('cartoon_bye sound')
  subprocess.call(['python', 'gan/TGan/run.py', '--audio', '1'])
elif sound==2:
  print('cartoon_hello sound')
  subprocess.call(['python', 'gan/TGan/run.py', '--audio', '2'])
elif sound==3:
  print('man_bye sound')
  subprocess.call(['python', 'gan/TGan/run.py', '--audio', '3'])
elif sound==4:
  print('man_hello sound')
  subprocess.call(['python', 'gan/TGan/run.py', '--audio', '4'])
elif sound==5:
  print('woman_bye sound')
  subprocess.call(['python', 'gan/TGan/run.py', '--audio', '5'])
elif sound==6:
  print('woman_hello sound')
  subprocess.call(['python', 'gan/TGan/run.py', '--audio', '6'])
else:
  print("no other selection")
  
print('clear input')
subprocess.call(['python', 'util/DeleteInputImg.py'])