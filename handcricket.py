import random as r  
import cv2 as cv
from cv2 import projectPoints
import mediapipe as mp
import time
import handTrackingModule as htm
import math
import basic as bs
print("Welcome to Odd OR Even game! \n")
for i in range(0,3):
    print(i)
print("Get set go")
ball=0
balls=1
x=bs.main("Number of overs")
print(x,"overs")
while x!=1 and x!=2 and x!=3 and x!=4 and x!=5 and x!=6:
    x=bs.main("Enter again")
    print(x,"overs while ")
if x==2:
    balls=12
elif x==5:
    balls=30
elif x==6 or x==1 or x==3 or x==4:
    ball=1
else:
    print("enter correct choice")
dec1=bs.main("choose odd or even")
if dec1==1 or dec1==3 or dec1==5:
    dec="odd"
    print(f"your choice {dec}")
elif dec1==2 or dec1==4 or dec1==6:
    dec="even"  
    print(f"your choice {dec}")
t1=bs.main("choose any number:")
print("your number:",t1)
t2=r.randint(1,6)
print(f"AI input: {t2}")
toss=t1+t2

if toss%2 == 0:
    dec="even"
else:
    dec="odd"
if dec1==dec:
    play=bs.main("Batting(1) or Bowling(2)? ")
    print(f"your choice is :{play}")
else:
    play=r.randint(1,2)
if play==1:
    print("You are batting!")
else:
    print("You are bowling!")
#-----------------------------------------------------------------------------------------------
balls1=balls
if play==1:
    runs1=0
    while balls>0 or ball==1:
        r1=bs.main("bat score: ")
        print(f"bat score:{r1}")
        r2=r.randint(1,6)
        print(f"AI input: {r2}")
        if r1==r2:
            print(f"OUT!!! \nYour Score: {runs1}")
            break
        elif r1>=1 and r1<=6:
            runs1+=r1
            print(f'Current score :{runs1}')
        else:
            print("Enter correct choice")
        if x==2 or x==5:
            balls-=1
            print(f"Balls remaining {balls}")

    print("Bowl and beat AI")
    runs2 = 0
    balls2=balls1
    while runs1>=runs2 and (balls2>0 or ball==1):
        if(runs1-runs2>0):
                print(f"required score:{runs1-runs2}")
        
        r1 = bs.main("bowl score: ")
        print(f"bowl score:{r1}")
        r2 = r.randint(1, 6)
        print(f"AI input: {r2}")
        if r1 == r2:
            print(f"OUT!!! \nAI Score: {runs2}\nYour Score: {runs1}\nYou Won\n")
            break
        elif r2>=1 and r2<=6:
            runs2 += r2
            print(f"Current score:{runs2}")
        else:
            print("Enter correct choice")
        if(x==5 or x==2):
            balls2-=1
            print(f'balls remaining {balls2}')
    if runs2>runs1:
        print(f"AI Score: {runs2}\nYour Score: {runs1}\nYou Lost\n")

#-----------------------------------------------------------------------------------------------
balls3=balls1
if play==2:
    runs2 = 0
    while ball==1 or balls1>0:
        r1 = bs.main("bowl score: ")
        print(f"bowl score:{r1}")
        r2 = r.randint(1, 6)
        print(f"AI input: {r2}")
        if r1 == r2:
            print(f"OUT!!! \nAI Score: {runs2}")
            break
        elif r1>=1 and r1<=6:
            runs2 += r2
            print(f'Current score :{runs2}')
        else:
            print("Enter correct choice")
        if x==5 or x==2:
            balls1-=1
            print(f'balls remaining{balls1}')
    print("Bat and beat AI\n")
    runs1 = 0
    while runs2>=runs1 and (balls3>0 or ball==1):
        if(runs2-runs1>0):
            print(f"Required runs:{runs2-runs1}")
            
        r1 = bs.main("bat score: ")
        print(f"bat score :{r1}")
        r2 = r.randint(1, 6)
        print(f"AI input: {r2}")
        if r1 == r2:
            print(f"OUT!!! \nYour Score: {runs1} \nAI Score: {runs2}\nYou Lost!\n")
            break
        elif r1<=6 and r1>=1:
            runs1 += r1
            print(f"your score:{runs1}")
        else:
            print("Enter correct choice")
        if x==5 or x==2:
            balls3-=1
            print(f"Balls remaining{balls3}")
    if runs1>runs2:
        print(f"Your Score: {runs1}\nAI Score: {runs2}\nYou Won!!!\n")
#-----------------------------------------------------------------------------------------------