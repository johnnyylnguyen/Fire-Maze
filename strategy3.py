## THIS CODE IS FOR STRATEGY 3##
import random
import math

def generateMaze(dim, p):
    #generates dim*dim zero matrix
    maze = [([0]*dim) for i in range(dim)]

    # 0 is empty
    # 1 is obstacle
    # 2 is start/you
    # 3 is goal
    # 4 is fire
    maze[0][0] = 2
    maze[dim-1][dim-1] = 3



    for i in range(dim):
        for j in range(dim):
            if maze[i][j] == 0:
                if random.uniform(0,1) <= p:
                    maze[i][j] = 1
    
    x = random.randint(1,dim*dim-2)
    row = x//dim
    col = x%dim

    maze[row][col] = 4

    return maze

def DFStoFire(maze):
    row = 0
    col = 0
    dim = len(maze)

    for i in range(dim):
        for j in range(dim):
            if maze[i][j] == 4:
                row1 = i
                col1 = j


    # The idea is to have two stacks: explored cells and path cells
    explored = [[0,0]]
    path = [[0,0]]

    while (row != row1) or (col != col1):
        if path != []:
            lengthPathStack = len(path)
            temp = path[lengthPathStack - 1]
            row = temp[0]
            col = temp[1] 

        if (row+1 < dim):
            # attempt to move down
            if (maze[row+1][col] != 1):
                if [row+1, col] not in explored:
                    row += 1
                    explored.append([row,col])
                    path.append([row,col])
                    continue

        if (col+1 < dim):
            # attempt to move right
            if (maze[row][col+1] != 1):
                if [row, col+1] not in explored:
                    col += 1
                    explored.append([row,col])
                    path.append([row,col])
                    continue

        if (row-1 >= 0):
            # attempt to move up
            if (maze[row-1][col] != 1):
                if [row-1, col] not in explored:
                    row -= 1
                    explored.append([row,col])
                    path.append([row,col])
                    continue
                
        if (col-1 >= 0):
            # attempt to move left
            if (maze[row][col-1] != 1):
                if [row, col-1] not in explored:
                    col -= 1
                    explored.append([row,col])
                    path.append([row,col])
                    continue
        
        if path == []:
            break
        else:
            path.pop()

    if path == []:
        return False
    else:
        return True
    
    

    # DFS is better than BFS because you do not need to find an optimal path.

# lets create a helper function to find the distance from node to closest fire
def findDistNearestFire(row, col, maze):
    # this will return the euclidean distance of the nearest fire
    dim = len(maze)

    distanceList = []

    for i in range(dim): # loop through rows
        for j in range(dim): # loop through columns
            if maze[i][j] == 4: # for every fire
                # find euclidean distance to index
                rowDist = row - i
                colDist = col - j
                dist = math.sqrt(rowDist**2 + colDist**2)
                # add distance to list
                distanceList.append(dist)
        
    return min(distanceList)
    # this helper method considers the neighbor being a fire and will return 0

# lets create another helper function to find the distance to the goal
def findDistGoal(row, col, maze):
    # this will return the euclidean distance to the goal
    dim = len(maze)

    rowDist = row - (dim - 1)
    colDist = col - (dim - 1)

    dist = math.sqrt(rowDist**2 + colDist**2)

    return dist

