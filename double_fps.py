'''
Author: Suddala Srujan

Step1: Extract and store individual frames in a temp folder

Step2: Iterate through the frames and store the averages of RGB values of
        adjacent frames between the original frames

Step3: Make the new video with double the FPS
'''
import os
from tqdm import tqdm
from decord import cpu, VideoReader
import cv2
import numpy as np
import matplotlib.pyplot as plt
print(f'Imports complete.')

OUT_FILE = '/home/srujan/Projects/testvid_double.mkv'
VID_PATH = '/home/srujan/Projects/testvid.mkv'

vr = VideoReader(VID_PATH, ctx = cpu(0))
ORIG_FPS = vr.get_avg_fps()
FINAL_FPS = 2*ORIG_FPS
print(f'Original FPS of the video = {ORIG_FPS}')
print(f'Final FPS of the video = {FINAL_FPS}')

height, width = vr[0].asnumpy().shape[0], vr[0].asnumpy().shape[1]
fourcc = cv2.VideoWriter_fourcc(*"mp4v")
out = cv2.VideoWriter(OUT_FILE, fourcc, FINAL_FPS,(width, height))

for i in tqdm(range(len(vr))):
    try:
        frame1 = cv2.cvtColor(vr[i].asnumpy(), cv2.COLOR_BGR2RGB)
        frame2 = cv2.cvtColor(vr[(i+1)].asnumpy(), cv2.COLOR_BGR2RGB)
        frame_avg = frame1//2 + frame2//2
        frame_avg[frame_avg > 254] = 254
        if i == 0:
            out.write(frame1)
        else:
            pass
        out.write(frame_avg)
        out.write(frame2)
    except:
        pass

del vr
out.release()
