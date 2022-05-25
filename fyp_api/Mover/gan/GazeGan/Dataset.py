from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()
from IMLib.utils import *

class Dataset(object):
#C:\Users\mevin\fyp_project3\Mover\upload_img\input\A
    def __init__(self, config):
        super(Dataset, self).__init__()

        self.data_dir = config.data_dir
        #self.dataset_name = 'NewGazeData'
        self.dataset_name = 'upload_img'
        #self.dataset_name = 'C:/Users/mevin/fyp_project3/Mover/upload_img/input/'
        #self.attr_0_txt = 'eye_train.txt'
        #self.attr_1_txt = 'eye_test.txt'
        #C:\Users\mevin\fyp_project3\Mover\logs\eyemovement
        #self.attr_1_txt = 'C:/Users/mevin/fyp_project3/Mover/logs/eyemovement/eye_test.txt'
        #current_dict=os.getcwd()
        #print("current dict" , current_dict)
        #Detect img location
        self.attr_1_txt = '\logs\eyemovement\eye_test.txt'
        #list of train eye location
        self.attr_2_txt = '\logs\eyemovement\eye_test2.txt'
        #all_dict = current_dict + self.attr_1_txt
        #print("all dict" , all_dict)
        self.height, self.width= config.img_size, config.img_size
        self.channel = config.output_nc
        self.capacity = config.capacity
        self.batch_size = config.batch_size
        self.num_threads = config.num_threads

        self.train_images_list, self.train_eye_pos, self.test_images_list, self.test_eye_pos, self.test_num = self.readfilenames()

    def readfilenames(self):

        train_eye_pos = []
        train_images_list = []
        #fh = open(os.path.join(self.data_dir, self.attr_0_txt))

        #for f in fh.readlines():
        #    eye_pos = []
        #    f = f.strip('\n')
        #    filenames = f.split(' ', 5)
        #    if os.path.exists(os.path.join(self.data_dir, "1/"+filenames[0]+".jpg")):
        #        train_images_list.append(os.path.join(self.data_dir, "1/"+filenames[0]+".jpg"))
        #        eye_pos.extend([int(value) for value in filenames[1:5]])
        #        train_eye_pos.append(eye_pos)

        #fh.close()

        current_dict=os.getcwd()
        print("current dict" , current_dict)
        all_dict = current_dict + self.attr_1_txt
        all_dict2 = current_dict + self.attr_2_txt
        
        #fh = open(os.path.join(self.data_dir, self.attr_1_txt))
        fh = open(os.path.join(self.data_dir, all_dict))
        fh2 = open(os.path.join(self.data_dir, all_dict2))
        test_images_list = []
        test_eye_pos = []
        #print("start",test_eye_pos)
        for f in fh2.readlines():
            eye_pos = []
            f = f.strip('\n')
            filenames = f.split(' ', 5)
 
            if os.path.exists(os.path.join(self.data_dir, "A/"+filenames[0]+".jpg")):
                test_images_list.append(os.path.join(self.data_dir,"A/"+filenames[0]+".jpg"))
                eye_pos.extend([int(value) for value in filenames[1:5]])
                test_eye_pos.append(eye_pos)
              
            if os.path.exists(os.path.join(self.data_dir, "A/"+filenames[0]+".png")):
                test_images_list.append(os.path.join(self.data_dir,"A/"+filenames[0]+".png"))
                eye_pos.extend([int(value) for value in filenames[1:5]])
                test_eye_pos.append(eye_pos)
    

        fh2.close()
        #print("1st",test_eye_pos)
        
        

        for f in fh.readlines():
            eye_pos = []
            f = f.strip('\n')
            filenames = f.split(' ', 5)

            if os.path.exists(os.path.join(self.data_dir, "A/"+filenames[0]+".jpg")):
                test_images_list.append(os.path.join(self.data_dir,"A/"+filenames[0]+".jpg"))
                eye_pos.extend([int(value) for value in filenames[1:5]])
                test_eye_pos.append(eye_pos)
                
            if os.path.exists(os.path.join(self.data_dir, "A/"+filenames[0]+".png")):
                test_images_list.append(os.path.join(self.data_dir,"A/"+filenames[0]+".png"))
                eye_pos.extend([int(value) for value in filenames[1:5]])
                test_eye_pos.append(eye_pos)

        fh.close()
        #print("2nd",test_eye_pos)
        
        
        
        return train_images_list, train_eye_pos, test_images_list, test_eye_pos, len(test_images_list)

    def read_images(self, input_queue):

        content = tf.read_file(input_queue)
        image = tf.image.decode_jpeg(content, channels=self.channel)
        image = tf.cast(image, tf.float32)
        image = tf.image.resize_images(image, size=(self.height, self.width))

        return image / 127.5 - 1.0

    def input(self):

        train_images = tf.convert_to_tensor(self.train_images_list, dtype=tf.string)
        train_eye_pos = tf.convert_to_tensor(self.train_eye_pos, dtype=tf.int32)
        train_queue = tf.train.slice_input_producer([train_images, train_eye_pos], shuffle=True)
        train_eye_pos_queue = train_queue[1]
        train_images_queue = self.read_images(input_queue=train_queue[0])

        test_images = tf.convert_to_tensor(self.test_images_list, dtype=tf.string)
        test_eye_pos = tf.convert_to_tensor(self.test_eye_pos, dtype=tf.int32)
        test_queue = tf.train.slice_input_producer([test_images, test_eye_pos], shuffle=False)
        test_eye_pos_queue = test_queue[1]
        test_images_queue = self.read_images(input_queue=test_queue[0])

        batch_path, batch_image1, batch_eye_pos1 = tf.train.shuffle_batch([train_queue[0], train_images_queue, train_eye_pos_queue],
                                                batch_size=self.batch_size,
                                                capacity=self.capacity,
                                                num_threads=self.num_threads,
                                                min_after_dequeue=1000
                                                )

        batch_image2, batch_eye_pos2 = tf.train.batch([test_images_queue, test_eye_pos_queue],
                                                batch_size=self.batch_size,
                                                capacity=500,
                                                num_threads=1
                                                )

        return batch_path, batch_image1, batch_eye_pos1, batch_image2, batch_eye_pos2
