import cv2 as cv

img = cv.imread('Photos/cat_1.png')
cv.imshow('img...', img)


# ############################################# Gray img
gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray_img...', gray_img)


# ############################################# Blur img
blur_img = cv.GaussianBlur(img, (7, 7), cv.BORDER_DEFAULT)
cv.imshow('blur_img...', blur_img)


# ############################################# Edge Cascade
# 125, 175 --> is a threshold meaning <125 do not catch as edges,
canny_img = cv.Canny(img, 125, 175)
cv.imshow('canny_img...', canny_img)


# ######################## we can reduce the number of Edge by passing the blur_img
# 125, 175 --> is a threshold meaning <125 do not catch as edges,
canny_img2 = cv.Canny(blur_img, 125, 175)
cv.imshow('canny_img2...', canny_img2)


# ######################## dilating  img
dilate_img = cv.dilate(canny_img2, (7, 7), iterations=3)
cv.imshow('dilate_img...', dilate_img)


# ######################## Resizing img
resized_img = cv.resize(img, (400, 400))
cv.imshow('resized_img...', resized_img)


# ######################## Cropping img
cropping_img = img[50:500, 50:600]
cv.imshow('cropping_img...', cropping_img)


cv.waitKey(0)
cv.destroyAllWindows()
