import cv2
import numpy as np
from matplotlib import pyplot as plt

def filter_countour(low_range, high_range):
  #Filter color mask
  range_mask = cv2.inRange(img_hsv, low_range, high_range)

  # Dilation
  kernel_mask = np.ones((25, 25))
  dilation = cv2.dilate(range_mask, kernel_mask, iterations=1)

  contours, _ = cv2.findContours(dilation, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
  number = str(len(contours))
  return number, dilation

file_dataset = './dataset/7.jpg'
img_src = cv2.imread(file_dataset)
img_blur = cv2.medianBlur(img_src, 11)
img_hsv = cv2.cvtColor(img_blur, cv2.COLOR_BGR2HSV)

# Detection red
low_range = np.array([170, 50, 50])
high_range = np.array([180, 255, 255])
count, mask_red = filter_countour(low_range, high_range)
print("Red : ", count)

# Detection green
low_range = np.array([36, 25, 25])
high_range = np.array([70, 255, 255])
count, mask_green = filter_countour(low_range, high_range)
print("Green : ", count)

# Detection brown
low_range = np.array([10, 100, 20])
high_range = np.array([20, 255, 200])
count, mask_brown = filter_countour(low_range, high_range)
print("Brown : ", count)

# Detection yellow
low_range = np.array([20,100,100])
high_range = np.array([45,255,255])
count, mask_yellow = filter_countour(low_range, high_range)
print("Yellow : ", count)

# Detection orange
low_range = np.array([0,150,150])
high_range = np.array([20,255,255])
count, mask_orange = filter_countour(low_range, high_range)
print("Orange : ", count)

# Detection blue
low_range = np.array([100,150,0])
high_range = np.array([140,255,255])
count, mask_blue = filter_countour(low_range, high_range)
print("Blue : ", count)

title_images = ['Red mask', 'Blue mask', 'Green mask', 'Brown mask', 'Orange mask', 'Yellow mask']
images = [mask_red, mask_blue, mask_green, mask_brown, mask_orange, mask_yellow]

for i in range(6) :
  plt.subplot(2, 3, i+1)
  plt.imshow(images[i], 'gray')
  plt.title(title_images[i])
  plt.xticks([]), plt.yticks([])

plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()