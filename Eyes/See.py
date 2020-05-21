import cv2
import numpy as np

# cap = cv2.VideoCapture(0)

# ret, frame = cap.read()

# cv2.imshow('video', frame)
# cv2.imwrite('testcubeback.png', frame)

back_raw = cv2.imread('testcubeback.png')
front_raw = cv2.imread('testcubefront.png')

# Convert BGR to HSV
back_hsv = cv2.cvtColor(back_raw, cv2.COLOR_BGR2HSV)
front_hsv = cv2.cvtColor(front_raw, cv2.COLOR_BGR2HSV)

lower_magenta = np.array([140,50,50])
upper_magenta = np.array([160,255,255])
# Threshold the HSV image to get only blue colors
mask = cv2.inRange(back_hsv, lower_magenta, upper_magenta)

cv2.imshow('mask', mask)
k = cv2.waitKey(0)

cv2.destroyAllWindows()