def move(tiles,goal):
    OPEN=[] #stores unvisited nodes; OPEN is priority queue 
    total_nodes=0 #gives total number of nodes expanded to reach solution

    #initial configurations
    node=tiles
    X_pos=node.index('X')+1 #I'll take position of X in current node as heuristic cost
    cost=X_pos #gives total heuristic cost to reach solution
    OPEN.append([tiles,X_pos]) 

    #generate children for original/starting node
    l=list(node) 

    idx=l.index('X') #locating position of X in current node
    mini=0 #for sorting cost-wise
    for i in range(len(tiles)):
        temp_l=l.copy() #for swapping X with tiles starting from position 1 to generate children (move 1 occurs before move 3, so always go from i=0)
        temp=temp_l[idx]
        temp_l[idx]=temp_l[i] 
        temp_l[i]=temp

        node=''.join(temp_l)
        if [node,node.index('X')+1] not in OPEN:
            OPEN.insert(0,[node,node.index('X')+1]) #appending children nodes of current node
            mini+=1
            #print('#',OPEN)

    #sorting cost-wise in ascending order to implement concept of priority queue
    #element with lowest cost comes before others in each level
    #print(OPEN)
    for i in range(mini-1):
        if OPEN[i][1]>OPEN[i+1][1]: 
            temp=OPEN[i]
            OPEN[i]=OPEN[i+1]
            OPEN[i+1]=temp

    #do best first search by traversing vertically from min cost
    while True:
        child=OPEN[0][0] #I'll be always checking from 1st element(since it has least cost) in OPEN
        print('MOVE %d   %s'%(child.index('X')+1,child))
        cost+=child.index('X')+1 #updating total cost


        if child in goal:
            total_nodes=len(OPEN) #whatever nodes the program generates before reaching goal state, that only total nodes
            #print(OPEN)
            print('\nCost : %d\nTotal nodes expanded: %d'%(cost,total_nodes))
            return

        else:
            #generate children for currently visited node
            l=list(child) 

            idx=l.index('X') #locating position of X in current node
            temp_sort,mini=[],0 #for sorting cost-wise
            for i in range(len(child)):
                temp_l=l.copy() #for swapping X with tiles starting from position 1 to generate children (move 1 occurs before move 3, so always go from i=0)
                temp=temp_l[idx]
                temp_l[idx]=temp_l[i] 
                temp_l[i]=temp

                node=''.join(temp_l)
                if [node,node.index('X')+1] not in OPEN:
                    temp_sort.append([node,node.index('X')+1]) #appending children nodes of current node
                    mini+=1
                    #print('#',OPEN)

            if(mini==0): #means current node 'child' has no children
                OPEN.pop(0) #so backtrack

            else:    
                #sorting cost-wise in ascending order to implement concept of priority queue
                #element with lowest cost comes before others in each level
                for i in range(mini-1):
                    if temp_sort[i][1]>temp_sort[i+1][1]: 
                        temp=temp_sort[i]
                        temp_sort[i]=temp_sort[i+1]
                        temp_sort[i+1]=temp

                for ele in temp_sort:
                    OPEN.insert(0,ele) #appending cost-wise sorted children of currently visited node to OPEN


        #No solution case
        if(len(OPEN)==0):
            print('No solution exists')
            return





