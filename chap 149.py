import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('coin01.jpg')

img_org = img.copy()

imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(imgray,127,255,0)
contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

img_org = cv2.drawContours(img_org, contours, -1, (255, 0, 0), 3)

plt.subplot(1,2,1),plt.imshow(img,cmap = 'gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])
plt.subplot(1,2,2),plt.imshow(img_org,cmap = 'gray')
plt.title('Contour'), plt.xticks([]), plt.yticks([])

plt.show()

#https://blog.christianperone.com/2014/06/simple-and-effective-coin-segmentation-using-python-and-opencv/