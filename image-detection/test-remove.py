import cv2
import numpy as np

img_src = cv2.imread('./dataset/1.jpg')

# Reduce noise
img_blur = cv2.medianBlur(img_src, 5)

mask = cv2.threshold(img_blur, 50, 255, cv2.THRESH_BINARY)[1][:, :, 0]
dst = cv2.inpaint(img_blur, mask, 7, cv2.INPAINT_NS)

# Set to HSV
img_hsv = cv2.cvtColor(dst, cv2.COLOR_BGR2HSV)
low_red = np.array([170, 50, 100])
high_red = np.array([180, 255, 255])
red_mask = cv2.inRange(img_hsv, low_red, high_red)


cv2.imshow('Original Image', img_blur)
cv2.imshow('Red Mask', red_mask)

cv2.waitKey(0)
cv2.destroyAllWindows()