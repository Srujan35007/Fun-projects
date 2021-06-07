import cv2 
import numpy as np 
import matplotlib.pyplot as plt 
import tkinter
from tqdm import tqdm
from scipy.optimize import curve_fit

def f(x, a,b,c,d,e):
    return a*(x**4) + b*(x**3) + c*(x**2) + d*(x**1) + e

thresh = 100
img = cv2.imread('./a.jpg')

# Preprocess image for easier compute
img = np.asarray(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY))
img[img>thresh] = 0
print(img.shape)
width = img.shape[1]
height = img.shape[0]
if width > 500 or height > 500:
    if width > height:
        new_height = int(height/(width/500))
        img = cv2.resize(img, (500,new_height))
    if height > width:
        new_width = int(width/(height/500))
        img = cv2.resize(img, (new_width, 500))
    print(f'Image resized to {img.shape}')

# Get the raw graph
points_raw = []
row_count = 0
print(f'Processing image data')
for row in tqdm(reversed(img)):
    col_count = 0
    for elem in row:
        if elem != 0:
            points_raw.append((col_count, row_count))
        col_count += 1
    row_count += 1

xs_raw = [raw[0] for raw in points_raw]
xs_ = sorted(list(set(xs_raw)))

# Clean the data
points = []
print('Cleaning datapoints')
for i in tqdm(range(len(xs_))):
    temp_ys = []
    for j in range(len(points_raw)):
        if points_raw[j][0] == xs_[i]:
            temp_ys.append(points_raw[j][1])
    points.append((xs_[i], np.average(temp_ys)))

# Fit Curve
xs = [point[0] for point in points]
ys = [point[1] for point in points]
ys = ys/max(ys)
params, foo = curve_fit(f, xs, ys)
print('Curve fitting done')

# Plot for checking accuracy
new_xs = [i for i in range(len(xs))]
new_ys = [f(i, *params) for i in new_xs]
plt.scatter(xs,ys,0.5,color='r')
plt.plot(new_xs, new_ys, linewidth=0.9,color='b')
plt.show()

# Print the function
func = ''
for i in range(len(params)):
    max_pow = len(params)-1
    if i != len(params)-1:
        func += f'({round(params[i], 8)}*x**{max_pow-i})+'
    elif i == len(params)-1:
        func += f'({round(params[i],8)})'

print(f'The function with parameters rounded to 8 decimal places and the output nomalized [0,1]:')
print(func)
