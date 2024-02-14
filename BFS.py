'''**********************************
*                                   *
*       BFS Implementation by       *
*      Samuela Abigail Mathew       *
*          71762108039              *
*         AI&DS, 2nd year           *
*                                   *
**********************************'''


def move(tiles,goal):
    OPEN,CLOSED=[],[] #stores unvisited and visited nodes respectively; OPEN is queue and CLOSED is list
    total_nodes,cost=0,0 #gives total number of nodes expanded and total cost respectively to reach solution
    level_node_cnt=0  #number of unvisited children nodes generated at each level


    #initial configurations
    CLOSED.append(tiles) #moving original tiles configuration to CLOSED[]
    node=tiles
    prev_X_pos=node.index('X')+1 #position of X in parent node

    while True:
        #generate children for current node
        #if I remove this for loop then often output is wrong 
        l=list(node) #in 1st iteration, node is original configuration

        idx=l.index('X') #locating position of X in current node
        for i in range(len(tiles)):
            temp_l=l.copy() #for swapping X with tiles starting from position 1 to generate children (move 1 occurs before move 3, so always go from i=0)
            #print(temp_l[idx],temp_l[i],temp_l,i)
            temp=temp_l[idx]
            temp_l[idx]=temp_l[i] 
            temp_l[i]=temp

            node=''.join(temp_l)
            if node not in CLOSED and node not in OPEN:
                OPEN.append(node) #appending children nodes of current node
                level_node_cnt+=1
                #print('#',OPEN)

        #do breadth first search by traversing from left to right in current level
        next_level_node_cnt=0 #number of unvisited nodes at next level for children of current node 'child'
        for j in range(level_node_cnt): 
            child=OPEN[0] #I'll be always popping 1st element in OPEN, so next child will come to index 0
            print('MOVE %d   %s'%(child.index('X')+1,child))
            cost+=abs((child.index('X')+1)-prev_X_pos)

            prev_X_pos=child.index('X')+1 #updating

            if child in goal:
                total_nodes=len(OPEN)+len(CLOSED) #whatever nodes the program generates before reaching goal state, that only total nodes
                #print(OPEN,CLOSED)
                print('\nCost : %d\nTotal nodes expanded: %d'%(cost,total_nodes))
                return

            else:
                CLOSED.append(child)
                li=list(child) #for finding children of current node 'child' 
                idx=li.index('X') #locating position of X

                OPEN.pop(0) #since I'm using OPEN as queue data structure (FIFO)

                #generating children (successor nodes) of current node 'child'
                for i in range(len(child)):
                    temp_l=li.copy()
                    
                    temp=temp_l[idx]
                    temp_l[idx]=temp_l[i]
                    temp_l[i]=temp

                    node=''.join(temp_l)
                    if node not in CLOSED and node not in OPEN:
                        OPEN.append(node) #appending children nodes of next level
                        next_level_node_cnt+=1
                        #print('inner',OPEN)
            

        #No solution case
        if(len(OPEN)==0):
            print('No solution exists')
            return
        
        #updating for next level in bfs tree
        level_node_cnt=next_level_node_cnt
        node=OPEN[0]
        #print(OPEN,CLOSED)

        

        