def strategy3(maze):
    # initialize to start loop
    if DFStoFire(maze) == False:
        print('The fire cannot reach the agent!')
    print('\n')
    # checks if fire can reach agent... then will continue anyways

    row = 0
    col = 0
    dim = len(maze)
    rowGoal = dim - 1
    colGoal = dim - 1

    path = [[0,0]]
    explored = [[0,0]]

    while row != rowGoal or col != colGoal:
        maze = advance_fire_one_step(maze)

        row = -1
        col = -1
        
        # find agent index and set to row and col
        for i in range(dim):
            for j in range(dim):
                if maze[i][j] == 2:
                    row = i
                    col = j

        # if the agent burned -- 2 cannot be found
        if row == -1 or col == -1:
            print('Your agent burned in the fire.')
            print('\n')
            print('The path taken is:')
            print(path)
            print('\n')
            return(maze)

        # the neighbor heuristic list will have elements such as [row, col, h(n)]
        neighborHeuristicList = []
        # find the neighbor cells: check if out of bounds or obstacle
        # down neighbor
        if (row+1 < dim): #out of bounds
            if (maze[row+1][col] != 1): #obstacle
                if [row+1, col] not in explored:
                    fireDist = findDistNearestFire(row+1, col, maze) #find dist to closest fire
                    goalDist = findDistGoal(row+1, col, maze) # find dist to goal

                    if fireDist != 0: # check if this cell is a fire
                        # this is the heuristic (dim*dim - fireDist) + goalDist = h(n)
                        # you will want to take the SMALLEST VALUE BC YOU WANT largest distance from closest fire and shortest distance to goal
                        h = (dim*dim - fireDist) + goalDist
                        neighborHeuristicList.append([row+1, col, h])
        # right neighbor
        if (col+1 < dim):
            if (maze[row][col+1] != 1):
                if [row, col+1] not in explored:
                    fireDist = findDistNearestFire(row, col+1, maze)
                    goalDist = findDistGoal(row, col+1, maze)

                    if fireDist != 0:
                        h = (dim*dim - fireDist) + goalDist
                        neighborHeuristicList.append([row, col+1, h])
        # up neighbor
        if (row-1 >= 0):
            if (maze[row-1][col] != 1):
                if [row-1, col] not in explored:
                    fireDist = findDistNearestFire(row-1, col, maze)
                    goalDist = findDistGoal(row-1, col, maze)

                    if fireDist != 0:
                        h = (dim*dim - fireDist) + goalDist
                        neighborHeuristicList.append([row-1, col, h])
        # left neighbor
        if (col-1 >= 0):
            if (maze[row][col-1] != 1):
                if [row, col-1] not in explored:
                    fireDist = findDistNearestFire(row, col-1, maze)
                    goalDist = findDistGoal(row, col-1, maze)

                    if fireDist != 0:
                        h = (dim*dim - fireDist) + goalDist
                        neighborHeuristicList.append([row, col-1, h])

        #you cannot add any neighbor to the list so you backtrack
        if neighborHeuristicList == []:
            path.pop()
            if path == []:
                print('There is no path to the goal.')
                print('\n')
                return(maze)
            else:
                newPosition = path[len(path)-1] #takes the most previous position
                if maze[newPosition[0]][newPosition[1]] != 4: 
                    maze[row][col] = 0
                    maze[newPosition[0]][newPosition[1]] = 2 #sets new position
                    for i in range(len(maze)):
                        print(maze[i])
                    print('\n')
                else:
                    print('There is no path to the goal.')
                    print('\n')
                    return(maze)
        else:
            # now you have a list of neighbors and heurstics
            # find the minimum heuristic
            lengthHeuristicList = len(neighborHeuristicList)
            heuristicList = []
            for k in range(lengthHeuristicList): #run through neighbors
                element = neighborHeuristicList[k] #retrieve element from that list
                heuristicList.append(element[2]) #append h value to a new list
            bestHeuristic = min(heuristicList) # take the minimum

            for l in range(lengthHeuristicList):
                element = neighborHeuristicList[l]
                if element[2] == bestHeuristic:
                    maze[row][col] = 0 #erases current agent location
                    row = element[0]
                    col = element[1]
                    maze[row][col] = 2 #sets new agent location
                    path.append([row, col])
                    explored.append([row, col]) #append new location to path

                    for i in range(len(maze)):
                        print(maze[i])
                    print('\n')
                    break

    print('The path taken is:')
    print(path)
    print('\n')
    return(maze)
            
        
def advance_fire_one_step(maze):
    # FIRE CELLS are 4
    dim = len(maze)
    tempMaze = [([0]*dim) for i in range(dim)]

    for i in range(dim):
        for j in range(dim):
            tempMaze[i][j] = maze[i][j]
    
    for i in range(dim):
        for j in range(dim):
            k = 0
            if tempMaze[i][j] != 1:
                if (i+1 < dim):
                    if (maze[i+1][j] == 4):
                        k = k + 1
                if (j+1 < dim):
                    if (maze[i][j+1] == 4):
                        k = k + 1
                if (i-1 >= 0):
                    if (maze[i-1][j] == 4):
                        k = k + 1
                if (j-1 >= 0):
                    if (maze[i][j-1] == 4):
                        k = k + 1
                prob = 1 - ((1 - q) ** k)
                if random.uniform(0,1) <= prob:
                    tempMaze[i][j] = 4
    return tempMaze
    

dim = input("Enter your maze dimension: ")
p = input("Enter your obstacle probability value (p) with range [0,1]: ")
q = input("Enter your obstacle probability value (q) with range [0,1]: ") 
print('\n')

if dim > 1:
    if p >= 0 and p <= 1:
        maze = generateMaze(dim,p)
        print('This is the original maze generated.')
        for i in range(len(maze)):
            print(maze[i])
        print('\n')

        maze = strategy3(maze)

        if maze[dim-1][dim-1] == 2:
            print('This is the final maze generated.')
            for i in range(len(maze)):
                print(maze[i])
            print('\n')
            print('Congratulations! You have completed the fire maze using strategy 3.')
        else:
            print('This is the final maze generated.')
            for i in range(len(maze)):
                print(maze[i])
            print('\n')
            print('Try Again. You failed to complete the fire maze using strategy 3.')
    else:
        print('Obstacle density must within range [0,1] inclusive.')
else:
    print('Maze dimensions must be 2 or highter.')