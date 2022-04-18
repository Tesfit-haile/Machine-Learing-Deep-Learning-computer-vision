import cv2 as cv
import numpy as np

""" Threshold is converting an image to a binary ....... .... ... .. """
img = cv.imread('Photos/cat_1.png')

# convert it to gray
gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

""" SIMPLE THRESHOLD....."""
# threshold....  #### obj will be white
threshold, thresh_img = cv.threshold(gray_img, 150, 255, cv.THRESH_BINARY)
cv.imshow('thresh_img', thresh_img)


#  invers  #### obj will be blacked
threshold, invers_thresh_img = cv.threshold(
    gray_img, 150, 255, cv.THRESH_BINARY_INV)
cv.imshow('invers_thresh_img', invers_thresh_img)


""" ADAPTIVE THRESHOLD....."""  # BE CARE FULL WITH WHAT RETURNS
adaptive_threshold_img = cv.adaptiveThreshold(
    gray_img, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 3)
cv.imshow('adaptive_threshold_img', adaptive_threshold_img)


# WITH GAUSSIAN
adaptive_threshold_GAUSSIAN = cv.adaptiveThreshold(
    gray_img, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 3)
cv.imshow('adaptive_threshold_GAUSSIAN', adaptive_threshold_GAUSSIAN)


""" SOMETIMES WITH GAUSSIAN WORKS BETTER SOMETIMES WITH THE MEAN....."""

cv.waitKey(0)
cv.destroyAllWindows()
