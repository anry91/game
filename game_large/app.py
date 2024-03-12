from map import *
from ui import * 

while True:
    clear()
    printMap(gameMap)
    key = controls()


    if key == 'x':
        break
    gameMap[rr][rc]= 0
    if key =='d' and gameMap[rr][rc+1] != 1 and 9>= rc+1 :        
       rc +=1             
     
    if key =='a' and gameMap[rr][rc-1] != 1 and 0<= rc-1 :        
        rc -=1     

    gameMap[rr][rc]= 2 # put the robot
    
    gameMap[rr][rc]= 0
    if key =='s' and gameMap[rr+1][rc] != 1 and 9>= rr + 1:
        rr +=1
        
    if key =='w' and gameMap[rr-1][rc] != 1 and 0<= rr - 1:
        rr -=1
    gameMap[rr][rc]= 0
    












