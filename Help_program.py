from cvzone.HandTrackingModule import HandDetector
import cv2
import time
import pyttsx3
engine = pyttsx3.init()


engine.setProperty("rate", 150)  
engine.setProperty("volume", 1.0)
cap=cv2.VideoCapture(0)
model=HandDetector()
while True:
    status,photo=cap.read()
    cv2.imshow("pic1",photo)
    if cv2.waitKey(10)==13:
        break

    hand=model.findHands(photo,draw=False)
    if hand:
        handPhoto=hand[0]
#       print(handPhoto)
        fingerlist=model.fingersUp(handPhoto)        
        if fingerlist==[0,1,1,1,1]:
            engine.say("namaste")
            engine.runAndWait()
            print("namaste")
            time.sleep(2)
        elif fingerlist==[1,0,0,0,0]:
            engine.say("Good job")
            engine.runAndWait()
            print("Good job")
            time.sleep(2)
        elif fingerlist==[0,1,1,0,0]:
            engine.say("Pleasure meeting with you")
            engine.runAndWait()
            print("Pleasure meeting with you")
            time.sleep(2)
        elif fingerlist==[0,1,1,0,0]:
            engine.say("Perfect")
            engine.runAndWait()
            print("Perfect")
            time.sleep(2)
        elif fingerlist==[1,1,0,0,1]:
            engine.say("I love Vimal Sir")
            engine.runAndWait()
            print("I love Vimal Sir")
            time.sleep(2)
        elif fingerlist==[0,0,0,0,0]:
            engine.say("Sorry")
            engine.runAndWait()
            print("Sorry")
            time.sleep(2)
        elif fingerlist==[0,1,0,0,0]:
            engine.say("Help")
            engine.runAndWait()
            print("Help")
            time.sleep(2)
        else:
            print("dont support")
            time.sleep(2)
        


  
cv2.destroyAllWindows()
cap.release()
