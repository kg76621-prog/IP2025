import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('IMG_6504.jpg')
rows,cols,ch = img.shape

pts1 = np.float32([[168,189],[760,193],[810,1090],[96,1074]])
pts2 = np.float32([[0,0],[300,0],[300,500],[0,500]])

M = cv2.getPerspectiveTransform(pts1,pts2)

dst = cv2.warpPerspective(img,M,(300,500))

plt.subplot(121),plt.imshow(img),plt.title('Input')
plt.subplot(122),plt.imshow(dst),plt.title('Output')
plt.show()