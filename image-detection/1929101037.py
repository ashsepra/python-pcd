import cv2
import numpy as np

# Reading image
# img_src = cv2.imread('./dataset/coins.jpg')
img_src = cv2.imread('./dataset/3.jpg')

# Reduce noise
img_blur = cv2.medianBlur(img_src, 11)

# Set to HSV
img_hsv = cv2.cvtColor(img_blur, cv2.COLOR_BGR2HSV)

# Detection red
# low_range = np.array([170, 50, 50], dtype=np.uint8)
# high_range = np.array([180, 255, 255], dtype=np.uint8)
# range_mask = cv2.inRange(img_hsv, low_range, high_range)
# output = cv2.bitwise_and(img_src, img_src, mask=range_mask)


# Detection green
# low_range = np.array([36, 25, 25], dtype=np.uint8)
# high_range = np.array([70, 255, 255], dtype=np.uint8)
# range_mask = cv2.inRange(img_hsv, low_range, high_range)
# output = cv2.bitwise_and(img_src, img_src, mask=range_mask)


# Detection brown
# low_range = np.array([10, 100, 20], dtype=np.uint8)
# high_range = np.array([20, 255, 200], dtype=np.uint8)
# range_mask = cv2.inRange(img_hsv, low_range, high_range)
# output = cv2.bitwise_and(img_src, img_src, mask=range_mask)


# Detection yellow
# low_range = np.array([20,100,100], dtype=np.uint8)
# high_range = np.array([45,255,255], dtype=np.uint8)
# range_mask = cv2.inRange(img_hsv, low_range, high_range)
# output = cv2.bitwise_and(img_src, img_src, mask=range_mask)


# Detection orange
# low_range = np.array([0,150,150]. dtype=np.uint8)
# high_range = np.array([20,255,255], dtype=np.uint8)
# range_mask = cv2.inRange(img_hsv, low_range, high_range)
# output = cv2.bitwise_and(img_src, img_src, mask=range_mask)

# Detection blue
low_range = np.array([100,150,0], dtype=np.uint8)
high_range = np.array([140,255,255], dtype=np.uint8)
range_mask = cv2.inRange(img_hsv, low_range, high_range)
# output = cv2.bitwise_and(img_src, img_src, mask=range_mask)

# Dilation
kernel_mask = np.ones((11, 11))
dilation = cv2.dilate(range_mask, kernel_mask, iterations=1)

contours, _ = cv2.findContours(dilation, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
number = str(len(contours))
print(number)

cv2.imshow('Original Image', img_blur)
cv2.imshow('Color Mask', dilation)

cv2.waitKey(0)
cv2.destroyAllWindows()