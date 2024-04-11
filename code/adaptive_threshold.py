import cv2

img_path = 'C:/Users/Srikar/PycharmProjects/opencv_basics/data/news.jpg'
img = cv2.imread(img_path)

img_grey = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

res,t_img = cv2.threshold(img_grey,90,255,cv2.THRESH_BINARY)
threshh = cv2.adaptiveThreshold(img_grey,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,21,31)



cv2.imshow('img_thresh_global',t_img)
cv2.imshow('img_thresh_adaptive',threshh)
cv2.waitKey(0)