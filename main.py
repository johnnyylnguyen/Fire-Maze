## THIS CODE IS FOR DFS, BFS, and A*##
import random
import math

def generateMaze(dim, p):
    #generates dim*dim zero matrix
    maze = [([0]*dim) for i in range(dim)]

    # 0 is empty
    # 1 is obstacle
    # 2 is start/you
    # 3 is goal
    maze[0][0] = 2
    maze[dim-1][dim-1] = 3

    for i in range(dim):
        for j in range(dim):
            if maze[i][j] == 0:
                if random.uniform(0,1) <= p:
                    maze[i][j] = 1
    
    return maze

def DFS(maze):
    row = 0
    col = 0
    dim = len(maze)
    row1 = dim - 1
    col1 = dim - 1

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
        print('The explored cells using depth first search is:')
        print(explored)
        print('\n')
        print('A path to the goal cannot be found using DFS.')
        # print(False)
    else:
        print('The explored cells using depth first search is:')
        print(explored)
        print('\n')
        print('The path to the goal using breadth first search is:')
        print(path)
        print('\n')
        lengthPath = len(path) - 1
        print('The number of steps in this path is: ')
        print(lengthPath)
        # print(True)
    
    print('\n')
    

    # DFS is better than BFS because you do not need to find an optimal path.

def BFS(maze):

    dim = len(maze)
    row1 = dim - 1
    col1 = dim - 1 

    explored = [[0,0]] 
    fringe = [[0,0]]


    while fringe != []:
        temp = fringe.pop(0)
        row = temp[0] 
        col = temp[1] 

        if (row+1 < dim): 
            if (maze[row+1][col] != 1):
                if [row+1, col] not in explored:
                    explored.append([row+1, col])
                    fringe.append([row+1, col])
                    maze[row+1][col] = 'S'
                    if [row+1, col] == [row1, col1]:
                        break
        if (col+1 < dim):
            if (maze[row][col+1] != 1):
                if [row, col+1] not in explored:
                    explored.append([row,col+1])
                    fringe.append([row,col+1])
                    maze[row][col+1] = 'E'
                    if [row, col+1] == [row1, col1]:
                        break
        if (row-1 >= 0):
            if (maze[row-1][col] != 1):
                if [row-1, col] not in explored:
                    explored.append([row-1, col])
                    fringe.append([row-1, col])
                    maze[row-1][col] = 'N'
                    if [row-1, col] == [row1, col1]:
                        break    
        if (col-1 >= 0):
            if (maze[row][col-1] != 1):
                if [row, col-1] not in explored:
                    explored.append([row,col-1])
                    fringe.append([row,col-1])
                    maze[row][col-1] = 'W'
                    if [row, col-1] == [row1, col1]:
                        break
    
    row = dim - 1
    col = dim - 1 
    row1 = 0
    col1 = 0 
    path = []

    if maze[dim-1][dim-1] != 3:
        path = [[dim-1, dim-1]]
        while (row != row1) or (col != col1):
            if (maze[row][col] == 'S'):
                row = row - 1
                path.insert(0, [row, col])
                continue
            if (maze[row][col] == 'E'):
                col = col - 1
                path.insert(0, [row, col])
                continue
            if (maze[row][col] == 'N'):
                row = row + 1
                path.insert(0, [row, col])
                continue
            if (maze[row][col] == 'W'):
                col = col + 1
                path.insert(0, [row, col])
                continue
    
    
    """
    for i in range(len(maze)):
        print(maze[i])
    
    print('\n')
    """

    if path != []:
        print('The explored cells using breadth first search is:')
        print(explored)
        print('\n')
        print('The shortest path to the goal using breadth first search is:')
        print(path)
        print('\n')

        lengthPath = len(path) - 1
        print('The number of steps in this path is: ')
        print(lengthPath)
    else:
        print('The explored cells using breadth first search is:')
        print(explored)
        print('\n')
        print('A shortest path to the goal cannot be found using BFS.')
    
    return path

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
                if (i-1 >= 0):
                    if (maze[i][j-1] == 4):
                        k = k + 1
                prob = 1 - ((1 - q) ** k)
                if random.uniform(0,1) <= prob:
                    tempMaze[i][j] = 4
    return tempMaze
 
