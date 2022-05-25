import os
os.environ['KMP_DUPLICATE_LIB_OK']='True'
from os import path
from pydub import AudioSegment
import sda
import scipy.io.wavfile as wav
from PIL import Image
import numpy as np
import cv2
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--audio', type=int, default='0', help='audio[1-6]')
opt = parser.parse_args()
print(opt.audio)
sound=opt.audio

if sound==1:
  audio_path = "gan/TGan/audio/cartoon_bye.wav"
  print('cartoon_bye')
elif sound==2:
  audio_path = "gan/TGan/audio/cartoon_hello.wav"
  print('cartoon_hello')
elif sound==3:
  audio_path = "gan/TGan/audio/man_bye.wav"
  print('man_bye')
elif sound==4:
  audio_path = "gan/TGan/audio/man_hello.wav"
  print('man_hello')
elif sound==5:
  audio_path = "gan/TGan/audio/woman_bye.wav"
  print('woman_bye')
elif sound==6:
  audio_path = "gan/TGan/audio/woman_hello.wav"
  print('woman_hello')
else:
  print("no other selection")
  
#original = 'C:/Users/mevin/fyp_project3/Mover/upload_img/input/A/'
original = 'upload_img/input/A/'

#check image name in dict
for images in os.listdir(original):
  if(images.endswith(".png") or images.endswith(".jpg")):
    print(images)


if __name__ == "__main__":
    #image_path = "C:/Users/mevin/fyp_project3/Mover/upload_img/input/A/"+images
    #output_path = "C:/Users/mevin/fyp_project3/Mover/list/output/movie.mp4"
    image_path = "upload_img/input/A/"+images
    output_path = "list/output/movie.mp4"
    
    
    va = sda.VideoAnimator(gpu=-1, model_path="timit")
    fs, audio_clip = wav.read(audio_path)
    still_frame = Image.open(image_path)
    vid, aud = va(np.array(still_frame), audio_clip, fs=fs)
    
    # model for increasing resolution
    sr = cv2.dnn_superres.DnnSuperResImpl_create()
    sr.readModel("gan/TGan/ESPCN_x4.pb")
    sr.setModel("espcn", 4)
    
    # increase the resolution of the images
    vid_superres = []
    for i in range(len(vid)):
        img_shape = vid[i].shape
        img = vid[i]
        img = np.zeros((img_shape[1], img_shape[2], img_shape[0]), dtype=np.uint8)
        for channel in range(img_shape[0]):
            for row in range(img_shape[1]):
                for col in range(img_shape[2]):
                    img[row][col][channel] = vid[i][channel][row][col]
        img = np.array(Image.fromarray(img, "RGB"))
        
        result = sr.upsample(img)
        
        img_shape = np.array(result).shape
        img_result = np.zeros((img_shape[2], img_shape[0], img_shape[1]), dtype=np.uint8)
        for row in range(img_shape[0]):
            for col in range(img_shape[1]):
                for channel in range(img_shape[2]):
                    img_result[channel][row][col] = result[row][col][channel]
        vid_superres.append(img_result)
    va.save_video(np.array(vid_superres), aud, output_path)