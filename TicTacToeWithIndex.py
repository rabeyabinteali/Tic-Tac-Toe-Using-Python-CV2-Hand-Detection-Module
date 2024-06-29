import random
import cv2
import time
import numpy as np
import keyboard as kb
from cvzone.HandTrackingModule import HandDetector as hd
import tictactoe as tc 
turn=0  #0 for Human, 1 for Computer
        #Human goes first
def pointIsInFrame(x1,y1,x2,y2,point):
    if point[0]>=x1 and point[0]<=x2 and point[1]>=y1 and point[1]<=y2:
            return True
    else:
            return False
cap = cv2.VideoCapture(0)
detector=hd(detectionCon=0.8,maxHands=2)
sTime=20
# Check that a camera connection has been established
if not cap.isOpened():
    print("Error establishing connection")
pTime = 0 # prev time initially is 0
plength=58
fcTime=0
while cap.isOpened():
    # Read an image frame
    ret, fr = cap.read()
    frame=cv2.flip(fr,1)
    # Determining frame rate
    cTime = time.time()  #current time
    fps = 1/(cTime-pTime) # frame rate= 1/time diff
    pTime = cTime #current time becomes prev time
    cv2.putText(frame,f'FPS:{int(fps)}',(20,20),cv2.FONT_HERSHEY_PLAIN, 1.5, (255,0,255),3)
    
    #cv2.line(frame,(50,350),(580,350),(0,255,0),2)
    #Hand Detecting Code
    iPt2D=(0,0)
    hands,frame=detector.findHands(frame,flipType=False,draw=False)
    if (tc.Score['player']==1 and fcTime<=sTime):
            fcTime+=1
            cv2.putText(frame,"YOU WIN!",(150,250),1,3,(0,255,0),5)
            if(fcTime==sTime-1):
                cap.release()
                cv2.destroyAllWindows()
    elif (tc.Score['computer']==1 and fcTime<=sTime):
            fcTime+=1
            cv2.putText(frame,"COMPUTER WINS!",(100,250),1,3,(0,255,0),5)
            if(fcTime==sTime-1):
                cap.release()
                cv2.destroyAllWindows()
    elif (tc.Score['player']==0 and tc.Score['computer']==0 and tc.gallery['moveCount']>=9 and fcTime<=sTime):
        fcTime+=1
        cv2.putText(frame,"IT'S A DRAW!",(150,250),1,3,(0,255,0),5)
        if(fcTime==sTime-1):
            cap.release()
            cv2.destroyAllWindows()
    else:
        cv2.line(frame,(50,200),(580,200),(0,255,0),2)
        cv2.line(frame,(50,300),(580,300),(0,255,0),2)
        cv2.line(frame,(200,50),(200,450),(0,255,0),2)
        cv2.line(frame,(400,50),(400,450),(0,255,0),2)
        if (turn==1):
            fcTime+=1
            if(fcTime>=sTime):
                tc.ComputerMove('O')
                fcTime=0
                turn=0
        if(tc.board[0][0]!=' '):
            cv2.putText(frame,tc.board[0][0],(125,125),2,2,(255,255,255),10)
        if(tc.board[0][1]!=' '):
            cv2.putText(frame,tc.board[0][1],(300,125),2,2,(255,255,255),10)
        if(tc.board[0][2]!=' '):
            cv2.putText(frame,tc.board[0][2],(490,125),2,2,(255,255,255),10)
        if(tc.board[1][0]!=' '):
            cv2.putText(frame,tc.board[1][0],(125,250),2,2,(255,255,255),10)
        if(tc.board[1][1]!=' '):
            cv2.putText(frame,tc.board[1][1],(300,250),2,2,(255,255,255),10)
        if(tc.board[1][2]!=' '):
            cv2.putText(frame,tc.board[1][2],(490,250),2,2,(255,255,255),10)
        if(tc.board[2][0]!=' '):
            cv2.putText(frame,tc.board[2][0],(125,375),2,2,(255,255,255),10)
        if(tc.board[2][1]!=' '):
            cv2.putText(frame,tc.board[2][1],(300,375),2,2,(255,255,255),10)
        if(tc.board[2][2]!=' '):
            cv2.putText(frame,tc.board[2][2],(490,375),2,2,(255,255,255),10)
        if (tc.board[0][0]==tc.board[0][1] and  tc.board[0][1]==tc.board[0][2] and tc.board[0][0]!=' ' and fcTime<=sTime):
            fcTime+=1
            cv2.line(frame,(50,125),(580,125),(255,255,255),2)
            if(tc.board[0][0]=='X'):
                tc.Score['player']=1
            elif (tc.board[0][0]=='O'):
                tc.Score['computer']=1
            if(fcTime==sTime):
                fcTime=0
        if (tc.board[1][0]==tc.board[1][1] and  tc.board[1][1]==tc.board[1][2] and tc.board[1][0]!=' ' and fcTime<=sTime):
            fcTime+=1
            cv2.line(frame,(50,250),(580,250),(255,255,255),2)
            if(tc.board[1][0]=='X'):
                tc.Score['player']=1
            elif(tc.board[1][0]=='O'):
                tc.Score['computer']=1
            if(fcTime==sTime):
                fcTime=0
        if (tc.board[2][0]==tc.board[2][1] and  tc.board[2][1]==tc.board[2][2] and tc.board[2][0]!=' ' and fcTime<=sTime):
            fcTime+=1
            cv2.line(frame,(50,375),(580,375),(255,255,255),2)
            if(tc.board[2][0]=='X'):
                tc.Score['player']=1
            elif(tc.board[2][0]=='O'):
                tc.Score['computer']=1
            if(fcTime==sTime):
                fcTime=0
        if (tc.board[0][0]==tc.board[1][0] and  tc.board[1][0]==tc.board[2][0] and tc.board[0][0]!=' ' and fcTime<=sTime):
            fcTime+=1
            cv2.line(frame,(125,50),(125,450),(255,255,255),2)
            if(tc.board[0][0]=='X'):
                tc.Score['player']=1
            elif(tc.board[0][0]=='O'):
                tc.Score['computer']=1
            if(fcTime==sTime):
                fcTime=0
        if (tc.board[0][1]==tc.board[1][1] and  tc.board[1][1]==tc.board[2][1] and tc.board[0][1]!=' ' and fcTime<=sTime):
            fcTime+=1
            cv2.line(frame,(300,50),(300,450),(255,255,255),2)
            if(tc.board[0][1]=='X'):
                tc.Score['player']=1
            elif(tc.board[0][1]=='O'):
                tc.Score['computer']=1
            if(fcTime==sTime):
                fcTime=0
        if (tc.board[0][2]==tc.board[1][2] and  tc.board[1][2]==tc.board[2][2] and tc.board[0][2]!=' ' and fcTime<=sTime):
            fcTime+=1
            cv2.line(frame,(490,50),(490,450),(255,255,255),2)
            if(tc.board[0][2]=='X'):
                tc.Score['player']=1
            elif(tc.board[0][2]=='O'):
                tc.Score['computer']=1
            if(fcTime==sTime):
                fcTime=0
        if (tc.board[0][0]==tc.board[1][1] and  tc.board[1][1]==tc.board[2][2] and tc.board[0][0]!=' ' and fcTime<=sTime):
            fcTime+=1
            cv2.line(frame,(50,50),(580,450),(255,255,255),2)
            if(tc.board[0][0]=='X'):
                tc.Score['player']=1
            elif(tc.board[0][0]=='O'):
                tc.Score['computer']=1
            if(fcTime==sTime):
                fcTime=0
        if (tc.board[0][2]==tc.board[1][1] and  tc.board[1][1]==tc.board[2][0] and tc.board[0][2]!=' ' and fcTime<=sTime):
            fcTime+=1
            cv2.line(frame,(580,50),(50,450),(255,255,255),2)
            if(tc.board[0][2]=='X'):
                tc.Score['player']=1
            elif(tc.board[0][2]=='O'):
                tc.Score['computer']=1
            if(fcTime==sTime):
                fcTime=0
        if hands:
            #print(board)
            hand1=hands[0]
            lmList1= hand1["lmList"]
            indexPoint=lmList1[8]
            fUp=detector.fingersUp(hand1)
            iPt2D=(indexPoint[0],indexPoint[1])
            if fUp[1]==1:
                if pointIsInFrame(50,50,200,200,iPt2D):
                    #1 1
                    cv2.circle(frame,iPt2D,2,(0,255,0),8)
                    fcTime+=1                
                    if(fcTime>=sTime and tc.board[0][0]==' ' and turn==0):
                        tc.playerMove('X',1,1)
                        fcTime=0
                        turn=1
                if pointIsInFrame(200,50,400,200,iPt2D):
                    #1 2
                    cv2.circle(frame,iPt2D,2,(0,255,0),8)
                    fcTime+=1
                    if(fcTime>=sTime and tc.board[0][1]==' ' and turn==0):
                        tc.playerMove('X',1,2)
                        fcTime=0
                        turn=1
                if pointIsInFrame(400,50,580,200,iPt2D):
                    #1 3
                    cv2.circle(frame,iPt2D,2,(0,255,0),8)
                    fcTime+=1
                    if(fcTime>=sTime and tc.board[0][2]==' ' and turn==0):
                        tc.playerMove('X',1,3)
                        fcTime=0
                        turn=1
                if pointIsInFrame(50,200,200,300,iPt2D):
                    #2 1
                    cv2.circle(frame,iPt2D,2,(0,255,0),8)
                    fcTime+=1
                    if(fcTime>=sTime and tc.board[1][0]==' ' and turn==0):
                        tc.playerMove('X',2,1)
                        fcTime=0
                        turn=1
                if pointIsInFrame(200,200,400,300,iPt2D):
                    #2 2
                    cv2.circle(frame,iPt2D,2,(0,255,0),8)
                    fcTime+=1
                    if(fcTime>=sTime and tc.board[1][1]==' ' and turn==0):
                        tc.playerMove('X',2,2)
                        fcTime=0
                        turn=1
                if pointIsInFrame(400,200,580,300,iPt2D):
                    #2 3
                    cv2.circle(frame,iPt2D,2,(0,255,0),8)
                    fcTime+=1
                    if(fcTime>=sTime and tc.board[1][2]==' ' and turn==0):
                        tc.playerMove('X',2,3)
                        fcTime=0
                        turn=1
                if pointIsInFrame(50,300,200,450,iPt2D):
                    #3 1
                    cv2.circle(frame,iPt2D,2,(0,255,0),8)
                    fcTime+=1
                    if(fcTime>=sTime  and tc.board[2][0]==' ' and turn==0):
                        tc.playerMove('X',3,1)
                        fcTime=0
                        turn=1
                if pointIsInFrame(200,300,400,450,iPt2D):
                    #3 2
                    cv2.circle(frame,iPt2D,2,(0,255,0),8)
                    fcTime+=1
                    if(fcTime>=sTime and tc.board[2][1]==' ' and turn==0):
                        tc.playerMove('X',3,2)
                        fcTime=0
                        turn=1
                if pointIsInFrame(400,300,580,450,iPt2D):
                    #3 3
                    cv2.circle(frame,iPt2D,2,(0,255,0),8)
                    fcTime+=1
                    if(fcTime>=sTime and tc.board[2][2]==' ' and turn==0):
                        tc.playerMove('X',3,3)
                        fcTime=0
                        turn=1
    # Displaying image frame 
    if ret:
        cv2.imshow('Tic Tac Toe',frame)
 
    # If the Esc key is pressed, terminate the while loop
    if cv2.waitKey(25) == 27: #ASCII value of ESC key
        break