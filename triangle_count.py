import numpy as np
import cv2 as cv
import math

def triangle_count(filename):

    img = cv.imread(filename)
    gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    dst = cv.cornerHarris(gray,2,3,0.04)
    # visualize the corners
    mask = np.zeros_like(gray)
    mask[dst>0.01*dst.max()] = 255

    # storing coordinate positions of all points in a list
    coordinates = np.argwhere(mask)
    coor_list = coordinates.tolist()

    # points beyond this threshold are preserved
    thresh = 20

    # function to compute distance between 2 points
    def distance(pt1, pt2):
        (x1, y1), (x2, y2) = pt1, pt2
        dist = math.sqrt( (x2 - x1)**2 + (y2 - y1)**2 )
        return dist

    # 
    coor_list_2 = coor_list.copy()

    # iterate for every 2 points
    i = 1    
    for pt1 in coor_list:
        for pt2 in coor_list[i::1]:
            if(distance(pt1, pt2) < thresh):
            # to avoid removing a point if already removed
                try:
                    coor_list_2.remove(pt2)      
                except:
                    pass
        i+=1

    # draw final corners
    img2 = img.copy()
    for pt in coor_list_2:
        img2 = cv.circle(img2, tuple(reversed(pt)), 2, (0, 0, 255), -1)
      

    # To find the number of possible triangles
    if (coor_list_2[0][1])/2 != coor_list_2[2][1]:
        if coor_list_2[0][1] == coor_list_2[3][1]:
            no_of_triangle = 0 
            n = int((-1+math.sqrt(1+8*(len(coor_list_2))))/2) 
            for i in range(n):
                no_of_triangle += i**2 
            img2 = cv.putText(img2,str(no_of_triangle),(100,100),cv.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 0), 3)
            cv.imshow('dst',img2)
        else:
            no_of_triangle = 6*(len(coor_list_2)-1)/4
            img2 = cv.putText(img2,str(no_of_triangle),(100,100),cv.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 0), 3)
            cv.imshow('dst',img2)
     
        
        
    if cv.waitKey(0) & 0xff == 27:
            cv.destroyAllWindows()

file_name1 = 'Triangle count\CV Traingles Task Test Image 1.jpg'
triangle_count(file_name1)  
file_name2 = 'Triangle count\CV Traingles Task Test Image 2.jpg' 
triangle_count(file_name2)     