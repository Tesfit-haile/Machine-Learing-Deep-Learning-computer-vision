import cv2 as cv
import numpy as np

img = cv.imread('Photos/boston_park.jpeg')

gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray_img', gray_img)


# ############ laplacian

laplacian_img = cv.Laplacian(gray_img, cv.CV_64F)
laplacian_img = np.uint8(np.absolute(laplacian_img))
cv.imshow('laplacian_img', laplacian_img)


# ########## Sobel ---- > y and x axis gradient

sobelx_img = cv.Sobel(gray_img, cv.CV_64F, 1, 0)
sobely_img = cv.Sobel(gray_img, cv.CV_64F, 0, 1)
combined_sobels_img = cv.bitwise_or(sobelx_img, sobely_img)

cv.imshow('sobelx_img', sobelx_img)
cv.imshow('sobely_img', sobely_img)
cv.imshow('combined_sobels_img', combined_sobels_img)


cv.waitKey(0)
cv.destroyAllWindows()
