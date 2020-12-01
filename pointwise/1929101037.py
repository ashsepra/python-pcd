# Author I Putu Ashadi Sedana Pratama
# Email: ashsepra@gmail.com
# This file contains pointwise image processing using an opencv-python package
# pointwise image processing described as 3 main processes such as arithmetic, geometry, and scaling

from cv2 import cv2
import numpy as np

# Get image from "images" directory
# I'm using Lenna file for example
file_img = './images/Lenna.png'
img_src = cv2.imread(file_img)
img_height = img_src.shape[0]
img_width = img_src.shape[1]
column_length = img_height - 1
row_length = img_width - 1

# Doing combine image processing with scalar value
scalar_value = -50
img_combine = img_src.copy()
# for x in range(0, img_width) :
#   for y in range(0, img_height) :
#     (b, g, r) = img_src[x, y]
#     bnew = scalar_value + b
#     gnew = scalar_value + g
#     rnew = scalar_value + r
#     print(b, g, r, bnew, gnew, rnew)
#     img_combine[x, y] = (bnew, gnew, rnew)

img_combine = cv2.add(img_src, scalar_value)
cv2.imwrite('./images/pointwise/Lenna-Add-Scalar.png', img_combine)

# Doing negative image processing
# img_negative = img_src.copy()
img_negative = np.zeros((img_width, img_height, 3), dtype = "uint8")
for x in range(0, img_width) :
  for y in range(0, img_height) :
    img_negative[x, y] = 255 - img_src[x, y]

cv2.imwrite('./images/pointwise/Lenna-Negative.png', img_negative)

# Doing rotation image processing 90 degree
img_rotation = np.zeros((img_width, img_height, 3), dtype = "uint8")
for x in range(0, img_width) :
  for y in range(0, img_height) :
    img_rotation[x, y] = img_src[column_length - y, x]

cv2.imwrite('./images/pointwise/Lenna-Rotation.png', img_rotation)

# Doing flip vertical image processing
img_flip = np.zeros((img_width, img_height, 3), dtype = "uint8")
for x in range(0, img_width) :
  for y in range(0, img_height) :
    img_flip[x, y] = img_src[row_length - x, y]

cv2.imwrite('./images/pointwise/Lenna-Flip.png', img_flip)

# Doing zoom in image processing with 2 scale
img_zoom_out = np.zeros((img_width*2, img_height*2, 3), dtype = "uint8")
m = 0
n = 0
for x in range(0, img_width) :
  for y in range(0, img_height) :
    img_zoom_out[m, n] = img_src[x, y]
    img_zoom_out[m, n + 1] = img_src[x, y]
    img_zoom_out[m + 1, n] = img_src[x, y]
    img_zoom_out[m + 1, n + 1] = img_src[x, y]
    n += 2
  m += 2
  n = 0

cv2.imwrite('./images/pointwise/Lenna-Zoom.png', img_zoom_out)

cv2.waitKey(0)
cv2.destroyAllWindows()