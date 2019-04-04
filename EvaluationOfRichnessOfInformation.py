import cv2
import math
from Histogram import histogram as h


img1 = cv2.imread('Low_Contrast.jpg', cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread('Modified_Contrast.jpg', cv2.IMREAD_GRAYSCALE)

height1 = img1.shape[0]
width1 = img1.shape[1]
pixels1 = width1*height1
height2 = img2.shape[0]
width2 = img2.shape[1]
pixels2 = width2*height2

hist1 = h(img1)
hist2 = h(img2)

Entropy1 = 0
Entropy2 = 0
for i in range(0, 256):
    p1 = (hist1[i]/pixels1)
    p2 = (hist2[i]/pixels2)
    if p1 > 0:
        Entropy1 += p1*math.log(p1, 2)
    if p2 > 0:
        Entropy2 += p2*math.log(p2, 2)

print(f"Entropy of Low_Contrast {-Entropy1} ")
print(f"Entropy of Modified_Contrast {-Entropy2} ")
