import cv2 as cv

messi_img = cv.imread('Photos/messi.jpeg')
cv.imshow('messi_img', messi_img)
# we need to convert the img to a gray cuz our haarFaceDetector does NOT care the colores but the edges
# GRAY img
gray_img = cv.cvtColor(messi_img, cv.COLOR_BGR2GRAY)
cv.imshow('messi_img', gray_img)

""" ========================== FOR SINGLE FACE ======================================== """

# use the haarFaceDetector obj
# the below obj will read the 33,000 xml line
haarFaceDetector = cv.CascadeClassifier('haar_face_detector.xml')
detected_face_rectangle = haarFaceDetector.detectMultiScale(
    gray_img, scaleFactor=1.1, minNeighbors=3)  # we'll get --> [[331  67  88  88]] coordinates
print(detected_face_rectangle)
for (x, y, w, h) in detected_face_rectangle:
    cv.rectangle(messi_img, (x, y), (x+w, y+h), (0, 255, 0), thickness=3)
cv.imshow('detected_img', (messi_img))


# ##################################################################################
""" ========================== FOR Multiple FACE ======================================== """

barca_team_img = cv.imread('Photos/people_2.jpeg')
cv.imshow('barca_team_img', barca_team_img)
# we need to convert the img to a gray cuz our haarFaceDetector does NOT care the colores but the edges
# GRAY img
gray_barca_team_img = cv.cvtColor(barca_team_img, cv.COLOR_BGR2GRAY)


# use the haarFaceDetector obj
# the below obj will read the 33,000 xml line
haarFaceDetector2 = cv.CascadeClassifier('haar_face_detector.xml')
""" minNeighbors will impact drastically the face detection... """
detected_face_rectangle2 = haarFaceDetector2.detectMultiScale(
    gray_barca_team_img, scaleFactor=1.1, minNeighbors=1)  # we'll get --> [[331  67  88  88]] coordinates
print(detected_face_rectangle)
print('Number of faces detected... >>> ', len(detected_face_rectangle2))

for (x, y, w, h) in detected_face_rectangle2:
    cv.rectangle(barca_team_img, (x, y),
                 (x+w, y+h), (0, 255, 0), thickness=2)
cv.imshow('detected_img', (barca_team_img))


cv.waitKey(0)
cv.destroyAllWindows()
