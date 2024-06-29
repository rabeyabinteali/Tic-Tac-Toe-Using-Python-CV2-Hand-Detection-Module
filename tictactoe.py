board=[[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
flag={'r1':0,'r2':0,'r3':0,'c1':0,'c2':0,'c3':0,'d1':0,'d2':0}
playerFlag={'r1':0,'r2':0,'r3':0,'c1':0,'c2':0,'c3':0,'d1':0,'d2':0}
computerFlag={'r1':0,'r2':0,'r3':0,'c1':0,'c2':0,'c3':0,'d1':0,'d2':0}
computerPriority={'11': 3, '12': 2, '13': 3, '21': 2, '22': 100, '23': 2, '31': 3, '32':2, '33': 3}
gallery={'st': '  ','ct': '  ', 'moveCount': 0}
Score={'player': 0, 'computer': 0}
def printBoard(board):
    print(board[0][0]+"|"+board[0][1]+'|'+board[0][2])
    print('-----')
    print(board[1][0]+"|"+board[1][1]+'|'+board[1][2])
    print('-----')
    print(board[2][0]+"|"+board[2][1]+'|'+board[2][2])
    
def playerMove(playerM,posx,posy):
        board[posx%3 -1][posy%3 -1]=playerM
        cm=str(posx)+str(posy)
        if board[1][1]==playerM:
            if board[0][0]==playerM and board[0][1]==' ' and board[0][2]==' ':
                  computerPriority['13']=550
            if board[2][0]==playerM and board[2][1]==' ' and board[2][2]==' ':
                  computerPriority['33']=550
            if board[2][2]==playerM and board[2][1]==' ' and board[2][0]==' ':
                  computerPriority['31']=550
            if board[0][2]==playerM and board[0][1]==' ' and board[0][0]==' ':
                  computerPriority['11']=550
        if board[0][0]==board[2][1] and board[0][0]==playerM and board[1][0]==' ' and board[2][0]==' ':
                    computerPriority['21']=500
        if board[0][2]==board[2][1] and board[0][2]==playerM and board[2][2]==' ' and board[1][2]==' ':
                    computerPriority['23']=500
        if board[0][0]==board[1][2] and board[0][0]==playerM and board[0][2]==' ' and board[0][1]==' ':
                    computerPriority['12']=500
        if board[0][2]==board[1][0] and board[0][2]==playerM and board[0][0]==' ' and board[0][1]==' ':
                    computerPriority['12']=500
        if board[2][0]==board[0][1] and board[2][0]==playerM and board[1][0]==' ' and board[0][0]==' ':
                    computerPriority['21']=500
        if board[2][2]==board[0][1] and board[2][2]==playerM and board[1][2]==' ' and board[0][2]==' ':
                    computerPriority['23']=500
        if board[1][2]==board[2][0] and board[2][0]==playerM and board[2][1]==' ' and board[2][2]==' ':
                    computerPriority['32']=500
        if board[1][0]==board[2][2] and board[2][2]==playerM and board[2][1]==' ' and board[2][0]==' ':
                    computerPriority['32']=500
        if board[0][2]==board[2][0] and board[2][0]==playerM and board[1][2]==' ' and board[2][2]==' ':
                    computerPriority['23']=1500
        if board[0][0]==board[2][2] and board[2][2]==playerM and board[1][0]==' ' and board[2][0]==' ':
                    computerPriority['21']=1500
        if board[1][2]==board[2][1] and board[1][2]==playerM and board[2][2]==' ' and board[2][0]==' ':
                    computerPriority['33']=1500
        if board[1][0]==board[2][1] and board[1][0]==playerM and board[2][2]==' ' and board[2][0]==' ':
                    computerPriority['31']=1500
        if board[1][0]==board[0][1] and board[1][0]==playerM and board[0][0]==' ' and board[0][2]==' ':
                    computerPriority['11']=1500
        if board[1][2]==board[0][1] and board[1][2]==playerM and board[0][2]==' ' and board[0][0]==' ':
                    computerPriority['13']=1500
        if cm=='13' and board[2][0]==playerM:
            if board[1][2]==' ':
                computerPriority['23']=500
            if board[1][0]==' ':
                computerPriority['21']=500
        if(posx==1):
            computerPriority['11']-=1
            computerPriority['12']-=1
            computerPriority['13']-=1
            playerFlag['r1']+=1
            flag['r1']+=1
            if posy==1:
                playerFlag['d1']+=1
                flag['d1']+=1
                computerPriority['22']-=1
                computerPriority['33']-=1
            if posy==3:
                playerFlag['d2']+=1
                flag['d2']+=1
                computerPriority['22']-=1
                computerPriority['33']-=1
        elif(posx==2):
            computerPriority['21']-=1
            computerPriority['22']-=1
            computerPriority['23']-=1
            playerFlag['r2']+=1
            flag['r2']+=1
        elif posx==3:
            computerPriority['31']-=1
            computerPriority['32']-=1
            computerPriority['31']-=1
            playerFlag['r3']+=1
            flag['r3']+=1
            if posy==3:
                playerFlag['d1']+=1
                flag['d1']+=1
                computerPriority['11']-=1
            if posy==1:
                playerFlag['d2']+=1
                flag['d2']+=1
                computerPriority['13']-=1
        if(posy==1):
            computerPriority['11']-=1
            computerPriority['21']-=1
            computerPriority['31']-=1
            playerFlag['c1']+=1
            flag['c1']+=1
        elif(posy==2):
            computerPriority['12']-=1
            computerPriority['22']-=1
            computerPriority['32']-=1
            playerFlag['c2']+=1
            flag['c2']+=1
        elif posy==3:
            computerPriority['13']-=1
            computerPriority['23']-=1
            computerPriority['33']-=1
            playerFlag['c3']+=1
            flag['c3']+=1
        if posx==2 and posy==2:
            computerPriority['11']-=1
            computerPriority['33']-=1
            computerPriority['13']-=1
            computerPriority['31']-=1
            playerFlag['d1']+=1
            playerFlag['d2']+=1
            flag['d1']+=1
            flag['d2']+=1
        computerPriority[cm]=-999
        gallery['moveCount']=gallery['moveCount']+1
        for x in flag:
            if flag[x]==3:
                playerFlag[x]=-99
def ComputerMove(computerM):
    gallery['moveCount']=gallery['moveCount']+1
    if(max(playerFlag.values())==2 and flag[max(playerFlag,key=lambda x: playerFlag[x])]==2):
        gallery['st']=max(playerFlag,key=lambda x: playerFlag[x])
    if(max(computerFlag.values())==2 and flag[max(computerFlag,key=lambda x: computerFlag[x])]==2):
        gallery['ct']=max(computerFlag,key=lambda x: computerFlag[x])
    if gallery['st'][0]=='r':
        if  gallery['st'][1]=='1':
            if board[0][0]==' ':
                computerPriority['11']=555
            elif board[0][1]==' ':
                computerPriority['12']=555
            elif board[0][2]==' ':
                computerPriority['13']=555
        elif  gallery['st'][1]=='2':
            if board[1][0]==' ':
                computerPriority['21']=555
            elif board[1][1]==' ':
                computerPriority['22']=555
            elif board[1][2]==' ':
                computerPriority['23']=555
        elif  gallery['st'][1]=='3':
            if board[2][0]==' ':
                computerPriority['31']=555
            elif board[2][1]==' ':
                computerPriority['32']=555
            elif board[2][2]==' ':
                computerPriority['33']=555
    elif  gallery['st'][0]=='c':
        if  gallery['st'][1]=='1':
            if board[0][0]==' ':
                computerPriority['11']=555
            elif board[1][0]==' ':
                computerPriority['21']=555
            elif board[2][0]==' ':
                computerPriority['31']=555
        elif  gallery['st'][1]=='2':
            if board[0][1]==' ':
                computerPriority['12']=555
            elif board[1][1]==' ':
                computerPriority['22']=555
            elif board[2][1]==' ':
                computerPriority['32']=555
        elif  gallery['st'][1]=='3':
            if board[0][2]==' ':
                computerPriority['13']=555
            elif board[1][2]==' ':
                computerPriority['23']=555
            elif board[2][2]==' ':
                computerPriority['33']=555
    elif  gallery['st'][0]=='d':
        if  gallery['st'][1]=='1':
            if board[0][0]==' ':
                computerPriority['11']=555
            elif board[1][1]==' ':
                computerPriority['22']=555
            elif board[2][2]==' ':
                computerPriority['33']=555
        elif gallery['st'][1]=='2' :
            if board[0][2]==' ':
                computerPriority['13']=555
            elif board[1][1]==' ':
                computerPriority['22']=555
            elif board[2][0]==' ':
                computerPriority['31']=555
    if gallery['ct'][0]=='r':
        if  gallery['ct'][1]=='1':
            if board[0][0]==' ':
                computerPriority['11']=595
            elif board[0][1]==' ':
                computerPriority['12']=595
            elif board[0][2]==' ':
                computerPriority['13']=595
        elif  gallery['ct'][1]=='2':
            if board[1][0]==' ':
                computerPriority['21']=595
            elif board[1][1]==' ':
                computerPriority['22']=595
            elif board[1][2]==' ':
                computerPriority['23']=595
        elif  gallery['ct'][1]=='3':
            if board[2][0]==' ':
                computerPriority['31']=595
            elif board[2][1]==' ':
                computerPriority['32']=595
            elif board[2][2]==' ':
                computerPriority['33']=595
    elif  gallery['ct'][0]=='c':
        if  gallery['ct'][1]=='1':
            if board[0][0]==' ':
                computerPriority['11']=999
            elif board[1][0]==' ':
                computerPriority['21']=999
            elif board[2][0]==' ':
                computerPriority['31']=999
        elif  gallery['ct'][1]=='2':
            if board[0][1]==' ':
                computerPriority['12']=595
            elif board[1][1]==' ':
                computerPriority['22']=595
            elif board[2][1]==' ':
                computerPriority['32']=595
        elif  gallery['ct'][1]=='3':
            if board[0][2]==' ':
                computerPriority['13']=595
            elif board[1][2]==' ':
                computerPriority['23']=595
            elif board[2][2]==' ':
                computerPriority['33']=595
    elif  gallery['ct'][0]=='d':
        if  gallery['ct'][1]=='1':
            if board[0][0]==' ':
                computerPriority['11']=595
            elif board[1][1]==' ':
                computerPriority['22']=595
            elif board[2][2]==' ':
                computerPriority['33']=595
        elif gallery['ct'][1]=='2' :
            if board[0][2]==' ':
                computerPriority['13']=595
            elif board[1][1]==' ':
                computerPriority['22']=595
            elif board[2][0]==' ':
                computerPriority['31']=595
    cm=max(computerPriority,key=computerPriority.get)
    computerPriority[cm]=-99
    posx=int(cm[0])
    posy=int(cm[1])
    if(posx==1):
        computerFlag['r1']+=1
        flag['r1']+=1
        if posy==1:
            computerFlag['d1']+=1
            flag['d1']+=1
        if posy==3:
            computerFlag['d2']+=1
            flag['d2']+=1
    elif(posx==2):
        computerFlag['r2']+=1
        flag['r2']+=1
    else:
        computerFlag['r3']+=1
        flag['r3']+=1
        if posy==3:
            computerFlag['d1']+=1
            flag['d1']+=1
        if posy==1:
            computerFlag['d2']+=1
            flag['d2']+=1
    if(posy==1):
        computerFlag['c1']+=1
        flag['c1']+=1
    elif(posy==2):
        computerFlag['c2']+=1
        flag['c2']+=1
    else:
        computerFlag['c3']+=1
        flag['c3']+=1
    if posx==2 and posy==2:
        computerFlag['d1']+=1
        computerFlag['d2']+=1
        flag['d1']+=1
        flag['d2']+=1
    for x in flag:
        if flag[x]==3:
            computerFlag[x]=-99
    board[posx%3 -1][posy%3 -1]=computerM
    if (board[posx%3 -1][posy%3 -1]==board[posx%3 -1][(posy-1)%3 -1] and  board[posx%3 -1][posy%3 -1]==board[posx%3 -1][(posy+1)%3 -1])or(board[posx%3 -1][posy%3 -1]==board[(posx-1)%3 -1][posy%3 -1] and  board[posx%3 -1][posy%3 -1]==board[(posx+1)%3 -1][posy%3 -1]):
            Score['computer']=1
    if(board[posx%3 -1][posy%3 -1]==board[1][1]):
        if board[0][0]==board[1][1] and board[1][1]==board[2][2]:
            Score['computer']=1
        if board[0][2]==board[1][1] and board[2][0]==board[1][1]:
            Score['computer']=1
    if(gallery['ct']!='  '):
        computerFlag[gallery['ct']]=-99
        flag[gallery['ct']]=-99
        gallery['ct']='  '
    elif(gallery['st']!='  '):
        playerFlag[gallery['st']]=-99
        gallery['st']='  '
    return posx, posy

    
    
