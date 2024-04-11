import os

import cv2

#read data
#image_path = os.path.join('.','data','tiger.jpg')
image_path = 'C:/Users/Srikar/PycharmProjects/opencv_basics/data/tiger.jpg'
img = cv2.imread(image_path)

#write data
cv2.imwrite('C:/Users/Srikar/PycharmProjects/opencv_basics/data/new_tiger.jpg',img)

#visualize data
cv2.imshow('image',img)
cv2.waitKey(0)
