import cv2 as cv
import numpy as np


img = cv.imread('Photos/house_1.jpeg')

black_img = np.zeros((400, 400), dtype='uint8')

# Rectangle
rectangle = cv.rectangle(black_img.copy(), (30, 30), (370, 370), 255, -1)
circle = cv.circle(black_img.copy(), (200, 200), 200, 255, -1)

cv.imshow('rectangle', rectangle)
cv.imshow('circle', circle)


# ##### Bitwise_AND  ##### only intersecting region
bitwise_and = cv.bitwise_and(rectangle, circle)
cv.imshow('bitwise_and', bitwise_and)


# ##### Bitwise_OR #### non-intersecting and intersectin area
bitwise_or = cv.bitwise_or(rectangle, circle)
cv.imshow('bitwise_or', bitwise_or)


# ##### Bitwise_xor non-intersection regions
bitwise_xor = cv.bitwise_xor(rectangle, circle)
cv.imshow('bitwise_xor', bitwise_xor)


cv.waitKey(0)
cv.destroyAllWindows()
