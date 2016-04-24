#! /usr/bin/env python


from SimpleCV import Camera, Display, Image
import time
import matplotlib.pyplot as plt

img = Image('Cuadraditos.png')
(red,green,blue)=img.splitChannels(False)
red_hist=red.histogram(255)
green_hist=green.histogram(255)
blue_hist=blue.histogram(255)

img2 = Image('Cuadraditos2.png')
(red,green,blue)=img2.splitChannels(False)
red_hist2=red.histogram(255)
green_hist2=green.histogram(255)
blue_hist2=blue.histogram(255)

imgc = Image('Cuadraditos.png')
imgGrayc = imgc.grayscale()
imgc2 = Image('Cuadraditos2.png')
imgGrayc2 = imgc2.grayscale()

histc = imgGrayc.histogram(255)
histc2 = imgGrayc2.histogram(255)


plt.subplot(4,2,1)
plt.stem(red_hist)
plt.xlim([0,256])
plt.yticks([])
plt.title('Cuadrado con letra RED')
plt.axis('tight')
plt.subplot(4,2,3)
plt.stem(blue_hist)
plt.xlim([0,256])
plt.yticks([])

plt.title('Cuadrado con letra BLUE')
plt.axis('tight')
plt.subplot(4,2,5)
plt.stem(green_hist)
plt.xlim([0,256])
plt.yticks([])
plt.title('Cuadrado con letra GREEN')
plt.axis('tight')


plt.subplot(4,2,2)
plt.stem(red_hist2)
plt.xlim([0,256])
plt.yticks([])
plt.title('Cuadrado sin letra RED')
plt.axis('tight')
plt.subplot(4,2,4)
plt.stem(blue_hist2)
plt.xlim([0,256])
plt.yticks([])
plt.title('Cuadrado sin letra BLUE')
plt.axis('tight')
plt.subplot(4,2,6)
plt.stem(green_hist2)
plt.xlim([0,256])
plt.yticks([])
plt.title('Cuadrado sin letra GREEN')
plt.axis('tight')

plt.subplot(4,2,7)
plt.stem(histc)
plt.xlim([0,256])
plt.yticks([])
plt.title('Cuadrado con letra gris')
plt.axis('tight')
plt.subplot(4,2,8)
plt.stem(histc2)
plt.xlim([0,256])
plt.yticks([])
plt.title('Cuadrado sin letra gris')
plt.axis('tight')


plt.show()

