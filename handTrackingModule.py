import cv2 as cv
import mediapipe as mp
import time
 
class HandDetector():
    def __init__(self,mode=False,max_hands=2,model_complexity=1,min_detection_confidence=0.5,min_tracking_confidence=0.5):
        self.mode=mode
        self.max_hands=max_hands
        self.model_complexity=model_complexity
        self.min_detection_confidence=min_detection_confidence
        self.min_tracking_confidence=min_tracking_confidence
        self.mphands=mp.solutions.hands
        self.hands=self.mphands.Hands(self.mode,self.max_hands,self.model_complexity,self.min_detection_confidence,self.min_tracking_confidence)
        self.draw=mp.solutions.drawing_utils
    def drawhands(self,img):
        imgrgb=cv.cvtColor(img,cv.COLOR_BGR2RGB)
        self.results=self.hands.process(imgrgb)
        if self.results.multi_hand_landmarks:
            for self.handlms in self.results.multi_hand_landmarks:
                self.draw.draw_landmarks(img,self.handlms,self.mphands.HAND_CONNECTIONS)
        return img
    def coordinates(self,img):
        self.lmlist=[]
        imgrgb=cv.cvtColor(img,cv.COLOR_BGR2RGB)
        self.results=self.hands.process(imgrgb)
        if self.results.multi_hand_landmarks:
            for handlms in self.results.multi_hand_landmarks:
                for id,lm in enumerate(handlms.landmark):
                    # print(id,lm)
                    h,w,c=img.shape
                    cx,cy=int(lm.x*w),int(lm.y*h)
                    #print(id,"\n"," " ,cx,cy)
                    self.lmlist.append([id,cx,cy])
        return self.lmlist