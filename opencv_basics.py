# To first start with opencv , one must install the necessary extensions 
# after insatllations and importing of opencv , we are going to start our coding. for simplicity purposes , i'm dividing this code into 2 sections- Setup and Execution.
#in setup , we write all the initial values of the entities and in execution , we will be coding the execution part
    
# Setup phase
#Importing of necessary libraries

import cv2  
import numpy as np


#Reading of the image 
image = cv2.imread("D:\grey screen.png",0)

#Displaying the window and labelling it
window_name = 'Image'


#Initial parameters required for the putText()----[for inserting text] command
font = cv2.FONT_HERSHEY_SIMPLEX
org = (50, 50)
org2 = (200,200) 
fontScale = 1
color = (255, 0, 0)
thickness = 2


#Initial parameters for the shape drawn(rectangle)
start_point = (400,400)
end_point = (600,600)
thickness = 2

#Execution phase
# Using cv2.putText() and cv2.rectangle method to insert text and shape respectively
#Moving of the entities 

image = cv2.putText(image, 'OpenCV is very useful in cases of face detection and security purposes', org, font,fontScale, color, thickness, cv2.LINE_AA)
image = cv2.putText(image,'made on 09-June-2022',org2,font,fontScale,color,thickness,cv2.LINE_AA)
image = cv2.rectangle(image,start_point,end_point,color,thickness)
cv2.imshow(window_name,image)
cv2.waitkey(0)

#Here we are taking the 3 variables , entity - for the object to be moved , x_coordinate - for change in x direction , y_direction - for change in y direction
entity = input("Enter the entity to be moved (Text , date , rectangle) ")
x_coordinate = int(input("Enter the number of units ,the entity needs to be in the  horizontal direction(Negative for left direction) "))
y_coordinate = int(input("Enter the number of units ,the entity needs to be in the  vertical direction(Negative for downward direction) "))

#checking the entity to be moved and then using x coordinate and y coordinate, we move the object
if entity == "text" or "Text":
    org = (50+x_coordinate,50+y_coordinate)
    image = cv2.putText(image, 'OpenCV is very useful in cases of face detection and security purposes', org, font,fontScale, color, thickness, cv2.LINE_AA)
    cv2.imshow(window_name,image)
elif entity == "date" or "Date":
    org2 = (200+x_coordinate,200+y_coordinate)
    image = cv2.putText(image,'made on 09-June-2022',org2,font,fontScale,color,thickness,cv2.LINE_AA)
    cv2.imshow(window_name,image)
    cv2.waitkey(0)
elif entity == "Rectangle" or "rectangle":
    start_point = (400+x_coordinate , 400+y_coordinate)
    end_point = (600+x_coordinate , 600+y_coordinate)
    image = cv2.rectangle(image,start_point,end_point,color,thickness)
    cv2.imshow(window_name,image)
else:
    print("No such entity found")


