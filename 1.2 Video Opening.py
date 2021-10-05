# importing the libraries
import cv2
import numpy as np

video=cv2.VideoCapture('#Video_name_with_extension') # Video Reading

win_name='my application' # Kernel_Name

frames=video.get(cv2.CAP_PROP_FRAME_COUNT) # Total Frames

frames=frames-1 # Indexing Starts from zero
frame_count=0 # Frame Count

open=video.isOpened() # if Opened Successfully
if(open):
    while(video.isOpened()): 
        it,frame=video.read() # Reading frames 
        if(it==True): # 'it' is a Boolean type

            cv2.imshow(win_name, frame) # Show Frames
            frame_count=frame_count+1 # frame Count 

            if (cv2.waitKey(3) == 27 or frames == frame_count): 
                break # Break on either pressing ECS key or on the last frame

video.release() # release video instance 
cv2.destroyAllWindows() # Destroy all windows
