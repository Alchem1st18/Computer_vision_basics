import cv2

img_path = 'C:/Users/Srikar/PycharmProjects/opencv_basics/data/whiteboard.jpg'
img = cv2.imread(img_path)
print(img.shape)

cv2.line(img,(100,150),(350,400),(255,0,0),5)
cv2.rectangle(img,(250,250),(370,370),(0,255,0),7)
cv2.circle(img,(200,200),27,(0,0,255),2)
cv2.putText(img,'Cold hours!!',(200,250),cv2.FONT_HERSHEY_PLAIN,5,(0,0,0),2)
cv2.imshow('img',img)
cv2.waitKey(0)
