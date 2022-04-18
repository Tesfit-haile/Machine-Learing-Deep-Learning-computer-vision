import cv2import matplotlib.pyplot as pltimport numpy as nplena_img = cv2.imread('Photos/Lena.png')gray_lena = cv2.cvtColor(lena_img, cv2.COLOR_BGR2RGB)cv2.imshow('Original_lena_img', lena_img)# blur functionblurred_img = cv2.blur(gray_lena, (1, 1))# GaussianBlurgaussianBlur = cv2.GaussianBlur(gray_lena, (7, 7), 0)# medianmedianBlur = cv2.medianBlur(gray_lena, 5)names  = ["gray_lena", 'blurred_img', 'gaussianBlur', 'medianBlur']images = [gray_lena, blurred_img, gaussianBlur, medianBlur]for i in range(len(names)):    plt.subplot(2, 2, i+1), plt.imshow(images[i], 'gray')    plt.title(names[i])    plt.xticks([]), plt.yticks([])plt.show()cv2.waitKey(0)cv2.destroyAllWindows()