import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
"""
After the import of the necessary libraries , we define a function called animation. Then for each rectangle to be moved , we are using for loops to run through the coordinates and 
show the rectangle . Here we are using two variables called dx and dy to move the rectangles around.
"""

def animation():
    dx,dy = 0,0
    for i in range(1760):
        if i == 0:
            img = np.zeros((830,1550,3),dtype='uint8')
            sq1 = cv.rectangle(img ,(300,300+dy),(500,500+dy),(0,255,0),-1)
            sq2 = cv.rectangle(img ,(520,300),(720,500),(0,255,0),-1)
            sq3 = cv.rectangle(img ,(740,300),(940,500),(0,255,0),-1)
            sq4 = cv.rectangle(img ,(300,80+dy),(500,280+dy),(0,255,0),2)
            dy +=1
        elif i == 220:
            img = np.zeros((830,1550,3),dtype='uint8')
            sq1 = cv.rectangle(img ,(300,300+dy),(500,500+dy),(0,255,0),2)
            sq2 = cv.rectangle(img ,(520,300),(720,500),(0,255,0),-1)
            sq3 = cv.rectangle(img ,(740,300),(940,500),(0,255,0),-1)
            sq4 = cv.rectangle(img ,(300,80+dy),(500,280+dy),(0,255,0),-1)
            dy +=1
        elif i >0 and i < 220:
            img = np.zeros((830,1550,3),dtype='uint8')
            sq1 = cv.rectangle(img ,(300,300+dy),(500,500+dy),(0,255,0),2)
            sq2 = cv.rectangle(img ,(520,300),(720,500),(0,255,0),-1)
            sq3 = cv.rectangle(img ,(740,300),(940,500),(0,255,0),-1)
            sq4 = cv.rectangle(img ,(300,80+dy),(500,280+dy),(0,255,0),2)
            dy +=1
        elif i > 220 and i <440:
            img = np.zeros((830,1550,3),dtype='uint8')
            sq1 = cv.rectangle(img ,(300+dx,520),(500+dx,720),(0,255,0),2)
            sq2 = cv.rectangle(img ,(520,300),(720,500),(0,255,0),-1)
            sq3 = cv.rectangle(img ,(740,300),(940,500),(0,255,0),-1)
            sq4 = cv.rectangle(img ,(300,300),(500,500),(0,255,0),-1)
            dx += 1   
        elif i == 440:
            img = np.zeros((830,1550,3),dtype='uint8')
            sq1 = cv.rectangle(img ,(300+dx,520),(500+dx,720),(0,255,0),2)
            sq2 = cv.rectangle(img ,(520,300),(720,500),(0,255,0),-1)
            sq3 = cv.rectangle(img ,(740,300),(940,500),(0,255,0),-1)
            sq4 = cv.rectangle(img ,(300,300),(500,500),(0,255,0),-1) 
            dy = 0
        elif i > 440 and i < 660:
            img = np.zeros((830,1550,3),dtype='uint8')
            sq1 = cv.rectangle(img ,(520,520-dy),(720,720-dy),(0,255,0),2)
            sq2 = cv.rectangle(img ,(520,300-dy),(720,500-dy),(0,255,0),2)
            sq3 = cv.rectangle(img ,(740,300),(940,500),(0,255,0),-1)
            sq4 = cv.rectangle(img ,(300,300),(500,500),(0,255,0),-1) 
            dy += 1       
        elif i == 660:
            img = np.zeros((830,1550,3),dtype='uint8')
            sq1 = cv.rectangle(img ,(520,520-dy),(720,720-dy),(0,255,0),-1)
            sq2 = cv.rectangle(img ,(520,300-dy),(720,500-dy),(0,255,0),2)
            sq3 = cv.rectangle(img ,(740,300),(940,500),(0,255,0),-1)
            sq4 = cv.rectangle(img ,(300,300),(500,500),(0,255,0),-1)
            dx = 0  
        elif i > 660 and i < 880:
            img = np.zeros((830,1550,3),dtype='uint8')
            sq1 = cv.rectangle(img ,(520,520-dy),(720,720-dy),(0,255,0),-1)
            sq2 = cv.rectangle(img ,(520+dx,300-dy),(720+dx,500-dy),(0,255,0),2)
            sq3 = cv.rectangle(img ,(740,300),(940,500),(0,255,0),-1)
            sq4 = cv.rectangle(img ,(300,300),(500,500),(0,255,0),-1) 
            dx += 1      
        elif i == 880:
            img = np.zeros((830,1550,3),dtype='uint8')
            sq1 = cv.rectangle(img ,(520,520-dy),(720,720-dy),(0,255,0),-1)
            sq2 = cv.rectangle(img ,(520+dx,300-dy),(720+dx,500-dy),(0,255,0),2)
            sq3 = cv.rectangle(img ,(740,300),(940,500),(0,255,0),-1)
            sq4 = cv.rectangle(img ,(300,300),(500,500),(0,255,0),-1)
            dy = 0
        elif i > 880 and i < 1100:
            img = np.zeros((830,1550,3),dtype='uint8')
            sq1 = cv.rectangle(img ,(520,300),(720,500),(0,255,0),-1)
            sq2 = cv.rectangle(img ,(740,80+dy),(940,280+dy),(0,255,0),2)
            sq3 = cv.rectangle(img ,(740,300+dy),(940,500+dy),(0,255,0),2)
            sq4 = cv.rectangle(img ,(300,300),(500,500),(0,255,0),-1)
            dy += 1  
        elif i == 1100:
            img = np.zeros((830,1550,3),dtype='uint8')
            sq1 = cv.rectangle(img ,(520,300),(720,500),(0,255,0),-1)
            sq2 = cv.rectangle(img ,(740,80+dy),(940,280+dy),(0,255,0),2)
            sq3 = cv.rectangle(img ,(740,300+dy),(940,500+dy),(0,255,0),2)
            sq4 = cv.rectangle(img ,(300,300),(500,500),(0,255,0),-1)
            dx = 0
        elif i > 1100 and i < 1320:
            img = np.zeros((830,1550,3),dtype='uint8')
            sq1 = cv.rectangle(img ,(520,300),(720,500),(0,255,0),-1)
            sq2 = cv.rectangle(img ,(740,300),(940,500),(0,255,0),-1)
            sq3 = cv.rectangle(img ,(740-dx,520),(940-dx,720),(0,255,0),2)
            sq4 = cv.rectangle(img ,(300,300),(500,500),(0,255,0),-1)
            dx += 1 
        elif i == 1320:
            img = np.zeros((830,1550,3),dtype='uint8')
            sq1 = cv.rectangle(img ,(520,300),(720,500),(0,255,0),-1)
            sq2 = cv.rectangle(img ,(740,300),(940,500),(0,255,0),-1)
            sq3 = cv.rectangle(img ,(520,520),(720,720),(0,255,0),2)
            sq4 = cv.rectangle(img ,(300,300),(500,500),(0,255,0),-1)
            dy = 0
        elif i > 1320 and i <1540:
            img = np.zeros((830,1550,3),dtype='uint8')
            sq1 = cv.rectangle(img ,(520,300-dy),(720,500-dy),(0,255,0),2)
            sq2 = cv.rectangle(img ,(740,300),(940,500),(0,255,0),-1)
            sq3 = cv.rectangle(img ,(520,520-dy),(720,720-dy),(0,255,0),2)
            sq4 = cv.rectangle(img ,(300,300),(500,500),(0,255,0),-1)
            dy += 1
        elif i == 1540:
            img = np.zeros((830,1550,3),dtype='uint8')
            sq1 = cv.rectangle(img ,(520,80),(720,280),(0,255,0),2)
            sq2 = cv.rectangle(img ,(740,300),(940,500),(0,255,0),-1)
            sq3 = cv.rectangle(img ,(520,300),(720,500),(0,255,0),-1)
            sq4 = cv.rectangle(img ,(300,300),(500,500),(0,255,0),-1) 
            dx = 0
        elif i > 1540 and i < 1760:
            img = np.zeros((830,1550,3),dtype='uint8')
            sq1 = cv.rectangle(img ,(520-dx,80),(720-dx,280),(0,255,0),2)
            sq2 = cv.rectangle(img ,(740,300),(940,500),(0,255,0),-1)
            sq3 = cv.rectangle(img ,(520,300),(720,500),(0,255,0),-1)
            sq4 = cv.rectangle(img ,(300,300),(500,500),(0,255,0),-1) 
            dx += 1  
        elif i == 1760:
            img = np.zeros((830,1550,3),dtype='uint8')
            sq1 = cv.rectangle(img ,(520-dx,80),(720-dx,280),(0,255,0),2)
            sq2 = cv.rectangle(img ,(740,300),(940,500),(0,255,0),-1)
            sq3 = cv.rectangle(img ,(520,300),(720,500),(0,255,0),-1)
            sq4 = cv.rectangle(img ,(300,300),(500,500),(0,255,0),-1)
            
        cv.imshow("window",img) 
        cv.waitKey(10)
    

while True:
    animation()    