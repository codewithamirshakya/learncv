# Python program to illustrate
# corner detection with Shi-Tomasi method


# imports
import cv2
import numpy as np
import matplotlib.pyplot as plt
# %matplotlib inline

# path to input image specified 
# image is loaded with imread command

image = 'corner1.png'
img = cv2.imread(image)

# convert image to grayscale
gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


# Shi-Tomasi corner detection function
corners = cv2.goodFeaturesToTrack(gray_image, 60, 0.01, 10)

# convert corners to integer
# So that we will be able to draw circles on them
corners = np.intp(corners)

# draw circles around corners
for i in corners:
    x, y = i.ravel()
    cv2.circle(img, (x,y), 3, (255,0,0), -1)

# resulting image
plt.imshow(img), plt.show()

