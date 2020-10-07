import cv2

print('Open CV Version {0}'.format(cv2.__version__))
img = cv2.imread('./images/sample.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow('Image sample', img)
cv2.imshow('Image sample gray', gray)

cv2.waitKey()
cv2.destroyAllWindows()