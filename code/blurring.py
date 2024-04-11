import cv2

img_path = 'C:/Users/Srikar/PycharmProjects/opencv_basics/data/worker.jpg'
img = cv2.imread(img_path)

k = 51
blur_img = cv2.blur(img,(k,k))
gauss_img = cv2.GaussianBlur(img,(k,k),9)
median_img = cv2.medianBlur(img,k)  #i feeel this is used to smoothen out images very well

cv2.imshow('img',img)
cv2.imshow('img1',blur_img)
cv2.imshow('img2',gauss_img)
cv2.imshow('img3',median_img)
cv2.waitKey()
