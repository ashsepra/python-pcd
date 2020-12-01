# Author I Putu Ashadi Sedana Pratama
# Email: ashsepra@gmail.com
# This file contains pointwise image processing using an opencv-python package and matplotlib
# this code relate to histogram color

import cv2
import numpy as np
from matplotlib import pyplot as plt

# Get image from "images" directory
# I'm using Lenna file for example
file_img = './images/LC.jpeg'
img_src = cv2.imread(file_img)
plt.hist(img_src.ravel(),256,[0,256])
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()