import cv2 as cv

messi_img = cv.imread('Photos/messi.jpeg')
cv.imshow('messi_img', messi_img)
# we need to convert the img to a gray cuz our haarFaceDetector does NOT care the colores but the edges
# GRAY img
gray_img = cv.cvtColor(messi_img, cv.COLOR_BGR2GRAY)
cv.imshow('messi_img', gray_img)


cv.waitKey(0)
cv.destroyAllWindows()


""" not finished ..."""
