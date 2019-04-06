import numpy as np
import cv2
import math

from Histogram import histogram as h
from CumulativeHistogram import cumulative_histogram as ch

img = cv2.imread('image_process_f16.jpg', cv2.IMREAD_GRAYSCALE)

height = img.shape[0]
width = img.shape[1]
pixels = width*height

hist = h(img)
cum_hist = ch(hist)


for i in np.arange(height):
    for j in np.arange(width):
        a = img.item(i, j)
        b = math.floor(cum_hist[a]*255 / pixels)
        img.itemset((i, j), b)

cv2.imwrite('Modified_Contrast.jpg', img)

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()



