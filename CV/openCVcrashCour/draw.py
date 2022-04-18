import cv2 as cv
import numpy as np

# generate black img
black_img = np.zeros((500, 500, 3), dtype='uint8')
# green_img = black_img[:] = 0, 255, 0
# red_img = black_img[:] = 0, 0, 255


# ##################################### change the color of the black img
# cv.imshow('green_img', green_img)
# cv.imshow('black_img', black_img)
# cv.imshow('red_img', red_img)


# ##################################### color a certain portion of the black img
# black_img[200:300, 300:400] = 255,0,0
# cv.imshow('black_img', black_img)
# cv.waitKey(0)


# ##################################### Draw a rectangle
# cv.rectangle(black_img, (0, 0),
#              (black_img.shape[1] // 2, black_img.shape[0]//2), (0, 255, 0), thickness=cv.FILLED)
# cv.imshow('black_img', black_img)


# ##################################### Draw a circle
# cv.circle(black_img, (black_img.shape[1] // 2,
#           black_img.shape[0]//2), 40, (0, 255, 0), thickness=3)
# cv.imshow('black_img', black_img)


# ##################################### Draw a line
# cv.line(black_img, (0, 0), (200, 300), (255, 255, 255), thickness=3)
# cv.imshow('line', black_img)
# cv.waitKey(0)


# ##################################### Write a Text
cv.putText(black_img, 'Tesfit Haile', (0, 200),
           cv.FONT_HERSHEY_COMPLEX, 1.0, (255, 0, 255), 2)

cv.imshow('text', black_img)
cv.waitKey(0)

cv.destroyAllWindows()
