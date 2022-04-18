import cv2 as cv
import matplotlib.pyplot as plt
""" openCV reads in the form of  BGR no RGB """
""" it is totally d/t how openCV reads an img """

img = cv.imread('Photos/cat_1.png')

# plt.imshow(img)
# plt.show()


# ########################################################   BGR to gray
# gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('gray_img', gray_img)


# ########################################################  BGR to HSV
hsv_img = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('HSV', hsv_img)


# ########################################################  BGR to l*a*b
# """ this is how human pereciv color  """
# lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
# cv.imshow('lab', lab)


# """ We can convert BGR to RGB using the openCV """
# rgb = cv.cvtColor(img, cv.COLOR_RGB2BGR)
# cv.imshow('rgb', rgb)


# ##################################################### NOW THE OTHER WAY AROUND [ any to BGR ]
# #####################################################
# there is no way convert a gray_img directly to BGR but instead convert it to hsv then to BGR

# ################## HCV to BGR
hsv_to_bgr = cv.cvtColor(hsv_img, cv.COLOR_HSV2BGR)
cv.imshow('hsv_to_bgr', hsv_to_bgr)


cv.waitKey(0)
cv.destroyAllWindows()
