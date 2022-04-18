import cv2 as cv
import numpy as np


img = cv.imread('Photos/house_1.jpeg')
cv.imshow('image_', img)

b, g, r = cv.split(img)

cv.imshow('blue', b)
cv.imshow('green', g)
cv.imshow('red', r)

print(img.shape)
print(g.shape)
print(r.shape)
print(g.shape)

# ######  combine them
mereged_img = cv.merge([b, g, r])
cv.imshow('Merged_img', mereged_img)


""" Re-Constract the b, g, r by creating new black img then merge them to get the original image """

black_img = np.zeros(img.shape[:2], dtype='uint8')

# ##################### constract them with the black img to see the actual img
blue = cv.merge([b, black_img, black_img])
green = cv.merge([black_img, g, black_img])
red = cv.merge([black_img, black_img, r])

cv.imshow('blue', blue)
cv.imshow('green', green)
cv.imshow('red', red)


cv.waitKey(0)
cv.destroyAllWindows()
