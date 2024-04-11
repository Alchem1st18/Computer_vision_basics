import cv2

img_path = 'C:/Users/Srikar/PycharmProjects/opencv_basics/data/birdd.jpg'
img = cv2.imread(img_path)

img_grey = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

res,t_img = cv2.threshold(img_grey,75,255,cv2.THRESH_BINARY)
tt_img = cv2.blur(t_img,(10,10))
res,tt_img = cv2.threshold(tt_img,75,255,cv2.THRESH_BINARY)
cv2.imshow('img_grey',img_grey)
cv2.imshow('img_thresh_no_blur',t_img)
cv2.imshow('img_thresh_blur',tt_img)
cv2.waitKey(0)