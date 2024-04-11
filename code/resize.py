import cv2

#read image
image_path = 'C:/Users/Srikar/PycharmProjects/opencv_basics/data/birdd.jpg'
img = cv2.imread(image_path)
print(img.shape)
#resize image
new_image = cv2.resize(img,(600,600))

#visualize image
cv2.imshow('img1',img)
cv2.imshow('img2',new_image)
cv2.waitKey(0)