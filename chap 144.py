import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('opencv_logo_cap.png')

k = 9
blur = cv2.GaussianBlur(img,(k,k),0)
median = cv2.bilateralFilter(img,9,75,75)


plt.subplot(121),plt.imshow(median),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(blur),plt.title('Averaging')
plt.xticks([]), plt.yticks([])
plt.show()