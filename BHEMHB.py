import numpy as np
import cv2
import math

from Histogram import histogram as h

img = cv2.imread('image_process_f16.jpg', cv2.IMREAD_GRAYSCALE)
height = img.shape[0]
width = img.shape[1]
pixels = width*height
hist = h(img)

Exposure = 0
for i in range(0, 256):
    Exposure += ((hist[i]/pixels)*i)
Exposure /= 255

tou = int(256*(1-Exposure))

n_low = 0
for i in range(0, tou):
    n_low += hist[i]
n_up = 0
for i in range(tou, 256):
    n_up += hist[i]

np_low = np.zeros(tou)
np_low[0] = math.log((hist[0]/n_low) + 1)
for i in range(1, tou):
    np_low[i] = np_low[i-1] + math.log((hist[i]/n_low) + 1)
np_up = np.zeros(256)
np_up[tou] = math.log((hist[tou]/n_up) + 1)
for i in range(tou+1, 256):
    np_up[i] = np_up[i-1] + math.log((hist[i]/n_up) + 1)

CHE = np.zeros(256)
for i in range(0, tou):
    CHE[i] = (tou-1)*np_low[i]
for i in range(tou, 256):
    CHE[i] = tou + (255 - tou)*np_up[i]

for i in np.arange(height):
    for j in np.arange(width):
        a = img.item(i, j)
        b = math.floor(CHE[a])
        img.itemset((i, j), b)

cv2.imwrite('BHEMHB_on_image_process_f16.jpg', img)

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