def A(maze):

    dim = len(maze)
    # creates a zero matrix
    tempMaze = [([None]*dim) for i in range(dim)]

    rowGoal = dim - 1
    colGoal = dim -1 

    row = 0
    col = 0

    path = [[0,0]]
    explored = [[0,0]] # this is the number of nodes traveled to
    explored2 = [[0,0]] # this is the number of neighbors searched

    # creates a heuristic matrix
    for i in range(dim):
        for j in range(dim):
            if maze[i][j] != 1:
                rowDist = rowGoal - i
                colDist = colGoal - j
                dist = math.sqrt(rowDist**2 + colDist**2)
                tempMaze[i][j] = dist

    while (row != rowGoal) or (col != colGoal):
        neighbors = []

        # down
        if (row+1 < dim): #out of bounds
            if (maze[row+1][col] != 1): # obstacle
                if [row+1, col] not in explored:
                    if [row+1, col] not in explored2:
                        explored2.append([row+1, col])
                    neighbors.append(tempMaze[row+1][col])
        # right
        if (col+1 < dim): #out of bounds
            if (maze[row][col+1] != 1): # obstacle
                if [row, col+1] not in explored:
                    if [row, col+1] not in explored2:
                        explored2.append([row, col+1])
                    neighbors.append(tempMaze[row][col+1])
        # up
        if (row-1 >= 0): #out of bounds
            if (maze[row-1][col] != 1): # obstacle
                if [row-1, col] not in explored:
                    if [row-1, col] not in explored2:
                        explored2.append([row-1, col])
                    neighbors.append(tempMaze[row-1][col])
        # left
        if (col-1 >= 0): #out of bounds
            if (maze[row][col-1] != 1): # obstacle
                if [row, col-1] not in explored:
                    if [row, col-1] not in explored2:
                        explored2.append([row, col-1])
                    neighbors.append(tempMaze[row][col-1])
        
        if neighbors == []:
            if path == []:
                break
            else:
                path.pop()
                if path == []:
                    break
                else:
                    temp = path[len(path) - 1]
                    row = temp[0]
                    col = temp[1]
        else:
            # search for smallest value in neighbors
            smallestNeighbor = min(neighbors)
            # check down, right, left, up
            if (row+1 < dim):
                if (tempMaze[row+1][col] == smallestNeighbor):
                    if [row+1, col] not in explored:
                        row = row + 1
                        path.append([row, col])
                        explored.append([row, col])
                        continue
            if (col+1 < dim):
                if (tempMaze[row][col+1] == smallestNeighbor):
                    if [row, col+1] not in explored:
                        col = col + 1
                        path.append([row, col])
                        explored.append([row, col])
                        continue
            if (row-1 >= 0):
                if (tempMaze[row-1][col] == smallestNeighbor):
                    if [row-1, col] not in explored:
                        row = row - 1
                        path.append([row, col])
                        explored.append([row, col])
                        continue
            if (col-1 >= 0):
                if (tempMaze[row][col-1] == smallestNeighbor):
                    if [row, col-1] not in explored:
                        col = col - 1
                        path.append([row, col])
                        explored.append([row, col])
                        continue

    if path == []:

        print('A path to the goal cannot be found using A*.')
        print('\n')
    else:
        # print('The path to the goal using A* is:')
        # print(path)
        # print('\n')

        lengthPath = len(path) - 1
        print('The number of steps in this path is: ')
        print(lengthPath)

dim = input("Enter your maze dimension: ")
# dim = 1000
p = input("Enter your probability value with range [0,1]: ") 
# p = .3
print('\n')

if dim > 1:
    if p >= 0 and p <= 1:
        maze = generateMaze(dim,p)
        print('This is the original maze generated.')
        for i in range(len(maze)):
            print(maze[i])
        print('\n')

        #DFS(maze)
        #BFS(maze)
        #A(maze)

    else:
        print('Obstacle density must within range [0,1] inclusive.')
else:
    print('Maze dimensions must be 2 or highter.')







