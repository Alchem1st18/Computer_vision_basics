import os

import cv2

image_path = 'C:/Users/Srikar/PycharmProjects/opencv_basics/data/birdd.jpg'
img = cv2.imread(image_path)

diff_img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
grey_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
hsv_img = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

cv2.imshow('img',img)
cv2.imshow('img1',diff_img)
#cv2.imshow('img2',grey_img)
#cv2.imshow('img3',hsv_img)
cv2.waitKey(0)
