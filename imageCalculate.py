from cv2 import cv2
import matplotlib.pyplot as plt
from skimage import io,color
import numpy as np
from PIL import Image
import imageio
from math import tanh
from scipy import signal
import os
import json
import requests
import sys

params = {
    'sigmaBF': int(sys.argv[1]),
    'phieqCQ': int(sys.argv[2]),
    'sigmaDE': int(sys.argv[3]),
}

def variableCalculate(percentage, max, reverse):
    if reverse:
        if percentage == 100:
            return 1
        elif percentage > 0:
            return (1-percentage/100)*max
        else:
            return max
    else:
        if percentage > 0:
            return percentage / 100 * max
        else:
            return 1

# Parameters
filepath = "./upload/filename.jpg"

# Bilateral filter
s = 8
sigmacolor = sigmaspace = variableCalculate(params['sigmaBF'], 20, False)

# Color quantization
phieq = variableCalculate(params['phieqCQ'], 20, False)

# Dog edge detection
sigma = variableCalculate(params['sigmaDE'], 4, True)
phie = 5  # typically [0.75,5] controls the sharpness of the activation falloff
tau = 0.981 # typically [0,1] control the center-sourround difference required for cell activation

def loadingImage():
    rgb = io.imread('./upload/filename.jpg')
    lab = color.rgb2lab(rgb) # img_array, RGB-image = MxNx3
    L, a, b = lab[:,:,0], lab[:,:,1], lab[:,:,2]
    m1, n1 = L.shape
    L0 = np.float32(L)
    D = np.zeros((m1,n1))

    L = np.float32(L)
    a = np.float32(a)
    b = np.float32(b)

    for i in range(3): # channel = 3, line 43
        L = cv2.bilateralFilter(L, s, sigmacolor, sigmaspace)
        a = cv2.bilateralFilter(a, s, sigmacolor, sigmaspace)
        b = cv2.bilateralFilter(b, s, sigmacolor, sigmaspace)

    def qnearest(f):
        q=0
        if f>=0 and f<5:
            q=0
        elif f>=5 and f<15:
            q=10
        elif f>=15 and f<25:
            q=20
        elif f>=25 and f<35:
            q=30
        elif f>=35 and f<45:
            q=40
        elif f>=45 and f<55:
            q=50
        elif f>=55 and f<65:
            q=60
        elif f>=65 and f<75:
            q=70
        elif f>=75 and f<85:
            q=80
        elif f>=85 and f<95:
            q=90
        elif f>=95 and f<100:
            q=100
        return q

    def gauss2D(shape,sigma):
        m,n = [(ss-1.)/2. for ss in shape]
        y,x = np.ogrid[-m:m+1,-n:n+1]
        h =np.exp(-(x*x + y*y)/(2.*sigma*sigma) )
        h[ h < np.finfo(h.dtype).eps*h.max() ] = 0
        sumh = h.sum()
        if sumh != 0:
            h /= sumh
        return h
    
    Quantum = np.zeros((m1, n1))
    imge = signal.convolve(L0, gauss2D((5,5),sigma), mode = 'same')
    imgr = signal.convolve(L0, gauss2D((5,5),sigma * 1.5), mode = 'same')

    for i in range(m1):
        for j in range(n1):
            Quantum[i,j]=qnearest(L[i,j])+5*tanh((L[i,j]-qnearest(L[i,j]))/phieq)
            
            if imge[i,j] - tau * imgr[i,j] > 0:
                D[i,j] = 1
            else:
                D[i,j] = 1 + tanh((imge[i,j] - tau * imgr[i,j]) * phie)


    L = Quantum

    lab3 = lab
    lab3[:,:,0] = L
    lab3[:,:,1] = a
    lab3[:,:,2] = b

    rgbFinal = color.lab2rgb(lab3)


    imgFinal = Image.new('RGB', (n1, m1), 'black')
    pixel = imgFinal.load()
    for i in range(m1):
        for j in range(n1):
            if D[i,j] < 0.1:
                r = g = b = 255 * D[i,j]
            else:
                r = 255 * rgbFinal[i, j, 0]
                g = 255 * rgbFinal[i, j, 1]
                b = 255 * rgbFinal[i, j, 2]

            pixel[j,i] = int(r), int(g), int(b)

    imageio.imwrite('./upload/final.jpg', imgFinal)


loadingImage()

resultList = {
    'sigmaBF': sigmacolor,
    'phieqCQ': phieq,
    'sigmaDE': sigma,
    'isOk': True,
    'message': 'Image calculate success'
}

result = json.dumps(resultList, ensure_ascii=False)

print(result)

sys.stdout.flush()