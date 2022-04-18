import cv2 as cv
import numpy as np


img = cv.imread('Photos/house_1.jpeg')
cv.imshow('image_', img)


""" We generally smoothing or blur an img when it has a noises( from camera lens or lights ) """
# ####### Types of smoothing
# 1. Average or blur
blur_img = cv.blur(img, (7, 7))
cv.imshow('blur_img', blur_img)

# 2. Gaussianblur
# more num of kernel but less blur
gaussian_img = cv.GaussianBlur(img, (7, 7), 0)
cv.imshow('gaussian_img', gaussian_img)

# 3. Median blur ( more effective on removing the noises than average blur )
median_blur = cv.medianBlur(img, 7)
cv.imshow('median_blur', median_blur)


# 4. Bilateral #####  it is type of blur but similar to the original image
bilateral_img = cv.bilateralFilter(img, 5, 15, 15)
cv.imshow('bilateral_img', bilateral_img)


cv.waitKey(0)
cv.destroyAllWindows()
