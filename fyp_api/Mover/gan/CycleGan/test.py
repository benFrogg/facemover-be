#!/usr/bin/python3
import argparse
import sys
import os
import glob

import torchvision.transforms as transforms
from torchvision.utils import save_image
from PIL import Image

from torch.utils.data import DataLoader
from torch.autograd import Variable
import torch

from models.generator import Generator
from datasets import ImageDataset


parser = argparse.ArgumentParser()
parser.add_argument('--batchSize', type=int, default=1, help='size of the batches')
parser.add_argument('--dataroot', type=str, default='upload_img/input', help='root directory of the dataset')
parser.add_argument('--input_nc', type=int, default=3, help='number of channels of input data')
parser.add_argument('--output_nc', type=int, default=3, help='number of channels of output data')
parser.add_argument('--size', type=int, default=256, help='size of the data (squared assumed)')
parser.add_argument('--cuda', action='store_true', help='use GPU computation')
parser.add_argument('--n_cpu', type=int, default=0, help='number of cpu threads to use during batch generation')
parser.add_argument('--generator_B2A', type=str, default='logs/genderchange@31.03.2022-11_02_55/200/netG_B2A.pth', help='B2A generator checkpoint file')
parser.add_argument('--order', type=int, default=0, help='image order')
opt = parser.parse_args()
print(opt)

if torch.cuda.is_available() and not opt.cuda:
    print("WARNING: You have a CUDA device, so you should probably run with --cuda")
     
###### Definition of variables ######
# Networks
netG_B2A = Generator(opt.output_nc, opt.input_nc)

if opt.cuda:
    netG_B2A.cuda()

# Load state dicts
netG_B2A.load_state_dict(torch.load(opt.generator_B2A, map_location=torch.device('cpu')))

# Set model's test mode
netG_B2A.eval()

# Inputs & targets memory allocation
Tensor = torch.cuda.FloatTensor if opt.cuda else torch.Tensor
input_A = Tensor(opt.batchSize, opt.input_nc, opt.size, opt.size)

# Dataset loader
transforms_ = [transforms.Resize((opt.size, opt.size), Image.BICUBIC),
                transforms.ToTensor(),
                transforms.Normalize((0.5,0.5,0.5), (0.5,0.5,0.5))]
dataloader = DataLoader(ImageDataset(opt.dataroot, transforms_=transforms_, mode='input'), 
                        batch_size=opt.batchSize, shuffle=False, num_workers=opt.n_cpu)

print("order")
order_no=int(opt.order)
print("order", order_no)

for i, batch in enumerate(dataloader):
    # Set model input
    real_A = Variable(input_A.copy_(batch['A']))

    # Generate output base on model
    fake_A = 0.5*(netG_B2A(real_A).data + 1.0)
    
    #save the img
    save_image(fake_A, 'list/output/%04d.png' % (order_no+i))
    print("success")

    sys.stdout.write('\rGenerated images %04d of %04d' % (order_no+i, len(dataloader)))

sys.stdout.write('\n')
