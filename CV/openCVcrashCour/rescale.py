import cv2 as cv

#### larger images/videos file tends to store a lot of informations in it 
#### a computer needs a lot of proccessing to display it 
#### the reason we are rescaling or resizing is cameras do not go higher that they can 
## so we need to downsample it (rescale or resize) meaning we've to change the Height and width


#lets create a rescaler func for video, live video and img
def rescalerFrame(frame, scale=0.25):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimension = (width, height)
    return cv.resize(frame, dimension, interpolation=cv.INTER_AREA)


capture = cv.VideoCapture('Videos/dog_video.mp4')
while True:
    isTrue, frame = capture.read()
    resizedVideo = rescalerFrame(frame, scale=0.75)

    cv.imshow('oldVideo', frame)
    cv.imshow('newVideo', resizedVideo)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.realse()
cv.destroyAllWindows()