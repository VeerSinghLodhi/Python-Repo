import cv2
data=cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
img=cv2.imread("C:\\Users\\Veersingh Lodhi\\Downloads\\Pawan Bhaiya pictures\\PAWAN-PHOTO.jpg")
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
coords=data.detectMultiScale(gray)
print(coords)
for (x,y,w,h) in coords:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)

cv2.imshow("Detector",img)
cv2.waitKey()