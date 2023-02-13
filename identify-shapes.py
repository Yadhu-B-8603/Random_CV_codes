"""
In this program , we are going to distinguish between circle and ellipse
We are going to define two functions called circle_ellipse_identifier and square_rectangle_identifier.
In both of these functions we are going to be using contour detection to find the approaximate shape of the object and 
then using the condition of aspect ratio we are going to detect whether the given shape os a circle or ellipse. 
A similar code is used for distinguishing between the square and rectangle.
In this program i could'nt get the output completely due to some problems with contour detection. But the code is good to go
"""
import cv2
import numpy as np
from matplotlib import pyplot as plt
  
# reading image
def circle_ellipse_identifier(img):
    
  
# converting image into grayscale image
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  
# setting threshold of gray image
    _, threshold = cv2.threshold(gray, 90,190, cv2.THRESH_BINARY)
  
# using a findContours() function
    contours, _ = cv2.findContours( threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
  
    i = 0
  
# list for storing names of shapes
    for contour in contours:
  
    # here we are ignoring first counter because 
    # findcontour function detects whole image as shape
        if i == 0:
            i = 1
            continue
  
    # cv2.approxPloyDP() function to approximate the shape
        approx = cv2.approxPolyDP(contour, 0.01 * cv2.arcLength(contour, True), True)
      
    # using drawContours() function
        cv2.drawContours(img, [contour], 0, (0, 0, 255), 1)
  
    # finding center point of shape
        M = cv2.moments(contour)
        if M['m00'] != 0.0:
            x = int(M['m10']/M['m00'])
            y = int(M['m01']/M['m00'])
        (x,y,w,h) = cv2.boundingRect(approx)
        aspect_ratio = w/float(h)
 
        if aspect_ratio >=0.98 and aspect_ratio <=1.02:
            cv2.putText(img, 'Circle', (x, y),cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 0), 2)
        else:
            cv2.putText(img, 'Ellipse', (x, y),cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 0), 2)

    cv2.imshow('shapes', img)
  
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def square_rectangle_identifier(img):
    
  
# converting image into grayscale image
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  
# setting threshold of gray image
    _, threshold = cv2.threshold(gray, 90,190, cv2.THRESH_BINARY)
  
# using a findContours() function
    contours, _ = cv2.findContours( threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
  
    i = 0
  
# list for storing names of shapes
    for contour in contours:
  
    # here we are ignoring first counter because 
    # findcontour function detects whole image as shape
        if i == 0:
            i = 1
            continue
  
    # cv2.approxPloyDP() function to approximate the shape
        approx = cv2.approxPolyDP(contour, 0.01 * cv2.arcLength(contour, True), True)
      
    # using drawContours() function
        cv2.drawContours(img, [contour], 0, (0, 0, 255), 1)
  
    # finding center point of shape
        M = cv2.moments(contour)
        if M['m00'] != 0.0:
            x = int(M['m10']/M['m00'])
            y = int(M['m01']/M['m00'])
        (x,y,w,h) = cv2.boundingRect(approx)
        aspect_ratio = w/float(h)
 
        if aspect_ratio >=0.95 and aspect_ratio <=1.05:
            cv2.putText(img, 'Square', (x, y),cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 0), 2)
        else:
            cv2.putText(img, 'Rectangle', (x, y),cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 0), 2)

    cv2.imshow('shapes', img)
  
    cv2.waitKey(0)
    cv2.destroyAllWindows()

img1 = cv2.imread('D:/IMG 1.jpeg')  
circle_ellipse_identifier(img1)  
img2 = cv2.imread('D:/IMG 2.jpeg')
circle_ellipse_identifier(img2)
img3 = cv2.imread('D:/IMG 3.jpeg')  
square_rectangle_identifier(img3)  
img4 = cv2.imread('D:/IMG 4.jpeg')
square_rectangle_identifier(img4)