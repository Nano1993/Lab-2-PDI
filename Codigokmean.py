#! /usr/bin/env python

from SimpleCV import*
import cv2
from matplotlib import pyplot as plt
from sklearn.cluster import KMeans
import argparse
import numpy as np


image=cv2.imread('rayasgris.png')
(a,b)=image.shape[:2]
image=image.reshape((image.shape[0]*image.shape[1],3))
clt=KMeans(n_clusters = 3)
labels = clt.fit_predict(image)
quant = clt.cluster_centers_.astype('uint8')[labels]
quant = quant.reshape((a,b,3))
image = image.reshape((a,b,3))
cv2.imshow('image',np.hstack([quant]))
cv2.waitKey(0)


