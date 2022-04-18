import cv2 as cv
import numpy as np


img = cv.imread('Photos/cat_1.png')
# cv.imshow('img', img)


# ################################# Translating img
# def translate(img, x, y):

#     translateMatrix = np.float32([[1, 0, x], [0, 1, y]])  # translation matrix
#     dimensions = (img.shape[0], img.shape[1])
#     return cv.warpAffine(img, translateMatrix, dimensions)


# tanslated_img = translate(img, 100, 50)
# cv.imshow('tanslated_img', tanslated_img)
# cv.waitKey(0)
# cv.destroyAllWindows()


# ################################# Translating img
# def rotate(img, angle, rotationalPts=None):
#     print(img.shape)
#     width, height = img.shape[:2]

#     if rotationalPts is None:
#         rotationalPts = (width//2, height//2)

#     rotateMatrix = cv.getRotationMatrix2D(rotationalPts, angle, 1.0, )
#     dimensions = (width, height)
#     return cv.warpAffine(img, rotateMatrix, dimensions)


# rotated_img = rotate(img, 45)
# cv.imshow('rotated_img', rotated_img)
# cv.waitKey(0)
# cv.destroyAllWindows()


# ############################## Flip img

flipped = cv.flip(img, 0)
cv.imshow('flipped', flipped)
cv.waitKey(0)
cv.destroyAllWindows()
