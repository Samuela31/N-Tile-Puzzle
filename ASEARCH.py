'''****************************************
*                                         *
*       A* Search Implementation by       *
*         Samuela Abigail Mathew          *
*               71762108039               *
*                                         *
*               Nivetha S                 *
*              71762108030                *
*            AI&DS, 2nd year              *
*                                         *
****************************************'''





def move(tiles,goal):
    OPEN,temp_sol=[],[] #stores unexplored paths and solution path found respectively; both are stacks
    total_nodes,f=1,0 #gives total number of nodes expanded and total cost respectively to reach goal state
    solution,cost=[],10000000 #to store solution path and solution cost


    #initial configurations
    OPEN.append(tiles)
    temp_sol.append(tiles)
    node=tiles
    prev_X_pos=H=node.index('X')+1 #I'm taking h in f=g+h as position of X in parent node
    f+=H #g is currently 0 (g is number of tiles X has moved from previous state to current state). H is heuristic cost of start state

    #generate children for original/starting node
    l=list(node) 

    idx=l.index('X') #locating position of X in current node
    for i in range(len(tiles)):
        temp_l=l.copy() #for swapping X with tiles starting from position 1 to generate children (move 1 occurs before move 3, so always go from i=0)
        temp=temp_l[idx]
        temp_l[idx]=temp_l[i] 
        temp_l[i]=temp

        node=''.join(temp_l)
        if node not in OPEN:
            OPEN.append(node) #appending children nodes of current node
            total_nodes+=1

    #do A* search by traversing vertically from right to left till OPEN becomes empty
    while(OPEN):
        child=OPEN[-1] #since I'm using stack, I'll be checking from topmost element
        if child not in temp_sol: #to prevent duplicate nodes
           temp_sol.append(child) #to keep track of solution path
           g=abs((child.index('X')+1)-prev_X_pos)
           h=child.index('X')+1
           f+=(g+h)
           prev_X_pos=child.index('X')+1 #updating
           #print(child,temp_sol,solution)


           if child in goal:
                if(f<cost):  #path with less cost is found
                    #print(temp_sol,f,cost)
                    cost=f
                    solution=temp_sol.copy()

                #print('#',OPEN,temp_sol,f,cost)
                while(temp_sol): #backtracking
                    if(OPEN[-1]==temp_sol[-1]):
                        OPEN.pop()
                        temp_sol.pop()

                    else:
                        break

                if(OPEN):
                    temp_sol.append(OPEN[-1]) #updating path
                    #updating f
                    for i in range(len(temp_sol)):
                        if i==0:
                           prev_X_pos=f=temp_sol[i].index('X')+1

                        else:
                           g=abs((child.index('X')+1)-prev_X_pos)
                           h=child.index('X')+1
                           f+=(g+h)
                           prev_X_pos=child.index('X')+1
   

           if(OPEN):
               li=list(OPEN[-1]) #for finding children of next node 
               idx=li.index('X') #locating position of X

               #generating children (successor nodes) of current node 'child'
               for i in range(len(OPEN[-1])):
                    temp_l=li.copy()
                                    
                    temp=temp_l[idx]
                    temp_l[idx]=temp_l[i]
                    temp_l[i]=temp

                    node=''.join(temp_l)
                    if node not in OPEN:
                        OPEN.append(node)
                        total_nodes+=1
            

    #No solution case
    if(len(OPEN)==0 and len(solution)==0):
        print('No solution exists')
        return

    #print solution path
    else:
        for i in range(1,len(solution)): #since 0th index has input node and I don't want to print it
            print('MOVE %d   %s'%(solution[i].index('X')+1,solution[i]))

        print('\nCost : %d\nTotal nodes expanded: %d'%(cost,total_nodes))    
        return

        
