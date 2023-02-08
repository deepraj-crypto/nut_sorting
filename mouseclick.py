import cv2
import numpy as np

def cordinates(event,x,y,flags,paras):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x,y)


img = cv2.imread('LUCID_TRI050S-C_213301347__20221223165613374_image0.jpg')
cv2.imshow('orgimage', img)
cv2.setMouseCallback('orgimage', cordinates)

cv2.waitKey(0)
