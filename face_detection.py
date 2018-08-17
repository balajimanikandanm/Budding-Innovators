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
cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
num=num+1
cv2.imWrite("dataSet/User."+Id+'.'+str(num)+".jpg",gray[y:y+h,x:x+w])
cv2.imshow('frame',img)
if cv2.WaitKey(100) & 0xFF == ord('q'):
  break
elif num>20:
  break
  cam.release()
  cv2.destroyAllWindows()
