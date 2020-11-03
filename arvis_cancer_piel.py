# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 10:39:41 2020

@author: User
"""

import cv2 #OpenCV
import numpy as np
import matplotlib.pyplot as plt

img1 = cv2.imread('imagenes/A.jpg')
img2 = cv2.imread('imagenes/B.jpg')

#Imagenes en grises
I = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
cv2.imshow('Img1-GRAY', I)

II = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
cv2.imshow('Img2-GRAY', II)

#imagenes en binario

umbral,_ = cv2.threshold(I,0,255,cv2.THRESH_OTSU)
mascara = np.uint8((I<umbral)+255)
cv2.imshow('Img1-Binary',mascara)

umbral2,_ = cv2.threshold(I,0,255,cv2.THRESH_OTSU)
mascara2 = np.uint8((II<umbral2)+255)
cv2.imshow('Img2-Binary',mascara2)

pxX = np.size(img2, axis=0)#w
pxY = np.size(img2, axis=1)#H
pxXY = np.size(img2, axis=None)
pxX = np.size(img1, axis=0)#w
pxY = np.size(img1, axis=1)#H
pxXY = np.size(img1, axis=None)



#Suma (px)
suma1 = np.sum(img1)
suma2 = np.sum(img2)

#Argumento minimo
minimo = np.min(img1)
minimo2 = np.min(img2)

#argumento maximo
maximo = np.max(img1)
maximo2 = np.max(img2)
#promedios
prom = np.mean(img1)
#varianzas
var = np.var(img1)
var2 = np.var(img1)
#desviacion estandar
de = np.sqrt(var)
de2 = np.sqrt(var2)
#histograma

data = I.flatten()
red = img1[:,:,0].flatten()
green = img1[:,:,1].flatten()
blue = img1[:,:,2].flatten()

plt.hist(data,bins=100)
plt.hist(red, bins=1000, histtype="stepfilled", color="red")
plt.hist(green, bins=1000, histtype="stepfilled", color="green")
plt.hist(blue, bins=1000, histtype="stepfilled", color="blue")

data = II.flatten()
red = img2[:,:,0].flatten()
green = img2[:,:,1].flatten()
blue = img2[:,:,2].flatten()

plt.hist(data,bins=100)
plt.hist(red, bins=1000, histtype="stepfilled", color="red")
plt.hist(green, bins=1000, histtype="stepfilled", color="green")
plt.hist(blue, bins=1000, histtype="stepfilled", color="blue")


cv2.waitKey(0)
cv2.destroyAllWindows()