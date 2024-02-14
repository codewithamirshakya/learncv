import cv2
import os

def load_images_from_folder(folder):
    images = []
    for img in os.listdir(folder):
        image = cv2.imread(folder+"/"+img)
        if image is not None:
            images.append(image)

    return images        

def canny_edge_detection(frame): 
    # Convert the frame to grayscale for edge detection 
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 
      
    # Apply Gaussian blur to reduce noise and smoothen edges 
    blurred = cv2.GaussianBlur(src=gray, ksize=(3, 5), sigmaX=0.5) 
      
    # Perform Canny edge detection 
    edges = cv2.Canny(blurred, 70, 135) 
      
    return blurred, edges


# path to input image specified and
# image is loaded with imread command
images = load_images_from_folder('images')

i = 0
for image in images:
    blurred, edges = canny_edge_detection(image)
    filename = f'results/a-{i}.jpg'
    cv2.imwrite(filename, edges)
    i = i + 1
