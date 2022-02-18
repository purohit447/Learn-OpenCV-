# importing the libraries
import cv2
import numpy as np

canvas = np.zeros((500,500,3)) #image channels (3rd dimension is for BGR info) 

# Line(img_name, (coordinates x1,y1), (coordinates x2,y2),(Blue,Green,Red), thickness, Line_Type)
# type 4 and 8 are application of bresenham algorithm
cv2.line(canvas, (120,110),(450,450),(255,250,0),3, cv2.LINE_4)
cv2.line(canvas, (200,210),(450,450),(255,250,0),3, cv2.LINE_8)
# type AA is the application of gausian filtering
cv2.line(canvas, (100,140),(400,450),(255,250,0),3, cv2.LINE_AA)

cv2.rectangle(canvas, (210,10),(370,150),(250,0,0),-1) # rectangle(image_name,((diagonal:1) x1,y1),((diagonal:2) x2,y2), (B,G,R), fill/thickness)
cv2.circle(canvas,(150,300),100,(0,255,0),-3) #circle (image_name, ((center)x,y), radius, (B,G,R), thickness/fill)
cv2.arrowedLine(canvas,(400,450),(470,450),(255,255,0),tipLength=0.3) # arrowLine(image_name,(x1,y1),(x2,y2),(B,G,R),tipLenght)

cv2.imshow('karan',canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()
