# importing the libraries

import cv2 
import numpy as np

image=cv2.imread('#image_name_with_extension') # Reading Image

win_name='my application' # Kernal_Name

cv2.imshow(win_name,image) # Show_Image 

cv2.waitKey(0)  # For Terminating the Kernal

cv2.destroyAllWindows() # Destroy all windows