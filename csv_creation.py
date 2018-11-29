import cv2
import numpy as np
import os
import glob
import csv

#data = []

fileNameList = []
image_list = os.listdir("dataset/")
for files in image_list:
    fileName, extension = os.path.splitext(files)
    fileNameList.append(fileName)
o=0
img_dir = "dataset/"
data_path = os.path.join(img_dir,'*g')
files = glob.glob(data_path)
csvTitle = [['Image Name', 'Area', 'Perimeter','Eccentricity','Prediction']]
csvData = []
for f1 in files:
    binary= cv2.imread(f1,0) 
    image, contours, hierarchy = cv2.findContours(binary, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
#img = cv2.drawContours(image, contours, -1, (0,0, 255), 1)

    numOfContours = len(contours)   #number of contours
    print("numOfContours:",numOfContours)
    area = []
    perimeter=[]
    count = 0
    for count in range(numOfContours) :
        cv2.drawContours(binary, contours, -1, (20,255,60), 1)  #draw contours
        cnt = contours[count]
        area.append(cv2.contourArea(cnt))
        peri = cv2.arcLength(cnt,True)
        perimeter.append(peri)
   
        count+=1
    a=max(area)
    print("area:",a)   #gives the largest area
    for i in range(numOfContours) :
        if area[i]==a:
            k=i
    if numOfContours<22 or a<7000:
        e=1
    else:
        cnt = contours[k]
        ellipse = cv2.fitEllipse(cnt)
        (center,axes,orientation) = ellipse
        majoraxis_length = max(axes)
        minoraxis_length = min(axes)
        e=minoraxis_length/majoraxis_length
    print("perimeter:",perimeter[k])
    #print(eccentricity)
    print("eccentricity:",e)
    contour = cnt.astype(np.float32)
    
    if e==1:
        pred=0
    else:
        pred=1
        
    csvData.append([fileNameList[o], a, perimeter[k], e,pred])
    o=o+1
    with open('dr_features.csv', 'w') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerows(csvTitle)
        writer.writerows(csvData)
    #print(csvTitle)
    #print(csvData)
c = cv2.waitKey(0);
if c == 27:           #wait for ESC key to exit
    cv2.destroyAllWindows();
    


