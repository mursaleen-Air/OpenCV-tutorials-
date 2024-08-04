#joinig 2 images(stacking)
#only images with the same can be stacked
import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread('lena.jpg')
#stacking horizontally
hor_img = np.hstack((img, img))
ver_img = np.vstack((img, img))
hor_img = cv2.cvtColor((hor_img), cv2.COLOR_BGR2RGB)
ver_img = cv2.cvtColor((ver_img), cv2.COLOR_BGR2RGB)
titles = ["hori", "verti"]
images = [hor_img, ver_img]

for i in range(2):
    plt.subplot(1, 2, i +1) , plt.imshow(images[i])
    plt.title(titles[i])

    



plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()