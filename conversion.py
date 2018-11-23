import cv2
import numpy as np
import os
import glob
#img_dir = "/home/mcaadmin/ALL_IDB1/im" # Enter Directory of all images
#data_path = os.path.join(img_dir,'*g')
#files = glob.glob(data_path)
#for f1 in files:  
image = cv2.imread("/home/mcaadmin/infected/Im001_1.png")
#while(1):

    # Convert BGR to HSV
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    # define range of blue color in HSV
lower_blue = np.array([80,120,70])
upper_blue = np.array([305,300,220])
    # Threshold the HSV image to get only blue colors
mask = cv2.inRange(hsv, lower_blue, upper_blue)
    # Bitwise-AND mask and original image
res = cv2.bitwise_and(image,image, mask= mask)
    #cv2.imshow('frame',frame)
cv2.imwrite("/home/mcaadmin/blueinfected/Im001_1.png",res)
    #cv2.imshow('res',res)


 
image = cv2.imread("/home/mcaadmin/blueinfected/Im001_1.png")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
thresh = 20
binary = cv2.threshold(gray, thresh, 300, cv2.THRESH_BINARY)[1]
cv2.imwrite("/home/mcaadmin/binaryinfected/Im001_1.png",binary)


