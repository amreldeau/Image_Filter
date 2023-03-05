import cv2
import numpy as np

img = cv2.imread('Air Force.jpg', -1)

# Defining the filters to apply
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(img, (11, 11), 0)
canny = cv2.Canny(img, 30, 150)

imS = cv2.resize(blurred, (960, 540))
# Displaying the input image and the output images with applied filters:
cv2.imshow('Input Image', img)
cv2.imshow('Grayscale', imS)
cv2.imshow('Blurred', blurred)
cv2.imshow('Canny Edges', canny)

cv2.waitKey(0)

# Save the output images:
cv2.imwrite('output_gray.jpg', gray)
cv2.imwrite('output_blur.jpg', blurred)
cv2.imwrite('output_canny.jpg', canny)
