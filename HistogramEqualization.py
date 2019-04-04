import numpy as np
import cv2

from Histogram import histogram as h
from CumulativeHistogram import cumulative_histogram as ch

img = cv2.imread('Low_Contrast.jpg', cv2.IMREAD_GRAYSCALE)

height = img.shape[0]
width = img.shape[1]
pixels = width*height

hist = h(img)
cum_hist = ch(hist)

p = 0.005

a_low = 0
for i in np.arange(256):
    if cum_hist[i] >= pixels*p:
        a_low = i
        break

a_high = 255
for i in np.arange(255, -1, -1):
    if cum_hist[i] <= pixels*(1-p):
        a_high = i
        break

for i in np.arange(height):
    for j in np.arange(width):
        a = img.item(i, j)
        b = 0
        if a <= a_low:
            b = 0
        elif a >= a_high:
            b = 255
        else:
            b = float(a - a_low) / (a_high - a_low) * 255
        img.itemset((i, j), b)

cv2.imwrite('Modified_Contrast.jpg', img)

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()



