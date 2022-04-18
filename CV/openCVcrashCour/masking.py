import cv2 as cv
import numpy as np

""" Masking allows us to focus on certain part of an image that we like ...."""
img = cv.imread('Photos/cat_1.png')


# ################################# now lets create a circle then will merge it with the real img

black_img = np.zeros((img.shape[:2]), dtype='uint8')

circle = cv.circle(
    black_img, (img.shape[1] // 2, img.shape[0] // 2), 100, 255,  -1)
cv.imshow('circle', circle)

# ##### Bitwise_AND  ##### only intersecting region
masked_img = cv.bitwise_and(img, img, mask=circle)
cv.imshow('masked_img', masked_img)


cv.waitKey(0)
cv.destroyAllWindows()
