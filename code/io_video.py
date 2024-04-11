import os

import cv2

#read video
video_path = 'C:/Users/Srikar/PycharmProjects/opencv_basics/data/2436088-uhd_3840_2160_25fps.mp4'
vid = cv2.VideoCapture(video_path)

#visualize video
ret = True
while ret:
    ret,frame = vid.read()
    if(ret):
        cv2.imshow('frame',frame)
        cv2.waitKey(40) # i.e wait 40 ms [for a 25frame/sec video]

vid.release()
cv2.destroyAllWindows()

