#! /usr/bin/env python

from SimpleCV import Camera, Display, Image
import time
import matplotlib.pyplot as plt
import cv2
import numpy as np
from matplotlib import pyplot as plt

# Fotos con letras binarizacion
#   Foto con fondo Cuadrada
imgc = Image('/home/pi/Documents/Fotos_cuadradas/Cuadraditos.png')
imgGrayc = imgc.grayscale()
#   Foto con fondo Blanca
imgb = Image('/home/pi/Documents/Fotos_blancas/blanca.png')
imgGrayb = imgb.grayscale()
#   Foto con fondo Rayas
imgr = Image('/home/pi/Documents/Fotos_rayas/rayas.png')
imgGrayr = imgr.grayscale()

# Binarizacion para imagenes cuadradas

imgfixed=imgGrayc.binarize(150)
imgfixed=imgfixed.invert()
imgfixed.save('/home/pi/Documents/Fotos_cuadradas/imagen Letras cuadraditos.png')

imgfixed2=imgGrayc.binarize(50)
imgfixed2=imgfixed2.invert()
imgfixed2.save('/home/pi/Documents/Fotos_cuadradas/Fondo cuadraditos.png')

imgfixed3=imgGrayc.binarize(190)
imgfixed3=imgfixed3.invert()
imgfixed3.save('/home/pi/Documents/Fotos_cuadradas/cuadricula.png')

imgcuanew = imgfixed3.invert() - imgfixed.invert()
imgcuanew.invert().save('/home/pi/Documents/Fotos_cuadradas/cuadricula nueva.png')

# Binarizacion para imagenes blancas

imgfixedb=imgGrayb.binarize(160)
imgfixedb=imgfixedb.invert()
imgfixedb.save('/home/pi/Documents/Fotos_blancas/imagen Letras.png')

imgfixedb2=imgGrayb.binarize(225)
imgfixedb2=imgfixedb2.invert()
imgfixedb2.save('/home/pi/Documents/Fotos_blancas/Fondo.png')

# Binarizacion para imagenes rayas

imgfixedr=imgGrayr.binarize(160)
imgfixedr=imgfixedr.invert()
imgfixedr.save('/home/pi/Documents/Fotos_rayas/imagen Letras rayas.png')

imgfixedr3=imgGrayr.binarize(200)
imgfixedr3=imgfixedr3.invert()
imgfixedr3.save('/home/pi/Documents/Fotos_rayas/rayitas.png')

imgcuanewr = imgfixedr3.invert() - imgfixedr.invert()
imgcuanewr.invert().save('/home/pi/Documents/Fotos_rayas/rayitas nueva.png')


