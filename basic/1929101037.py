# Author I Putu Ashadi Sedana Pratama
# Email: ashsepra@gmail.com
# This file contain basic image processing using opencv-python package
# before running the code below, please make sure already installed opencv-python package
# How to install is below
# https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_setup/py_table_of_contents_setup/py_table_of_contents_setup.html
# I'm using python 3 with the newest version of python 3.7.3

# Function to display dimension and image type
# Argument are img_arg is image and image_type is string description
def print_img_shape(img_arg, img_type) :
  # Get dimension of the image
  dimension = img_arg.shape
  # Display of the title
  print('=================================')
  print('======== Image dimension ========')
  print('======== ', img_type ,' ========')
  print('=================================')
  # Display height and width image
  # First index is height
  # Second index is width
  print('Image height: ', dimension[0])
  print('Image width: ', dimension[1])
  # Clasify the image type by checking the channel of the image
  # RGB image and RGBA image contain the third index for channel information
  # Assume that the length of the array is always 3
  if len(dimension) > 2 :
    # RGB image has channel value is 3
    if dimension[2] == 3 :
      print('Image type is RGB image')
    # RGB image has channel value is 4
    else: 
      print('Image type is RGBA image')
  else :
    color_value = img_arg[0, 0]
    # Grayscale image is average of color by RGB image
    # The grayscale image value between 1 until 254
    if color_value > 0 and color_value < 255 :
      print('Image type is Grayscale image')
    # The binary image value is 0 or 255
    else :
      print('Image type is Binary image')

# Function to display image color on specific row and column
# Argument are img_arg is image, row is row value, col is column value, and image_type is string description, 
def display_color_index(img_arg, row, col, img_type) :
  print('=================================')
  print('======== Image color information ========')
  print('======== ', img_type ,' ========')
  print('=================================')
  # Get dimension of the image
  dimension = img_arg.shape
  # Check the maximum row and column
  if (row >= dimension[0] or col >= dimension[1]) :
    print('Please check your row and column input, maximum value for row is ', dimension[0] - 1, ' and maximum value for column is ', dimension[1] - 1)
  else :
    # RGB image and RGBA image contain the third index for channel information
    # Assume that the length of the array is always 3
    # Display color of RGB and RGBA image start with Blue and continue by Red and Green
    if len(dimension) > 2 :
      print('Color value at row ', row ,', column ', col ,'are : ')
      print('Blue ', img_arg[row, col][0])
      print('Red ', img_arg[row, col][1])
      print('Green ', img_arg[row, col][2])
    else :
      # Display color of grayscale and binary image
      print('Color value at row ', row ,', column ', col ,'is : ', img_arg[row, col])

# Import opencv-python package, it is called cv2
import cv2

# Get image from "images" directory
# I'm using Lenna file for example
file_img = './images/Lenna.png'
img_src = cv2.imread(file_img)

# Convert the image to rgba image type
# Use COLOR_BGR2RGBA enum to proceed it
img_rgba = cv2.cvtColor(img_src, cv2.COLOR_BGR2BGRA)

# Convert the image to grayscale image type
# Use COLOR_BGR2GRAY enum to proceed it
img_gray = cv2.cvtColor(img_src, cv2.COLOR_BGR2GRAY)

# Convert the gray image to binary image type
# First we need to decide threshould value to make sure the image is not become fully black
# I decide to use 128 for threshould value
# Use threshold function, the documentation is below
# https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_thresholding/py_thresholding.html#:~:text=If%20pixel%20value%20is%20greater,should%20be%20a%20grayscale%20image.
# Use THRESH_OTSU enum to proceed it
# The threshold function with THRESH_OTSU enum will return array with two index, first index is for threshould and the second one is for binarization
threshould = 128
img_binary = cv2.threshold(img_gray, threshould, 255, cv2.THRESH_OTSU)[1]

# Now we have 4 image with different type
# We call it one by one to know the dimension and color depth 
print_img_shape(img_src, 'Source Image')
print_img_shape(img_rgba, 'RGBA Image')
print_img_shape(img_gray, 'Gray Image')
print_img_shape(img_binary, 'Binary Image')

# Now we to check the image color on specific row and column
# We call it one by one to know the  image color value
print('=========================================')
again = True
print('Let\'s play a game, please input the index of row and column of the image to get the color information')
while again :
  row = int(input('Please input row of the image: '))
  col = int(input('Please input row of the image: '))
  print('Color at image ')
  display_color_index(img_src, row, col, 'Source Image')
  display_color_index(img_rgba, row, col, 'RGBA Image')
  display_color_index(img_gray, row, col, 'Gray Image')
  display_color_index(img_binary, row, col, 'Binary Image')
  print('=========================================')
  try_again = input('You want to try again (Y/N)? ')
  again = not (try_again == 'N' or try_again == 'n')
  print('=========================================')

save = input('Do you want to save the image (Y/N)?' )
if (save == 'Y' or save == 'y') :
  print('Image option :')
  print('1. RGBA Image')
  print('2. Gray Image')
  print('3. Binary Image')
  choose = int(input ('What kind of image do you want to save (1/2/3) '))
  file_name = input('Your name file : ' )
  file_save = './images/modify/' + file_name + '.png'
  img_save = img_rgba
  if choose == 2 :
    img_save = img_gray
  elif choose == 3 :
    img_save = img_binary
  success = cv2.imwrite(file_save, img_save)
  if success :
    cv2.imshow(file_name, img_save)

cv2.waitKey(0)
cv2.destroyAllWindows()