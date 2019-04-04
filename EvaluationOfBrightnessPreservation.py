import numpy as np
import cv2

img1 = cv2.imread('Low_Contrast.jpg', cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread('Modified_Contrast.jpg', cv2.IMREAD_GRAYSCALE)

height = img1.shape[0]
width = img1.shape[1]
pixels = width*height

a, b = 0, 0
for i in np.arange(height):
    for j in np.arange(width):
        a += img1.item(i, j)
        b += img2.item(i, j)

AMBE = abs((a/pixels) - (b/pixels))

print(f"AMBE of Modified_Contrast {AMBE} ")
