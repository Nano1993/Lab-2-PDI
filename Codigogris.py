#! /usr/bin/env python


from SimpleCV import Camera, Display, Image
import time
import matplotlib.pyplot as plt

imgc = Image('cuadradito.png')
imgGrayc = imgc.grayscale()
imgGrayc.save('cuadraditogris.png')

plt.figure()
histc = imgGrayc.histogram(255)
plt.subplot(3,1,1)
plt.stem(histc)
plt.axis('tight')


imgb = Image('blanca.png')
imgGrayb = imgb.grayscale()
imgGrayb.save('blancagris.png')

histb = imgGrayb.histogram(255)
plt.subplot(3,1,2)
plt.stem(histb)
plt.axis('tight')


imgr = Image('rayas.png')
imgGrayr = imgr.grayscale()
imgGrayr.save('rayasgris.png')

histr = imgGrayr.histogram(255)
plt.subplot(3,1,3)
plt.stem(histr)
plt.axis('tight')

plt.show()

