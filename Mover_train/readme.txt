activate Mover_train

train -> start training the cycleGan to generate logs 
python train.py --dataroot datasets/genderchange2

test -> to see generated result
python test.py --dataroot datasets/genderchange2 --generator_A2B logs/genderchange2@21.04.2022-19_01_42/100/netG_A2B.pth --generator_B2A logs/genderchange2@21.04.2022-19_01_42/100/netG_B2A.pth

plot -> combine all image into one plot
require you to activate Mover first
python plot.py