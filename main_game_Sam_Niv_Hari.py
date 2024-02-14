'''************************************************
*                                                 *
*                N-Tile Puzzle by                 *
*                                                 *
*      Samuela Abigail Mathew, 71762108039        *
*              Nivetha S , 71762108030            *
*             Haripriya V , 71762108011           *
*                                                 *
*              B.Tech AI&DS, 2nd year             *
*        Coimbatore Institute of Technology       *
*                                                 *
************************************************'''

import BFS
import DFS
import BEST
import ASEARCH
import HC

#Global variables
l,GOAL=[],[]



'''*************************************
*  Finding all possible goal states of *
*  input puzzle                        *
*************************************'''

def find_goal_states(tiles):
    l.append('X')  #appending empty tile at beginning
    for i in tiles:
        if i=='G':
            l.insert(1,i) #insert G's at beginning after X

        elif i=='R':
            l.append(i) #append R's in end

    GOAL.append(''.join(l)) #appending initial goal state starting with X at position 1
    tiles_copy=l.copy()
    
    for i in range(len(tiles)-2): #to exclude case where X comes in last position as R should be in rightmost place
        temp=tiles_copy[i]
        tiles_copy[i]=tiles_copy[i+1]
        tiles_copy[i+1]=temp

        GOAL.append(''.join(tiles_copy)) #appending new goal state found by moving X

    return  
            




        
'''*************************************
*        Start of main program         *
*************************************'''

tiles=input('Enter tiles configuration: ')

#Checking if green,red and empty tiles are there
if 'G' not in tiles or 'R' not in tiles or 'X' not in tiles:
    print('Invalid configuration')

elif tiles.count('G')!=tiles.count('R') or tiles.count('X')!=1:
    print('Invalid configuration')    

else:
    find_goal_states(tiles)
    #print(GOAL)

    print('Which search do you want to perform?')
    print('1.Breadth First Search\n2.Depth First Search\n3.Best First Search\n4.A* Search\n5.Hill Clmibing Search')
    op=int(input('Enter choice: '))

    #input is goal state
    if tiles in GOAL and op in [1,2]:
        print('\n\nCost: 0\nTotal nodes expanded: 1')

    elif tiles in GOAL: #for heuristic search algorithms
        print('\n\nCost: %d\nTotal nodes expanded: 1'%(tiles.index('X')+1))

    else:    
        if op==1:
            BFS.move(tiles,GOAL)

        elif op==2:
            DFS.move(tiles,GOAL)

        elif op==3:
            BEST.move(tiles,GOAL)

        elif op==4:
            ASEARCH.move(tiles,GOAL)

        elif op==5:
            HC.move(tiles,GOAL)      

    

    
