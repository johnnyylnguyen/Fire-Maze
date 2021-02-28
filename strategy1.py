## THIS CODE IS FOR STRATEGY 1##
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
        # print('The explored cells using depth first search is:')
        # print(explored)
        # print('\n')
        #print('A path to the goal cannot be found using DFS.')
        return False
    else:
        # print('The explored cells using depth first search is:')
        # print(explored)
        # print('\n')
        # print('The path to the goal using breadth first search is:')
        # print(path)
        # print('\n')
        # lengthPath = len(path) - 1
        # print('The number of steps in this path is: ')
        # print(lengthPath)
        return True
    
    

    # DFS is better than BFS because you do not need to find an optimal path.

def strategy1(maze):

    # advance the fire
    maze = advance_fire_one_step(maze)
    
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
                # if (maze[row+1][col] != 4):
                if [row+1, col] not in explored:
                    explored.append([row+1, col])
                    fringe.append([row+1, col])
                    tempMaze[row+1][col] = 'S'
                    if [row+1, col] == [row1, col1]:
                        break
        if (col+1 < dim):
            if (maze[row][col+1] != 1):
                # if (maze[row][col+1] != 4):
                if [row, col+1] not in explored:
                    explored.append([row,col+1])
                    fringe.append([row,col+1])
                    tempMaze[row][col+1] = 'E'
                    if [row, col+1] == [row1, col1]:
                        break
        if (row-1 >= 0):
            if (maze[row-1][col] != 1):
                # if (maze[row-1][col] != 4):
                if [row-1, col] not in explored:
                    explored.append([row-1, col])
                    fringe.append([row-1, col])
                    tempMaze[row-1][col] = 'N'
                    if [row-1, col] == [row1, col1]:
                        break    
        if (col-1 >= 0):
            if (maze[row][col-1] != 1):
                # if (maze[row][col-1] != 4):
                if [row, col-1] not in explored:
                    explored.append([row,col-1])
                    fringe.append([row,col-1])
                    tempMaze[row][col-1] = 'W'
                    if [row, col-1] == [row1, col1]:
                        break
    
    # sets new goal and agent indices to backtrack and print shortest path
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

    return path


    

    """
    for i in range(len(maze)):
        print(maze[i])
    
    print('\n')
    
    if path != []:
        print('The path to the goal using breadth first search is:')
        print(path)
        print('\n')

        lengthPath = len(path) - 1
        print('The number of steps in this path is: ')
        print(lengthPath)
    else:
        print('A path to the goal cannot be found using BFS.')
    """


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


# if the fire cannot reach the agent
if DFStoFire(maze) == False:
    print('The fire cannot reach the agent!')
    print('\n')

# find the shortest path and returns it
path = strategy1(maze)

pathTaken = [[0,0]]

# if there is not path the maze cannot be completed thus failure
if path == []:
    print('There is no path to the goal.')
    print('The path taken was:')
    print(pathTaken)
    print('\n')
    print('Try Again. You failed to complete the fire maze using strategy 1.')
else:
    while path != []:

        #check if the goal is burned
        if maze[dim-1][dim-1] == 4:
            break

        nextStepIndex = path.pop(0)
        pathTaken.append(nextStepIndex)
        x = nextStepIndex[0]
        y = nextStepIndex[1]

        row = -1
        col = -1

        # find agent index
        for i in range(dim):
            for j in range(dim):
                if maze[i][j] == 2:
                    row = i
                    col = j

        # this is if the agent burned
        if row == -1 or col == -1:
            print('This is the final maze generated.')
            for i in range(len(maze)):
                print(maze[i])
            print('\n')

            print('Your agent burned in the fire.')
            print('The path taken was:')
            print(pathTaken)
            print('Try Again. You failed to complete the fire maze using strategy 1.')
            break
        
        # if fire does not block the path change the index of the agent 
        if maze[x][y] != 4:
            maze[row][col] = 0
            maze[x][y] = 2
            maze = advance_fire_one_step(maze)
            continue

        # if the fire blocks the shortest path
        else:
            print('This is the final maze generated.')
            for i in range(len(maze)):
                print(maze[i])
            print('\n')

            print('There is no path to the goal.')
            print('The path taken was:')
            print(pathTaken)
            print('Try Again. You failed to complete the fire maze using strategy 1.')
            break
    if maze[dim-1][dim-1] == 2:
        print('This is the final maze generated.')
        for i in range(len(maze)):
            print(maze[i])
        print('\n')

        print('The path taken was:')
        print(pathTaken)
        print('Congratulations! You have completed the fire maze using strategy 1.')
    