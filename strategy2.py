## THIS CODE IS FOR STRATEGY 2##
import random

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
    
    x = random.randint(1,dim*dim-1)
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

def strategy2(maze):

    maze = advance_fire_one_step(maze)
    dim = len(maze)
    
    row1 = dim - 1
    col1 = dim - 1

    row = -1
    col = -1
    ## this will find the indices of person
    for i in range(dim):
        for j in range(dim):
            if maze[i][j] == 2:
                row = i
                col = j
    # this takes into account if the agent is burned in fire
    if row == -1 or col == -1:
        return maze

    explored = [[row,col]] 
    fringe = [[row,col]]

    tempMaze = [([0]*dim) for i in range(dim)]

    for i in range(dim):
        for j in range(dim):
            tempMaze[i][j] = maze[i][j]

    while fringe != []:
        temp = fringe.pop(0)
        row = temp[0] 
        col = temp[1] 

        if (row+1 < dim): 
            if (maze[row+1][col] != 1):
                if (maze[row+1][col] != 4):
                    if [row+1, col] not in explored:
                        explored.append([row+1, col])
                        fringe.append([row+1, col])
                        tempMaze[row+1][col] = 'S'
                        if [row+1, col] == [row1, col1]:
                            break
        if (col+1 < dim):
            if (maze[row][col+1] != 1):
                if (maze[row][col+1] != 4):
                    if [row, col+1] not in explored:
                        explored.append([row,col+1])
                        fringe.append([row,col+1])
                        tempMaze[row][col+1] = 'E'
                        if [row, col+1] == [row1, col1]:
                            break
        if (row-1 >= 0):
            if (maze[row-1][col] != 1):
                if (maze[row-1][col] != 4):
                    if [row-1, col] not in explored:
                        explored.append([row-1, col])
                        fringe.append([row-1, col])
                        tempMaze[row-1][col] = 'N'
                        if [row-1, col] == [row1, col1]:
                            break    
        if (col-1 >= 0):
            if (maze[row][col-1] != 1):
                if (maze[row][col-1] != 4):
                    if [row, col-1] not in explored:
                        explored.append([row,col-1])
                        fringe.append([row,col-1])
                        tempMaze[row][col-1] = 'W'
                        if [row, col-1] == [row1, col1]:
                            break
    
    row = dim - 1
    col = dim - 1 
    for i in range(dim):
        for j in range(dim):
            if maze[i][j] == 2:
                row1 = i
                col1 = j
    path = []

    if tempMaze[dim-1][dim-1] != 3:
        path = [[dim-1, dim-1]]
        while (row != row1) or (col != col1):
            if (tempMaze[row][col] == 'S'):
                row = row - 1
                path.insert(0, [row, col])
                continue
            if (tempMaze[row][col] == 'E'):
                col = col - 1
                path.insert(0, [row, col])
                continue
            if (tempMaze[row][col] == 'N'):
                row = row + 1
                path.insert(0, [row, col])
                continue
            if (tempMaze[row][col] == 'W'):
                col = col + 1
                path.insert(0, [row, col])
                continue
    
    for i in range(dim):
        for j in range(dim):
            if maze[i][j] == 2:
                row = i
                col = j

    if path == []:
        print('A path to the goal cannot be found.')
        ## prints maze
        maze[dim-1][dim-1] = 5
        for i in range(len(maze)):
            print(maze[i])
        print('\n')
        return maze
    else:
        path.pop(0)
        newIndex = path.pop(0)
        x = newIndex[0]
        y = newIndex[1]

        maze[row][col] = 0
        maze[x][y] = 2
        print('The next step is: ') 
        print(newIndex)
        for i in range(len(maze)):
            print(maze[i])
        print('\n')

    
    return maze

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
# dim = 50
p = input("Enter your obstacle probability value (p) with range [0,1]: ")
# p = .3
## this already defines a global variable
q = input("Enter your obstacle probability value (q) with range [0,1]: ") 
print('\n')
# q = 0.70


maze = generateMaze(dim,p)
print('This is the original maze generated.')
for i in range(len(maze)):
    print(maze[i])
print('\n')

if DFStoFire(maze) == False:
    print('The fire cannot reach the agent!')
    print('\n')
while maze[dim-1][dim-1] != 2:
    if maze[dim-1][dim-1] == 5:
        break

    row = -1
    col = -1
    # find the agent
    for i in range(dim):
        for j in range(dim):
            if maze[i][j] == 2:
                row = i
                col = j

    # if the agent burned
    if row == -1 or col == -1:
        print('Your agent burned in the fire.')
        break

    maze = strategy2(maze)

if maze[dim-1][dim-1] == 2:
    print('Congratulations! You have completed the fire maze using strategy 2.')
else:
    print('Try Again. You failed to complete the fire maze using strategy 2.')