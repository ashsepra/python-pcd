import numpy as np
import cv2

green = np.uint8([[[50,40,43 ]]])
hsv_green = cv2.cvtColor(green,cv2.COLOR_BGR2HSV)
print (hsv_green)