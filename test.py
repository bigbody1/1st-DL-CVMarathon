import cv2
import numpy as np

img = cv2.imread('lena.png', cv2.IMREAD_COLOR)

img_1 = img[:,:,0]
img_2 = img[:,:,1]
img_3 = img[:,:,2]

cv2.imshow('image1', img_1)
cv2.imshow('image2', img_2)
cv2.imshow('image3', img_3)

cv2.waitKey(0)

