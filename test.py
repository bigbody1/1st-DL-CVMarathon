import cv2
img = cv2.imread('lena.png', cv2.IMREAD_COLOR)
img2 = cv2.imread('lena.png', cv2.IMREAD_GRAYSCALE)

cv2.imshow('rgb', img)
cv2.imshow('gray', img2)
cv2.waitKey(0)



