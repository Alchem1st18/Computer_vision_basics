import cv2

#read file
image_path = 'C:/Users/Srikar/PycharmProjects/opencv_basics/data/birdd.jpg'
img = cv2.imread(image_path)
print(img.shape)

#cropping
crop_img = img[20:300,120:700]

#visualize image
cv2.imshow('img1',img)
cv2.imshow('img2',crop_img)
cv2.waitKey(0)