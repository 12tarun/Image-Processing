import numpy as np
import cv2
import math

img1 = cv2.imread('Low_Contrast.jpg', cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread('Modified_Contrast.jpg', cv2.IMREAD_GRAYSCALE)

height = img1.shape[0]
width = img1.shape[1]
pixels = width*height

diffs = 0
for i in np.arange(height):
    for j in np.arange(width):
        a = img1.item(i, j)
        b = img2.item(i, j)
        diffs += (abs(a-b)**2)

MSE = diffs/pixels
PSNR = 10*math.log((255**2)/MSE, 10)

y, z, w, x = 0, 0, 0, 0
for i in np.arange(height):
    for j in np.arange(width):
        y += img2.item(i, j)
        z += y**2
        w += img1.item(i, j)
        x += w**2

C1 = (x/pixels) - ((w/pixels)**2)
C2 = (z/pixels) - ((y/pixels)**2)
Contrast1 = 10*math.log(C1, 10)
Contrast2 = 10*math.log(C2, 10)

print(f"PSNR of Modified_Contrast {PSNR} ")

print(f"Contrast of Low_Contrast {Contrast1} ")
print(f"Contrast of Modified_Contrast {Contrast2} ")
