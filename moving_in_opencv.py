"""
Here we are going to put a screen saver for our window using opencv. 
After importing all the necessary libraries(numpy and cv2) , we define a function called screen saver. 
In this we take 4 variables x,y,dx,dy . the two variables x and y are used to determine the coordinates of the center of the circle. 
the variables dx and dy , increases the x and y value correspondingly as to move the circle around.
Then we will use some if statements to account for the collision in boundaries

After defining the function , we insert the image we want to display and then provide the condition for time to start the screen savr after no key is pressed.
For some extra thing , i am also doing a live text adding into the window if the screensaveer is not done.
"""

import cv2
import numpy as np



def screensaver():
    img = np.zeros((830,1550,3),dtype='uint8')
    dx,dy =1,1
    x,y = 100,100
    while True:
        # Display the image
        cv2.imshow('a',img)
        k = cv2.waitKey(10)
        img = np.zeros((830,1550,3),dtype='uint8') 
        # Increment the position
        x = x+dx
        y = y+dy
        cv2.circle(img,(x,y),20,(0,0,255),-1)
        if k != -1:
            break
        # Change the sign of increment on collision with the boundary
        if y >=830:
            dy *= -1
        elif y<=0:
            dy *= -1
        if x >=1550:
            dx *= -1
        elif x<=0:
            dx *= -1
    cv2.destroyAllWindows()



# Background Image
img1 = cv2.imread('D:/grey screen.png')
# Initialize these for text placement
i = 0 
a,b = 30,30
while True:
    cv2.imshow('a',img1)
    k = cv2.waitKey(10000)
    # If no key is pressed, display the screensaver
    if k == -1:
        screensaver()
    # Press Escape to exit
    elif k == 27:
        break
    # Otherwise write real time text on the image.
    # This is used for visualization only
    # You can use anything here.
    else:
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img1,chr(k),(a+i,b), font, 0.5,(255,255,255),2,cv2.LINE_AA)
        if a+i >= img1.shape[1]:
            b = b+15
            i = 0
        i +=10
        
cv2.destroyAllWindows()