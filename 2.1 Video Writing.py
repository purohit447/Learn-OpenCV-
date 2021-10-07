# importing the libraries
import cv2
import numpy as np

video = cv2.VideoCapture(0)  # Video Reading

win_name = 'my application'  # Kernel_Name
height = video.get(cv2.CAP_PROP_FRAME_HEIGHT) # to get frame height
width = video.get(cv2.CAP_PROP_FRAME_WIDTH) # to get frame width
fps = video.get(cv2.CAP_PROP_FPS) # to get frames per second

fourcc = cv2.VideoWriter_fourcc(*'MJPG') # fourcc is a 4 char code used to define extension for videos input.
output = cv2.VideoWriter('karan4.avi', fourcc, fps, (int(width),int(height)))   # width, height should be in same order and type-casted
frames =video.get(cv2.CAP_PROP_FRAME_COUNT)   # Total Frames


open = video.isOpened()   # if Opened Successfully
if(open):
    while(video.isOpened()):
        it,frame=video.read()   # Reading frames
        if(it == True):   # 'it' is a Boolean type

            cv2.imshow(win_name, frame)   # Show Frames
            output.write(frame)  # video writing

            if (cv2.waitKey(3) == 27):
                break   # Break on pressing ECS key

output.release()  # release output instance
video.release()   # release video instance
cv2.destroyAllWindows()    # destroy all windows