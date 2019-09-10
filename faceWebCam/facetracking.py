import cv2
import sys
import time as ti
import numpy as np
font = cv2.FONT_HERSHEY_SIMPLEX
cascPath = sys.argv[1]
detect_smile=False
if len(sys.argv)>2: 
    if sys.argv[2]=='smile':
        detect_smile=True
        smilepath='./haarcascade_smile.xml'
        smileCascade = cv2.CascadeClassifier(smilepath)

# name = input('What is your name?')
faceCascade = cv2.CascadeClassifier(cascPath)

video_capture = cv2.VideoCapture(700)#0 + cv2.CAP_DSHOW)
print('Vcap:', video_capture, cv2.CAP_DSHOW)
image_no = 1000
for i in range(1000):
    video_capture = cv2.VideoCapture(i)
    ret, frame = video_capture.read()
    
    if ret==True:
        print('Found camera on ',i)
        break
    video_capture.release()

time_interval = 0.1
# A=ti.time()
while True:
    # Capture frame-by-frame
    
    ret, frame = video_capture.read()
    if ret==False:
        print('Cannot find camera')
        break
    print(ret)

    #print(frame)
    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #gray = cv2.equalizeHist(gray)
    gray=frame#frame=gray
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )

    # Draw a rectangle around the faces
    
    if len(faces)!=0:
        print(faces)
        
        x1 = int(faces[0][0])
        y1 = int(faces[0][1])
        x2 = int(faces[0][0]+224)#faces[0][2]))
        y2 = int(faces[0][1]+224)#+faces[0][3])+30)
        faceROI = gray[y1:y2,x1:x2,:].copy()
        print(type(faceROI))
        print(np.shape(faceROI))
        
        # if ti.time()-A > time_interval:
        #    print('Saving image no:', image_no)
        #    A = ti.time()
        #    cv2.imwrite(name+'_'+str(image_no)+'.jpg',faceROI)
        #    image_no+=1
        #gray[0:250, 0:200] = 0
        # smiles=[]
        #if detect_smile==True:
        #    smiles = smileCascade.detectMultiScale(
        #        faceROI,
        #        scaleFactor=1.1,
        #        minNeighbors=22,
        #        minSize=(30, 30)
        #    )
        
        #if faceROI.shape[0]>250 or faceROI.shape[1]>200:
        #    print('large image')
        #    cv2.putText(gray, 'Face To Big', (10,200), font, 1, (179, 255, 255), 2, cv2.LINE_AA)
        #else: 
        #    if len(smiles)>0:
        #        print('at least one is happy')
        #        for (x, y, w, h) in smiles:
        #            print(smiles[0])
        #            cv2.rectangle(faceROI, (x, y), (x+w, y+h), (0, 255, 0), 2)
        #    else:
        #        cv2.putText(gray, 'Smile', (10,240), font, 1, (179, 255, 255), 2, cv2.LINE_AA)
        #    gray[0:faces[0][3], 0:faces[0][2]]=faceROI
        #    cv2.putText(gray, 'Face', (10,200), font, 1, (179, 255, 255), 2, cv2.LINE_AA)
    
        
    else:
        gray[0:224, 0:224,:] = 0
    
    for (x, y, w, h) in faces:
        cv2.rectangle(gray, (x, y), (x+224, y+224), (0, 255, 0), 2)
    
    # Display the resulting frame
    #cv2.putText(gray, 'Time'+str(ti.time()-A), (10,300), font, 1, (179, 255, 255), 2, cv2.LINE_AA)
    cv2.imshow('Video', gray)
    #ti.sleep(2)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()