#! /usr/bin/env python


from SimpleCV import Camera, Display, Image
import time
import matplotlib.pyplot as plt

# Fotos con letras
#     Foto con fondo Cuadrada
imgc = Image('/home/pi/Documents/Fotos_cuadradas/Cuadraditos.png')
imgGrayc = imgc.grayscale()
imgGrayc.save('/home/pi/Documents/Fotos_cuadradas/Cuadraditogris.png')

plt.figure()
histc = imgGrayc.histogram(255)
plt.subplot(3,1,1)
plt.title("Cuadrados gris")
plt.stem(histc)
plt.yticks([])
plt.axis('tight')

#     Foto con fondo Blanca
imgb = Image('/home/pi/Documents/Fotos_blancas/blanca.png')
imgGrayb = imgb.grayscale()
imgGrayb.save('/home/pi/Documents/Fotos_blancas/blancagris.png')

histb = imgGrayb.histogram(255)
plt.subplot(3,1,2)
plt.title("Blanca girs")
plt.stem(histb)
plt.yticks([])
plt.axis('tight')
 
#     Foto con fondo Rayas
imgr = Image('/home/pi/Documents/Fotos_rayas/rayas.png')
imgGrayr = imgr.grayscale()
imgGrayr.save('/home/pi/Documents/Fotos_rayas/rayasgris.png')

histr = imgGrayr.histogram(255)
plt.subplot(3,1,3)
plt.title("Rayas gris")
plt.stem(histr)
plt.axis('tight')
plt.yticks([])
plt.show() 



