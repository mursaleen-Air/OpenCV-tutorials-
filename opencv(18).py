     #image pyramids in opencv
#i)  Gaussian Pyramid(pyrdown,pyrup) 
#ii) Laplacian Pyramid


import cv2
img = cv2.imread('lena.jpg')
#lr is lower resolution
layer = img.copy()
gp = [layer]

for i in range(5):
    layer = cv2.pyrDown(layer)
    gp.append(layer)
   # cv2.imshow(str(i), layer)

layer = gp[5]
cv2.imshow("upper lvl gaussian pyramid",layer)                      
lp = [layer]
for i in range(5, 0, -1):#(start, stop, reducing by 1)
    gaussian_extended = cv2.pyrUp(gp[i])
    laplacian = cv2.subtract(gp[i-1], gaussian_extended )
    cv2.imshow(str(i), laplacian)


cv2.waitKey(0)
cv2.destroyAllWindows()
