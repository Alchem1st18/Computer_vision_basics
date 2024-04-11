import cv2

img_loc = 'C:/Users/Srikar/PycharmProjects/opencv_basics/data/flying.jpg'
img = cv2.imread(img_loc)

img_grey = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
res,img_thresh = cv2.threshold(img_grey,130,255,cv2.THRESH_BINARY_INV)

contours,hirarchy = cv2.findContours(img_thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

for c in contours:
    if(cv2.contourArea(c)>200):
        #cv2.drawContours(img,c,-1,(255,0,0),4)
        x,y,w,h = cv2.boundingRect(c)
        #line = ((w*w)+(h*h))**0.5
        #radius = line/2
        #cx = int(x+radius)
        #cy = int(y+radius)
        #cv2.circle(img,(cx,cy),int(radius),(0,255,0),2)
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)

cv2.imshow('img',img)
cv2.imshow('img_grey',img_grey)
cv2.imshow('img_thresh',img_thresh)
cv2.waitKey(0)