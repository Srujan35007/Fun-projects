import cv2 
import numpy as np 

size = 100
img = cv2.imread('./a.jpg')
img = cv2.resize(img, (size,size))
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img = np.asarray(img)

# char_map = '@#+:.'
char_map = '.:+#@'
def get_char(pixel_val):
    return char_map[int(pixel_val//(256/len(char_map)))]

lines = []
for line in img:
    temp_line = ''
    for val in line:
        temp_line += (get_char(val) + ' ')
    lines.append(temp_line + '\n')

with open('./img.txt', 'wt') as foo:
    for line in lines:
        foo.writelines(line)
