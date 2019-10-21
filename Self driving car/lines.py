# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 20:21:57 2019

@author: Nadia
"""
import cv2

#from cv2 import __version__

img=cv2.imread('Anne.jpg',1)


resized=cv2.resize(img,(int(img.shape[1]/2),int(img.shape[0]/2)))
#print(img.shape)
cv2.imshow("result",resized)
cv2.waitKey(5000)
cv2.destroyAllWindows()

