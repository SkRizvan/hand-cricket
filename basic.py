import cv2 as cv
import mediapipe as mp
import time
import handTrackingModule as htm
import math

def main(textin=""):
    fingercount1=0
    fp=open("5fingers.txt","w")
    cam = cv.VideoCapture(0)
    cam.set(3,480)
    cam.set(4,640)
    pTime=0
    detect=htm.HandDetector(max_hands=1,min_detection_confidence=0.7)
    countthumb=0
    countindex=0
    countmiddle=0
    countring=0
    countpinky=0
    sumthumb=0
    sumindex=0
    summiddle=0
    sumring=0
    sumpinky=0
    stime=time.time()
    print(stime)
    while True:
        etime=time.time()
        if etime-stime>5:
            break
        fingers=""
        success,img=cam.read()
        #print(img.shape)
        cv.putText(img,textin,(50,50),cv.FONT_HERSHEY_PLAIN,2,(255,0,0),1)
        cTime=time.time()
        fps=1/(cTime-pTime)
        pTime=cTime
        cv.rectangle(img,(200,200),(450,450),(255,0,0),thickness=4)
        cv.resize(img,(600,600))
        #cv.putText(img,str(int(fps)),(30,50),cv.FONT_HERSHEY_COMPLEX,2,(0,255,0),3)
        detect.drawhands(img)
        list_of_coordinates=detect.coordinates(img)
        if len(list_of_coordinates)!=0:
            x0,y0=list_of_coordinates[0][1],list_of_coordinates[0][2]
            x4, y4 = list_of_coordinates[4][1], list_of_coordinates[4][2]
            x8, y8 = list_of_coordinates[8][1], list_of_coordinates[8][2]
            x12, y12 = list_of_coordinates[12][1], list_of_coordinates[12][2]
            x16, y16 = list_of_coordinates[16][1], list_of_coordinates[16][2]
            x20, y20 = list_of_coordinates[20][1], list_of_coordinates[20][2]
            thumbdistance=math.hypot(x4-x0,y4-y0)
            indexfingerdistance=math.hypot(x8-x0,y8-y0)
            middlefingerdistance=math.hypot(x12-x0,y12-y0)
            ringfingerdistance=math.hypot(x16-x0,y16-y0)
            pinkyfingerdistance=math.hypot(x20-x0,y20-y0)
            if thumbdistance>140:
                fingers+=str(1)
            else:
                fingers+=str(0)
            if indexfingerdistance>150:
                fingers+=str(1)
            else:
                fingers+=str(0)
            if middlefingerdistance>150:
                fingers+=str(1)
            else:
                fingers+=str(0)
            if ringfingerdistance>150:
                fingers+=str(1)
            else:
                fingers+=str(0)
            if pinkyfingerdistance>150:
                fingers+=str(1)
            else:
                fingers+=str(0)
            #print(fingers)
        def number_of_fingers(fingers):
            if fingers=='00001' or fingers=='00010' or fingers=='00100' or fingers=='01000':
                return 1
            elif fingers=='01001' or fingers=='01010' or fingers=='01100' or fingers=='00110' or fingers=='00101'or fingers=='00011':
                return 2
            elif fingers=='01110' or fingers=='00111' or fingers=='01101' or fingers=='01011':
                return 3
            elif fingers=='01111':
                return 4
            elif fingers=='11111':
                return 5
            elif fingers=='10000':
                return 6
            else:
                return 0
        cv.putText(img,f'number of fingers {number_of_fingers(fingers)}',(50,150),cv.FONT_HERSHEY_COMPLEX_SMALL,2,(255,0,0))
            
        if len(list_of_coordinates)!=0:
            sumthumb+=thumbdistance
            sumindex+=indexfingerdistance
            sumring+=ringfingerdistance
            summiddle+=middlefingerdistance
            sumpinky+=pinkyfingerdistance
            countthumb+=1
            countindex+=1
            countmiddle+=1
            countring+=1
            countpinky+=1
            # print(f'thumb distance {thumbdistance}')
            # print(f'index finger distance {indexfingerdistance}')
            # print(f'middle finger distance {middlefingerdistance}')
            # print(f'ring finger distance {ringfingerdistance}')
            # print(f'pinky finger distance {pinkyfingerdistance}')
            fp.write(f'thumb distance {thumbdistance}\n')
            fp.write(f'index finger distance {indexfingerdistance}\n')
            fp.write(f'middle finger distance {middlefingerdistance}\n')
            fp.write(f'ring finger distance {ringfingerdistance}\n')
            fp.write(f'pinky finger distance {pinkyfingerdistance}\n')
        fingercount1=0
        def fingercount():
            fingercount1=number_of_fingers(fingers)
            print(fingercount1)
            return fingercount1
        
        for i in range(6):
            if len(list_of_coordinates)!=0:
                x= list_of_coordinates[i*4][1]
                y =list_of_coordinates[i * 4][2]
                cv.circle(img,(x,y),7,(255,0,255),-1)
                if i==1:
                    distance=math.hypot(x-x0,y-y0)
       
        cv.imshow('img',img)
        cv.waitKey(1)
        #if cv.waitKey(1) & 0xFF==ord('d'):
            #break
    cv.destroyAllWindows()

    if len(list_of_coordinates)!=0:
        avgthumb=sumthumb//countthumb
        avgindex=sumindex//countindex
        avgmiddle=summiddle//countmiddle
        avgring=sumring//countring
        avgpinky=sumpinky//countpinky
       # print(f'average thumb {avgthumb}\n average index {avgindex}\n average middle {avgmiddle}\n average ring {avgring}\n average pinky {avgpinky}\n')
        fp.write(f'average thumb {avgthumb}\n average index {avgindex}\n average middle {avgmiddle}\n average ring {avgring}\n average pinky {avgpinky}\n')
        fp.close()
    return fingercount()
        


if __name__ == "__main__":
    main()