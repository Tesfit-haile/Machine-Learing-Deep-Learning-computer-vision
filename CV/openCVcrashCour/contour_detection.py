import cv2 as cv
import numpy as np


""" Contour is a boundary of an object."""

img = cv.imread('Photos/cat_1.png')
cv.imshow('cat', img)


# ################################################## Black img
black_img = np.zeros(img.shape, dtype='uint8')


# ######################### Gray img
gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('cat', gray_img)


# ########################## Blur img ------
""" one way of reducing the len of the contour drastically is by passing the blur_img to the canny then to the contour """
blur_img = cv.GaussianBlur(img, (5, 5), cv.BORDER_DEFAULT)


# ######################### Canny img
canny_img = cv.Canny(blur_img, 125, 175)
cv.imshow('cats_canny', canny_img)


# ########################## Threshold img ------
""" another way of reducing the len of the contour drastically is by passing the Threshold_img to the canny then to the contour """
ret, threshold_img = cv.threshold(
    gray_img, 125, 255, cv.THRESH_BINARY)  # if <125 make it 0 or black if>125 make it white or 255
cv.imshow('threshold_img', threshold_img)


# ######################### Contour - img

contour_edg, hierarchies = cv.findContours(
    canny_img, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(len(contour_edg))


# ###################################################### we can draw now the contour_edg
""" for some reason this function is not working """
cv.drawContours(black_img, contour_edg, -1, (0, 0, 255), 2)
cv.imshow('drawContour', black_img)

cv.waitKey(0)
cv.destroyAllWindows()
