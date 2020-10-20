import os 
import cv2 

target_size = 15 # KB
path_img = '/User/Drive/Folder/Image.jpg'

print(os.path.getsize(path_img)//1024, 'KB')
img = cv2.imread(path_img)
temp = img
temp_path = './temp.jpg'
cv2.imwrite(temp_path, img)
print('Original shape = ',temp.shape)

height = temp.shape[0]
width = temp.shape[1]

while os.path.getsize(temp_path)//1024 > target_size:
    temp = cv2.resize(img, (width, height))
    cv2.imwrite(temp_path, temp)
    print(os.path.getsize(temp_path)//1024, f'KB == ({height},{width})')
    height = int(height * 0.9)
    width = int(width * 0.9)
