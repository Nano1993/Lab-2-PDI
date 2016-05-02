#! /usr/bin/env python
#!/usr/bin/python
from SimpleCV import Camera, Display, Image
import cv2
import time
import matplotlib.pyplot as plt
import argparse
import numpy as np
from sklearn.cluster import KMeans


#Tomar fotos
var = 'si'

while var == 'si' :
 print "Tomando fotografia..."
 c = Camera()
 time.sleep(2)
 img = c.getImage()
 img.show()
 var = raw_input("desea tomar la foto nuevamente: (si/no) ")
 
print "Indique que tipo de fondo tiene el papel :"
print "   1. Papel Blanco"
print "   2. Papel Cuadriculado"
print "   3. Papel caligrafico"
papel = raw_input(" ")
enter = raw_input("Para mostrar la imagen a escala de grises presione Enter")
# Dejarla a escala gris
imgGray = img.grayscale()
imgGray.save('fotopruebagris.png')
# Mostrar imagen a escala de gris
imgGray.show()
enter = raw_input("Para mostrar la histograma de la imagen a escala de grises presione Enter")
# Mostrar histograma
plt.figure()
histc = imgGray.histogram(255)
plt.title("Histograma para foto cuadriculada gris")
plt.stem(histc)
plt.yticks([])
plt.axis('tight')
plt.show()
time.sleep(2)
enter = raw_input("Para mostrar la imagen binarizada que solo muestre las letras presione Enter")

if papel == '1':
# Binarizacion blanca
  imgfixed=imgGray.binarize(160)
  imgfixed=imgfixed.invert()
  imgfixed.show()
  enter = raw_input("Para mostrar el fondo presione Enter")
  imgfixed2=imgGray.binarize(225)
  imgfixed2=imgfixed2.invert()
  imgfixed2.show()
  enter = raw_input("Para mostrar la imagen aplicando las tres segmentaciones con Kmeans presione Enter")
  
elif papel == '2':
    # Binarizacion cuadriculada
  imgfixed=imgGray.binarize(100)
  imgfixed=imgfixed.invert()
  imgfixed.show()
  enter = raw_input("Para mostrar la imagen con solo las cuadriculas presione Enter")
  imgfixed2=imgGray.binarize(160)
  imgfixed2=imgfixed2.invert()
  imgfixed2.show()
  enter = raw_input("Para mostrar la imagen con las cuadriculas sin letras precione Enter")
  imgcuanew = imgfixed2.invert() - imgfixed.invert()
  imgcuanew.invert().show()
  enter = raw_input("Para mostrar la imagen aplicando las tres segmentaciones con Kmeans presione Enter")
   
elif papel == '3':
    # Binarizacion rayada
  imgfixed=imgGray.binarize(105)
  imgfixed=imgfixed.invert()
  imgfixed.show()
  enter = raw_input("Para mostrar la imagen con solo las cuadriculas presione Enter")
  imgfixed2=imgGray.binarize(160)
  imgfixed2=imgfixed2.invert()
  imgfixed2.show()
  enter = raw_input("Para mostrar la imagen caligrafica sin letras precione Enter")
  imgcuanew = imgfixed2.invert() - imgfixed.invert()
  imgcuanew.invert().show()
  enter = raw_input("Para mostrar la imagen aplicando las tres segmentaciones con Kmeans presione Enter")

# Usar Kmean para distintos valores
print('Esperando la imagen aplicando Kmeans con 3 segmentos...')
image=cv2.imread('fotopruebagris.png')
(a,b)=image.shape[:2]
image=image.reshape((image.shape[0]*image.shape[1],3))
clt=KMeans(n_clusters = 3)
labels = clt.fit_predict(image)
quant = clt.cluster_centers_.astype('uint8')[labels]
quant = quant.reshape((a,b,3))
image = image.reshape((a,b,3))
cv2.imshow('image',np.hstack([quant]))
cv2.waitKey(0)
