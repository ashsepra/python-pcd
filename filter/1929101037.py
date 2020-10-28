# Author I Putu Ashadi Sedana Pratama
# Email: ashsepra@gmail.com
# This file contains basic image filter processing
# before running the code below, please make sure already installed opencv-python package
# How to install is below
# https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_setup/py_table_of_contents_setup/py_table_of_contents_setup.html
# I'm using python version 3 with the newest version of python 3.7.3

from cv2 import cv2
import numpy as np

file_img = './images/Lenna.png'
file_img_noise = './images/Lenna_Noise.png'
img_src = cv2.imread(file_img)
img_noise_src = cv2.imread(file_img_noise)

# Create blur
img_src_blur = img_src.copy()
img_blur_1 = cv2.blur(img_src_blur, (10, 10))
cv2.imwrite('./images/filter/Lenna-Blur.png', img_blur_1)

# Create Gaussian Blur
# the kernel size suppose to be odd
img_src_gaussian = img_src.copy()
img_blur_2 = cv2.GaussianBlur(img_src_gaussian, (11, 11), 0)
cv2.imwrite('./images/filter/Lenna-Gaussian-Blur.png', img_blur_2)

# Create media filter for reduce noise
# the kernal value is odd value
img_src_noise = img_noise_src.copy()
img_blur_3 = cv2.medianBlur(img_src_noise, 5)
cv2.imwrite('./images/filter/Lenna-Median-Blur.png', img_blur_3)

# Create bilateral filter to reduce noise
img_src_bilateral = img_noise_src.copy()
img_blur_4 = cv2.bilateralFilter(img_src_bilateral, 20, 75, 75)
cv2.imwrite('./images/filter/Lenna-Bilateral.png', img_blur_4)

# Edge detection
img_src_edge = img_src.copy()
img_edge_canny = cv2.Canny(img_src_edge, 100, 200)
cv2.imwrite('./images/filter/Lenna-Edge-Canny.png', img_edge_canny)

img_sobel_x = cv2.Sobel(img_src_edge, 0, 1, 0)
img_sobel_y = cv2.Sobel(img_src_edge, 0, 0, 1)
cv2.imwrite('./images/filter/Lenna-Edge-Sobel-X.png', img_sobel_x)
cv2.imwrite('./images/filter/Lenna-Edge-Sobel-Y.png', img_sobel_y)

img_laplacian = cv2.Laplacian(img_src_edge, 0)
cv2.imwrite('./images/filter/Lenna-Edge-Laplacian.png', img_laplacian)


# Prewitt edge mask
kernel_prewitt_x = np.array([
    [-1, 0, 1],
    [-1, 0, 1],
    [-1, 0, 1]])
kernel_prewitt_y = np.array([
    [1, 1, 1],
    [0, 0, 0],
    [-1, -1, -1]])

img_prewitt_x = cv2.filter2D(img_src_edge, 0, kernel_prewitt_x)
img_prewitt_y = cv2.filter2D(img_src_edge, 0, kernel_prewitt_y)
cv2.imwrite('./images/filter/Lenna-Edge-Prewitt-X.png', img_prewitt_x)
cv2.imwrite('./images/filter/Lenna-Edge-Prewitt-Y.png', img_prewitt_y)

# Robert edge mask
kernel_robert_x = np.array([
    [0, 1],
    [-1, 0]])
kernel_robert_y = np.array([
    [1, 0],
    [0, -1]])

img_robert_x = cv2.filter2D(img_src_edge, 0, kernel_robert_x)
img_robert_y = cv2.filter2D(img_src_edge, 0, kernel_robert_y)
cv2.imwrite('./images/filter/Lenna-Edge-Robert-X.png', img_robert_x)
cv2.imwrite('./images/filter/Lenna-Edge-Robert-Y.png', img_robert_y)

# Robinson compass edge mask
kernel_north = np.array([
    [-1, 0, 1],
    [-2, 0, 2],
    [-1, 0, 1]])
kernel_north_west = np.array([
    [0, 1, 2],
    [-1, 0, 1],
    [-2, -1, 0]])
kernel_west = np.array([
    [1, 2, 1],
    [-1, 0, 1],
    [-1, -2, -1]])
kernel_south_west = np.array([
    [2, 1, 0],
    [1, 0, -1],
    [0, -1, -2]])
kernel_south = np.array([
    [1, 0, -1],
    [2, 0, -2],
    [1, 0, -1]])
kernel_south_east = np.array([
    [0, -1, -2],
    [1, 0, -1],
    [2, 1, 0]])
kernel_east = np.array([
    [-1, -2, -1],
    [0, 0, 0],
    [1, 2, 1]])
kernel_north_east = np.array([
    [-2, -1, 0],
    [-1, 0, 1],
    [0, 1, 2]])

img_compass_north = cv2.filter2D(img_src_edge, 0, kernel_north)
img_compass_north_east = cv2.filter2D(img_src_edge, 0, kernel_north_east)
img_compass_east = cv2.filter2D(img_src_edge, 0, kernel_east)
img_compass_south = cv2.filter2D(img_src_edge, 0, kernel_south)
img_compass_south_east = cv2.filter2D(img_src_edge, 0, kernel_south_east)
img_compass_south_west = cv2.filter2D(img_src_edge, 0, kernel_south_west)
img_compass_west = cv2.filter2D(img_src_edge, 0, kernel_west)
img_compass_north_west = cv2.filter2D(img_src_edge, 0, kernel_north_west)

cv2.imwrite('./images/filter/Lenna-Edge-North.png', img_compass_north)
cv2.imwrite('./images/filter/Lenna-Edge-North-East.png', img_compass_north_east)
cv2.imwrite('./images/filter/Lenna-Edge-East.png', img_compass_east)
cv2.imwrite('./images/filter/Lenna-Edge-South-East.png', img_compass_south_east)
cv2.imwrite('./images/filter/Lenna-Edge-South.png', img_compass_south)
cv2.imwrite('./images/filter/Lenna-Edge-South-West.png', img_compass_south_west)
cv2.imwrite('./images/filter/Lenna-Edge-West.png', img_compass_west)
cv2.imwrite('./images/filter/Lenna-Edge-North-West.png', img_compass_north_west)



cv2.waitKey(0)
cv2.destroyAllWindows()