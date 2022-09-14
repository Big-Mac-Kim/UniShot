import cv2
import numpy as np
from tensorflow.compat.v1.keras.models import load_model
import time


cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)


MODEL_FILENAME= "D:/oneshot/0506-Z-check.hdf5"

model = load_model(MODEL_FILENAME)# 自動建立目錄
print("model loaded")

frame=np.zeros((480,640,3),dtype=int)
print("input baseframe")
for i in range(0,10):
    ret, img = cap.read()  
    img.astype(int)
    if ret==True:
        frame=frame+img
    else:
        print("cam was broken")
        
frame=frame//10
frame=np.array(frame, dtype=np.uint8)

asize=frame.shape
b=int((asize[1]-asize[0])/2)
frame=frame[0:asize[0],b:b+asize[0]]



frame=cv2.resize(frame, (400, 400), interpolation=cv2.INTER_AREA)
aa=np.copy(frame)  

cv2.imshow("s",frame)
base_frame=cv2.resize(frame, (64, 64), interpolation=cv2.INTER_AREA)


base_frame=base_frame/255.0 



base_frame = np.expand_dims(base_frame, axis=0)

a=0
while True:
    Frame=aa.copy()
    
    if a==0:    
        start_time=time.time()
        
    ret, frame1 = cap.read()  
    asize=frame1.shape
    b=int((asize[1]-asize[0])/2)
    frame1=frame1[0:asize[0],b:b+asize[0]]
    
  #  zommed_frame=frame1#[140:140+200,140:140+200]
    zommed_frame=cv2.resize(frame1, (400, 400), interpolation=cv2.INTER_AREA)
    zommed_frame= zommed_frame[100:300,100:300,:]
    
    
    cv2.imshow("ss",  zommed_frame)    
    zommed_frame=cv2.resize(zommed_frame, (64, 64), interpolation=cv2.INTER_AREA)
    
    zommed_frame=zommed_frame/255.0    
  
    zommed_frame= np.expand_dims(zommed_frame, axis=0)  
   
    
    Predicted_Probability = model.predict( [ zommed_frame,base_frame])
    X=np.argmax(Predicted_Probability,axis=1)
    X=int(X)
    print("X:"+str(X)) 

     
    Frame = cv2.rectangle(    Frame , (X*10,100), (X*10+200,100+200),(0,255,255), 2)

        
    cv2.imshow("ssSS",      Frame )   
    
    
    a=a+1
    if a==30:
        end_time=time.time()
        run_time=end_time-start_time
        print("FPS:"+str(30/run_time))
        a=0
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()

