# importing the libraries
import cv2
import numpy as np

canvas = np.zeros((500,500,3)) #image channels (3rd dimension is for BGR info) 

pts = np.array([[250, 5], [220, 80], [280,80], [250,250]], np.int32) # (x',y') the points to be used as joints 
pts = pts.reshape((-1,1,2))  # reshaping the array to be passsed through polylines function 
cv2.polylines(canvas, [pts], True, (0,255,0), 3) # polylines(image_name, [array], True/false,(B,G,R),thickness)
print(pts)

TextCanvas = np.zeros((800,800)) #2D canvas

fonts = [cv2.FONT_HERSHEY_COMPLEX,    # All 8 text fonts in OpenCV 
         cv2.FONT_HERSHEY_DUPLEX,
         cv2.FONT_HERSHEY_PLAIN,
         cv2.FONT_HERSHEY_SIMPLEX,
         cv2.FONT_HERSHEY_TRIPLEX,
         cv2.FONT_HERSHEY_COMPLEX_SMALL,
         cv2.FONT_HERSHEY_SCRIPT_COMPLEX,
         cv2.FONT_HERSHEY_SCRIPT_SIMPLEX]

position = (10,30)  #position of the text in page.

for i in range(0,8):
	cv2.putText(TextCanvas,"THIS IS OPENCV !", position, fonts[i], 1,(255,0,0), 2, cv2.LINE_AA) # putText(image_name, text, position, font-type, font-face, (B,G,R), thickness, line-type)
	position = (position[0], position[1] + 30)   # moving position down to avoid text over-writing  

	cv2.putText(TextCanvas,"THIS IS OPENCV!".lower(), position, fonts[i], 1, (255,0,0), 2, cv2.LINE_AA)# putText(image_name, text.lower(), position, font-type, font-face, (B,G,R), thickness, line-type)
	position = (position[0], position[1] + 30)  # moving position down to avoid text over-writing  


cv2.imshow('karan',canvas)  # show canvas 
cv2.waitKey(0)
cv2.imshow('karan',TextCanvas)  # show text canvas
cv2.waitKey(0)
cv2.destroyAllWindows() 