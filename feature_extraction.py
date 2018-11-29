 
image = cv2.imread("/home/mcaadmin/blueinfected/Im001_1.png")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
thresh = 20
binary = cv2.threshold(gray, thresh, 300, cv2.THRESH_BINARY)[1]
cv2.imwrite("/home/mcaadmin/binaryinfected/Im001_1.png",binary)



#contour

image, contours, hierarchy = cv2.findContours(binary, cv2.RETR_EXTERNAL,
cv2.CHAIN_APPROX_SIMPLE)
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
if numOfContours>6 :
    e=1
else:
    cnt = contours[k]
    ellipse = cv2.fitEllipse(cnt)
    (center,axes,orientation) = ellipse
    majoraxis_length = max(axes)
    minoraxis_length = min(axes)
    e=minoraxis_length/majoraxis_length
print("perimeter:",perimeter[k])

print("eccentricity:",e)
contour = cnt.astype(np.float32)
    


