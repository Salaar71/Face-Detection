import cv2
import time
import FaceDetectionModule as fd

cap=cv2.VideoCapture(0)
pTime=0
detector=fd.FaceDetector()
while True:
    success, img= cap.read()
    img=cv2.resize(img,(750,500))
    img, bboxs= detector.findFaces(img)
    print(bboxs)
    cTime=time.time()
    fps=1/(cTime-pTime)
    pTime=cTime
    cv2.putText(img,f'FPS: {int(fps)}',(20,70),cv2.FONT_HERSHEY_PLAIN,3,(0,0,255),3)
    cv2.imshow("Image",img)
    cv2.waitKey(1)
    