import numpy as np
import cv2

n = int(input("Enter canvas size in pixel ( multiple of 8 ): "))
box_size = int(n/8)
print(box_size)

checkerboard = np.zeros([n,n],dtype = 'uint8')
s = box_size
e = box_size * 2

for j in range(s,n,e):
    for i in range(s,n,e):
        checkerboard[j-s:j,i-s:i] = 255
        checkerboard[j:j+s,i:i+s] = 255

cv2.imshow('Checkboard 8*8',checkerboard)
cv2.waitKey(0)
cv2.destroyAllWindows()