import cv2import matplotlib.pyplot as pltimport numpy as npimg = cv2.imread('Photos/openCV_img.jpeg')gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)cv2.imshow('gray_img', gray_img)""" first we need to find out the threshold in order to find the contour """success, thresh = cv2.threshold(gray_img, 127, 255, 0)cv2.imshow('thresh', thresh)cv2.waitKey(0)cv2.destroyAllWindows()