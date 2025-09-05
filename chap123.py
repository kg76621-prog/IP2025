import numpy as np
import cv2
# Create a black image
img = cv2.imread('meme.jpg')
# Draw a diagonal blue line with thickness of 5 px
img = cv2.line(img,(0,0),(894,894),(255,0,0),5)
img = cv2.rectangle(img,(384,0),(510,128),(0,255,0),3)
img = cv2.circle(img,(447,63), 63, (0,0,255), 10)
img = cv2.ellipse(img,(256,256),(100,50),0,0,90,255,-1)
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'OpenCV',(10,850), font, 4,(0,0,0),2,cv2.LINE_AA)

cv2.imshow('frame',img)
k = cv2.waitKey(0)
if k == 27:
    cv2.destroyAllWindows()

