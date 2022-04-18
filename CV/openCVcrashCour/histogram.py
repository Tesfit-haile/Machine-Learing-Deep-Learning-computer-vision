import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt


""" histogram helps us to see the distribution of the pixel intensity of an img """

img = cv.imread('Photos/house_1.jpeg')


black_img = np.zeros(img.shape[:2], dtype='uint8')


""" HISTOGRAM FOR GRAY IMAGE ............ """
# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Gray', gray)


# circle = cv.circle(
#     black_img, (img.shape[1] // 2, img.shape[0] // 2), 100, 255,  -1)


# # we can do it in a specific part of an image by finding the mask
# masked_img = cv.bitwise_and(gray, gray, mask=circle)
# cv.imshow('masked_img', masked_img)

# GRayscale histogram
# gray_hist = cv.calcHist([gray], [0], masked_img, [256], [0, 256])


# plt.figure()
# plt.title('Grayscale Histogram')
# plt.xlabel('Bins')
# plt.ylabel('# of pixels')
# plt.plot(gray_hist)
# plt.xlim([0, 256])
# plt.show()


""" HISTOGRAM FOR COLORED IMAGE ............ """

# ###################@ compoting Colored img hostogram
circle = cv.circle(
    black_img, (img.shape[1] // 2, img.shape[0] // 2), 100, 255,  -1)


# # we can do it in a specific part of an image by finding the mask
masked_img = cv.bitwise_and(img, img, mask=circle)
cv.imshow('masked_img', masked_img)


plt.figure()
plt.title('Grayscale Histogram')
plt.xlabel('Bins')
plt.ylabel('# of pixels')


colors = ('b', 'g', 'r')

for i, colo in enumerate(colors):
    hist = cv.calcHist([img], [i], None, [256], [0, 256])
    plt.plot(hist, color=colo)
    plt.xlim([0, 256])

plt.show()


cv.waitKey()
cv.destroyAllWindows()
