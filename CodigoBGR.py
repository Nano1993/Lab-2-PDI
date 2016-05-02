#! /usr/bin/env python


from SimpleCV import Camera, Display, Image
import time
import matplotlib.pyplot as plt

# Foto con fondo cuadrado

imgc = Image('/home/pi/Documents/Fotos_cuadradas/Cuadraditos.png')
(red,green,blue)=imgc.splitChannels(False)
red_histc=red.histogram(255)
green_histc=green.histogram(255)
blue_histc=blue.histogram(255)

plt.subplot(3,1,1)
plt.stem(red_histc)
plt.xlim([0,255])
plt.title('Cuadrado con letra RED')
plt.axis('tight')
plt.subplot(3,1,2)
plt.stem(blue_histc)
plt.xlim([0,255])
plt.title('Cuadrado con letra BLUE')
plt.axis('tight')
plt.subplot(3,1,3)
plt.stem(green_histc)
plt.xlim([0,255])
plt.title('Cuadrado con letra GREEN')
plt.axis('tight')
plt.show()

# Foto con fondo blanco

imgb = Image('/home/pi/Documents/Fotos_blancas/blanca.png')
(red,green,blue)=imgb.splitChannels(False)
red_histb=red.histogram(255)
green_histb=green.histogram(255)
blue_histb=blue.histogram(255)

plt.subplot(3,1,1)
plt.stem(red_histb)
plt.xlim([0,255])
plt.title('Blanco con letra RED')
plt.axis('tight')
plt.subplot(3,1,2)
plt.stem(blue_histb)
plt.xlim([0,255])
plt.title('Blanco con letra BLUE')
plt.axis('tight')
plt.subplot(3,1,3)
plt.stem(green_histb)
plt.xlim([0,255])
plt.title('Blanco con letra GREEN')
plt.axis('tight')
plt.show()
# Foto con fondo rayas

imgr = Image('/home/pi/Documents/Fotos_rayas/rayas.png')
(red,green,blue)=imgr.splitChannels(False)
red_histr=red.histogram(255)
green_histr=green.histogram(255)
blue_histr=blue.histogram(255)

plt.subplot(3,1,1)
plt.stem(red_histr)
plt.xlim([0,255])
plt.title('Rayas con letra RED')
plt.axis('tight')
plt.subplot(3,1,2)
plt.stem(blue_histr)
plt.xlim([0,255])
plt.title('CRayas con letra BLUE')
plt.axis('tight')
plt.subplot(3,1,3)
plt.stem(green_histr)
plt.xlim([0,255])
plt.title('Rayas con letra GREEN')
plt.axis('tight')
plt.show()

