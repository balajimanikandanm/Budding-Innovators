import cv2
cam=cv2.VideoCapture(0)
detector=cv2.CascadeClassifier('frontface.xml')
Id=input('enter id')
num=0
while(true):
ret,img=cam.read()
gray=cv2.cvtColor(img,cv2.COLOR.BGR2GRAY)
faces=detector.detectMultiscale(gray,1.3,5)
for(x,y,w,h) in faces:
cv2.rectangle(img,(x,y),(x+w,y+h))
