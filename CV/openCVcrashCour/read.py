import cv2 as cv


# #### Read an image
# img = cv.imread('Photos/cat_large_3.jpeg')
# print(img.shape)
# cv.imshow('large_cat..', img)
# cv.waitKey(6000)
# cv.destroyAllWindows()


##### Read a video
capture = cv.VideoCapture('Videos/dog_video.mp4')

while True:
    isTrue, frame = capture.read()
    cv.imshow('Video', frame)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.realse()
cv.destroyAllWindows()