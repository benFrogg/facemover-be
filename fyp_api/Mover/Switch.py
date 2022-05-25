#Features
#Animated Facial Expression 1
#Animated Eye Movement 2
#Gender Customization 3-4
#Face Aging 5-6
#Anime-Style Image 7
#Producing Audio 8-13

import argparse
import subprocess
import sys

parser = argparse.ArgumentParser()
parser.add_argument('--mode', type=int, default='0', help='feature[1-7]')
opt = parser.parse_args()
print(opt.mode)
feature=opt.mode

if feature==1:
 print('Animated Facial Expression')
 subprocess.call(['python', 'Expression.py'])
elif feature==2:
 print('Animated Eye Movement')
 subprocess.call(['python', 'EyeMovement.py'])
elif feature==3:
 print('Gender Customization m->f')
 subprocess.call(['python', 'GenderCustomization.py', '--type', 'f'])
elif feature==4:
 print('Gender Customization f->m')
 subprocess.call(['python', 'GenderCustomization.py', '--type', 'm'])
elif feature==5:
 print('Face Aging y->o')
 subprocess.call(['python', 'FaceAging.py', '--type', 'o'])
elif feature==6:
 print('Face Aging o->y')
 subprocess.call(['python', 'FaceAging.py', '--type', 'y'])
elif feature==7:
 print('Anime-Style Image')
 subprocess.call(['python', 'ConvertCartoon.py'])
elif feature==8:
 print('Producing Audio cartoon_bye')
 subprocess.call(['python', 'Audio.py', '--audio', '1'])
elif feature==9:
 print('Producing Audio cartoon_hello')
 subprocess.call(['python', 'Audio.py', '--audio', '2'])
elif feature==10:
 print('Producing Audio man_bye')
 subprocess.call(['python', 'Audio.py', '--audio', '3'])
elif feature==11:
 print('Producing Audio man_hello')
 subprocess.call(['python', 'Audio.py', '--audio', '4'])
elif feature==12:
 print('Producing Audio woman_bye')
 subprocess.call(['python', 'Audio.py', '--audio', '5'])
elif feature==13:
 print('Producing Audio woman_hello')
 subprocess.call(['python', 'Audio.py', '--audio', '6'])
else:
  print('error')
