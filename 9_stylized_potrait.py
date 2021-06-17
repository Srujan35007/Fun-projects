import os 
import time 
import cv2 
from tqdm import tqdm 
from argparse import ArgumentParser as AP 
import numpy as np 
import random
import matplotlib.pyplot as plt
print('Imports complete')

PROB = 0.999
THRESH = 30
BOX_H = 200
BOX_V = 200
RATIO = 1.1

parser = AP()
parser.add_argument("image_file_path")
args = parser.parse_args()

file_path = args.image_file_path 
image = cv2.imread(file_path)
orig_w, orig_h = image.shape[:2]
image = np.asarray(cv2.cvtColor(image, cv2.COLOR_BGR2GRAY))
image[image<THRESH] = 0 
image = cv2.resize(image, (int(orig_h/RATIO), int(orig_w/RATIO)))
black_canvas = np.zeros_like(np.asarray(image))

for row in tqdm(range((image.shape[0]))):
    for column in range((image.shape[1])):
        try:
            if random.random() > PROB:
                start_point_y = random.choice([foo for foo in range(row-BOX_V, row)])
                start_point_x = random.choice([foo for foo in range(column-BOX_H, column+BOX_H)])
                end_point_y = random.choice([foo for foo in range(row, row+BOX_V)])
                end_point_x = random.choice([foo for foo in range(column-BOX_H, column+BOX_H)])
                weight = int(image[row][column]/255*10)//2
                color_ = [int(image[row][column])]*3
                cv2.line(black_canvas, (start_point_x, start_point_y), (end_point_x, end_point_y),
                        color_, weight)
            else:
                pass
        except:
            pass 
plt.imshow(black_canvas)
plt.show()
plt.imsave('test.jpg', black_canvas)
