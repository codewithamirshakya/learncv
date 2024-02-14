import numpy as np
import cv2 
from matplotlib import pyplot as plt


#read the image
filename = 'corner1.png'
img = cv2.imread(filename)

#covert image to gray scale image
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#detect corners with the goodFeaturesToTrack function
corners = cv2.goodFeaturesToTrack(gray, 27, 0.01, 10)
corners = np.intp(corners)

# we iterate through the corners
# making a circle at each point that we think is a corner

for i in corners:
    x, y = i.ravel()
    cv2.circle(img, (x, y), 3, 255, -1)

plt.imshow(img), plt.show()    

