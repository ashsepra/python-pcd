# Author I Putu Ashadi Sedana Pratama
# Email: ashsepra@gmail.com
# This file contains pointwise image processing using an opencv-python package
# pointwise image processing described as 3 main processes such as arithmetic, geometry, and scaling

import cv2

# Get image from "images" directory
# I'm using Lenna file for example
file_img = './images/Lenna.png'
img_src = cv2.imread(file_img)
img_height = img_src.shape[0]
img_width = img_src.shape[1]
column_length = img_height - 1
row_length = img_width - 1

# Doing combine image processing with scalar value
scalar_value = 35
img_combine = img_src.copy()
for x in range(0, img_width) :
  for y in range(0, img_height) :
    img_combine[x, y] = scalar_value + img_src[x, y]

# Doing negative image processing
img_negative = img_src.copy()
for x in range(0, img_width) :
  for y in range(0, img_height) :
    img_negative[x, y] = 255 - img_src[x, y]

# Doing rotation image processing 90 degree
img_rotation = img_src.copy()
for x in range(0, img_width) :
  for y in range(0, img_height) :
    img_rotation[x, y] = img_src[column_length - y, x]

# Doing flip vertical image processing
img_flip = img_src.copy()
for x in range(0, img_width) :
  for y in range(0, img_height) :
    img_flip[x, y] = img_src[row_length - x, y]

# Doing zoom in image processing with 2 scale
img_zoom_out = cv2.resize(img_src, (2*img_width, 2*img_height))
m = 0
n = 0
for x in range(0, img_width) :
  for y in range(0, img_height) :
    img_zoom_out[m, n] = img_src[x, y]
    img_zoom_out[m, n + 1] = img_src[x, y]
    img_zoom_out[m + 1, n] = img_src[x, y]
    img_zoom_out[m + 1, n + 1] = img_src[x, y]
  m += 2
  n = 0

cv2.imshow('test', img_zoom_out)

cv2.waitKey(0)
cv2.destroyAllWindows()