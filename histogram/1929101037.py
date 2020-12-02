# Author I Putu Ashadi Sedana Pratama
# Email: ashsepra@gmail.com
# This file contains pointwise image processing using an opencv-python package and matplotlib
# this code relate to histogram color

import cv2
import numpy as np
from matplotlib import pyplot as plt

# Get image from "images" directory
# I'm using Lenna file for example
file_imgs = ['GS.png', 'GS-Bright.jpeg', 'GS-Dark.jpeg', 'Lenna.png', 'Lenna-Bright.jpeg', 'Lenna-Dark.jpeg', 'HC.jpeg', 'LC.jpeg']
for file_img in file_imgs:
  img_src = cv2.imread('./images/' + file_img)

  plt.title(file_img)
  plt.hist(img_src.ravel(),256,[0,256])
  plt.show()

file_imgs = ['Lenna.png', 'Lenna-Bright.jpeg', 'Lenna-Dark.jpeg', 'HC.jpeg', 'LC.jpeg']
for file_img in file_imgs:
  img_src = cv2.imread('./images/' + file_img)
  img_convert = cv2.cvtColor(img_src, cv2.COLOR_BGR2HSV)
  cv2.imwrite('./images/hsv/' + file_img, img_convert)

  plt.title(file_img)
  plt.hist(img_convert.ravel(),256,[0,256])
  plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()