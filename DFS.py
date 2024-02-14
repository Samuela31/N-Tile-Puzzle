def move(tiles,goal):
    OPEN,CLOSED=[],[] #stores unvisited and visited nodes respectively; OPEN is stack and CLOSED is list
    total_nodes,cost=1,0 #gives total number of nodes expanded and total cost respectively to reach solution
    #total nodes expanded is initialized to 1 since it includes inputted node


    #initial configurations- storing original tiles configuration to CLOSED and OPEN
    OPEN.append(tiles)
    CLOSED.append(tiles) 
    node=tiles
    prev_X_pos=node.index('X')+1 #position of X in parent node

    #generate children for original/starting node
    l=list(node) 

    idx=l.index('X') #locating position of X in current node
    for i in range(len(tiles)):
        temp_l=l.copy() #for swapping X with tiles starting from position 1 to generate children (move 1 occurs before move 3, so always go from i=0)
        temp=temp_l[idx]
        temp_l[idx]=temp_l[i] 
        temp_l[i]=temp

        node=''.join(temp_l)
        if node not in CLOSED and node not in OPEN:
            OPEN.append(node) #appending children nodes of current node
            total_nodes+=1
            #print('#',OPEN)

    #do depth first search by traversing vertically from right to left
    while True:
        child=OPEN[-1] #since I'm using stack, I'll be checking from topmost element
        CLOSED.append(child) #I'll always append topmost element of stack 'OPEN' to mark node as visited 
        print('MOVE %d   %s'%(child.index('X')+1,child))
        cost+=abs((child.index('X')+1)-prev_X_pos)

        prev_X_pos=child.index('X')+1 #updating

        if child in goal:
            #print(OPEN,CLOSED)
            print('\nCost : %d\nTotal nodes expanded: %d'%(cost,total_nodes))
            return

        else:
            li=list(child) #for finding children of current node 'child' 
            idx=li.index('X') #locating position of X
            flag=0

            #generating children (successor nodes) of current node 'child'
            for i in range(len(child)):
                temp_l=li.copy()
                    
                temp=temp_l[idx]
                temp_l[idx]=temp_l[i]
                temp_l[i]=temp

                node=''.join(temp_l)
                if node not in CLOSED and node not in OPEN:
                    OPEN.append(node) #appending children nodes of next level
                    total_nodes+=1
                    flag=1
                    #print('inner',OPEN) 
            
            

        #No solution case
        if(len(OPEN)==0):
            print('No solution exists')
            return
        
        #current node is already visited and doesn't have children, so it must be popped from stack
        if(flag==0 and child in CLOSED):
            OPEN.pop()
        

        
