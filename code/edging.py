import cv2
import numpy as np

img_path = 'C:/Users/Srikar/PycharmProjects/opencv_basics/data/cric.jpg'
img = cv2.imread(img_path)

img_edge = cv2.Canny(img,150,220)
img_edge_d = cv2.dilate(img_edge,np.ones((4,4),dtype = np.int8))
img_edge_e = cv2.erode(img_edge_d,np.ones((2,2),dtype = np.int8))

# cv2.imshow('img',img)
cv2.imshow('img_edge',img_edge)
cv2.imshow('img_edge_d',img_edge_d)
cv2.imshow('img_edge_e',img_edge_e)



cv2.waitKey(0)