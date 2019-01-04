class Board():    
    def __init__(self): #we probably need to change these constants for pathfinding purposes
        self.LEFT = 1
        self.RIGHT = 2
        self.UP = 3
        self.DOWN = 4
        self.ROWS = 21
        self.COLS = 20
        """self.PELLET = 0
        self.BLOCK = 1
        self.SNAKE = 2
        self.GWALL = 3
        self.GHOST = 4
        self.GHOST2 = 5
        self.GHOST3 = 6
        self.GHOST4 = 7
        self.grid=
               [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ,1, 1, 1, 1, 1, 1, 1, 1, 1, 9],\ #0
                [1, 0, 0, 0, 0, 0, 0, 0, 0, 1 ,0, 0, 0, 0, 0, 0, 0, 0, 1, 9],\ #1
                [1, 0, 1, 1, 0, 1, 1, 1, 0, 1 ,0, 1, 1, 1, 0, 1, 1, 0, 1, 9],\ #2
                [1, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0, 0, 0, 0, 0, 0, 0, 0, 1, 9],\ #3
                [1, 0, 1, 1, 0, 1, 0, 1, 1, 1 ,1, 1, 0, 1, 0, 1, 1, 0, 1, 9],\ #4
                [1, 0, 0, 0, 0, 1, 0, 0, 0, 1 ,0, 0, 0, 1, 0, 0, 0, 0, 1, 9],\ #5
                [1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 9],\ #6
                [1, 1, 1, 1, 0, 1, 0, 0, 0, 7, 0, 0, 0, 1, 0, 1, 1, 1, 1, 9],\ #7
                [1, 1, 1, 1, 0, 1, 0, 1, 1, 3, 1, 1, 0, 1, 0, 1, 1, 1, 1, 9],\ #8
                [1, 0, 0, 0, 0, 0, 0, 1, 4, 5, 6, 1, 0, 0, 0, 0, 0, 0, 1, 9],\ #9
                [1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 9],\ #10
                [1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 9],\ #11
                [1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 9],\ #12
                [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 9],\ #13
                [1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 9],\ #14
                [1, 0, 0, 1, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 1, 0, 0, 1, 9],\ #15
                [1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 9],\ #16
                [1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 9],\ #17
                [1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 9],\ #18
                [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 9],\ #19
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 9]]  #20
                #0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19"""

        self.PELLET = 1
        self.BLOCK = 0
        self.SNAKE = 2
        self.GWALL = -3
        self.GHOST = -4
        self.GHOST2 = -5
        self.GHOST3 = -6
        self.GHOST4 = -7
        self.grid= [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0, 0, 0, 0, 0, 0, 0, 0, 0, -9],\
                [0, 1, 1, 1, 1, 1, 1, 1, 1, 0 ,1, 1, 1, 1, 1, 1, 1, 1, 0, -9],\
                [0, 1, 0, 0, 1, 0, 0, 0, 1, 0 ,1, 0, 0, 0, 1, 0, 0, 1, 0, -9],\
                [0, 1, 1, 1, 1, 1, 1, 1, 1, 1 ,1, 1, 1, 1, 1, 1, 1, 1, 0, -9],\
                [0, 1, 0, 0, 1, 0, 1, 0, 0, 0 ,0, 0, 1, 0, 1, 0, 0, 1, 0, -9],\
                [0, 1, 1, 1, 1, 0, 1, 1, 1, 0 ,1, 1, 1, 0, 1, 1, 1, 1, 0, -9],\
                [0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, -9],\
                [0, 0, 0, 0, 1, 0, 1, 1, 1, -7, 1, 1, 1, 0, 1, 0, 0, 0, 0, -9],\
                [0, 0, 0, 0, 1, 0, 1, 0, 0, -3, 0, 0, 1, 0, 1, 0, 0, 0, 0, -9],\
                [0, 1, 1, 1, 1, 1, 1, 0, -4, -5, -6, 0, 1, 1, 1, 1, 1, 1, 0, -9],\
                [0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, -9],\
                [0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, -9],\
                [0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, -9],\
                [0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, -9],\
                [0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, -9],\
                [0, 1, 1, 0, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 0, 1, 1, 0, -9],\
                [0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, -9],\
                [0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, -9],\
                [0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, -9],\
                [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, -9],\
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -9]]

        
        self.visited = [x[:] for x in self.grid]
        self.originalGrid = [x[:] for x in self.grid]
        #self.temp = []
        for i in range(self.ROWS):
            for j in range(self.COLS):
                if self.grid[i][j] == self.PELLET or self.grid[i][j] == self.GHOST4:
                    self.visited[i][j] = 0
                elif self.grid[i][j] == self.SNAKE:
                    self.visited[i][j] = 1
                else:
                    self.visited[i][j] = -1
        self.originalVisited = [x[:] for x in self.visited]
        """for i in range(21):
            for j in range(20):
                self.temp+=[0]
            self.visited.append(self.temp)
            self.temp = [] #added by Daniel, visited board now has correct dimensions"""
            
        self.indexDict={self.SNAKE: (15, 9), self.GHOST: (9, 8), self.GHOST2: (9, 9), self.GHOST3: (9, 10), self.GHOST4: (7, 9)} #do we need GHOST (4) as well? I added it (Daniel)
        self.score = 0

    #what does this do?
    def index_2d(self, v):
        for i, x in enumerate(self.grid):
            if v in x:
                return (i, x.index(v))
        return -1

    #update positions on the grid
    def updatePos(self,keyList=[],indexList=[]):#,SNAKEindex,GHOSTindex,GHOST2index,GHOST3index,GHOST4index):
        for i in range(len(indexList)):
            self.indexDict[keyList[i]]=indexList[i]

        #clear the old positions on the grid
        for i in range(self.ROWS):
            for j in range(self.COLS):
                if self.grid[i][j] == self.SNAKE or self.grid[i][j] == self.GHOST or self.grid[i][j] == self.GHOST2\
                   or self.grid[i][j] == self.GHOST3 or self.grid[i][j] == self.GHOST4:
                    if i == 8 and j == 9:
                        self.grid[i][j] == self.GWALL
                    elif i == 9 and (j == 8 or j == 9 or j == 10):
                        self.grid[i][j] = self.BLOCK
                    else: self.grid[i][j] = self.PELLET

        #set new positions
        self.grid[8][9] = self.GWALL #this is necessary for some reason
        for x in self.indexDict:
            self.grid[self.indexDict[x][0]][self.indexDict[x][1]] = x
        
        return 1

    """def updateVisited(self,path=[]):#,SNAKEindex,GHOSTindex,GHOST2index,GHOST3index,GHOST4index):
        for i in range(len(path)):
            self.visited[path[i][0]][path[i][1]]+=1
            if self.visited[path[i][0]][path[i][1]]==1:
                self.score+=1
        return self.visited"""

    #updates a single tile as visited rather than a path
    def updateVisited(self, pos):
        if self.isPellet(pos):
            self.score += 1
        self.visited[pos[0]][pos[1]] += 1

    #checks if a certain tile contains a normal pellet
    def isPellet(self, pos):
        return self.visited[pos[0]][pos[1]] == 0

    #is this necessary?
    def update(self,score,keyList=[],indexList=[],path=[]):
        a=updateVisited(self,path)
        b=updatePos(self,keyList,indexList)
        self.score = score
        return 1

    #resets the grids when a new game starts
    def reset(self):
        self.grid = [x[:] for x in self.originalGrid]
        self.visited = [x[:] for x in self.originalVisited]
        self.updatePos([2,-4,-5,-6,-7], [(15, 9),(9, 8),(9, 9),(9, 10),(7, 9)])
        self.score = 0

    #move a single item in one direction
    def move(self, item, direction):
        if direction == self.UP:
            self.updatePos([item], [(self.indexDict[item][0]-1, self.indexDict[item][1])])
        elif direction == self.DOWN:
            self.updatePos([item], [(self.indexDict[item][0]+1, self.indexDict[item][1])])
        elif direction == self.LEFT:
            self.updatePos([item], [(self.indexDict[item][0], self.indexDict[item][1]-1)])
        elif direction == self.RIGHT:
            self.updatePos([item], [(self.indexDict[item][0], self.indexDict[item][1]+1)])
            
        if item == self.SNAKE:
           self.updateVisited(self.indexDict[item])

    #debugging
    def test(self):
        print("Score: ", self.score)

        print("grid: ")
        for i in range(self.ROWS):
            for j in range(self.COLS):
                if self.grid[i][j] >= 0:
                    print("  ", self.grid[i][j], end="")
                else:
                    print(" ", self.grid[i][j], end="")
            print("")
        
        print("visited: ")
        for i in range(self.ROWS):
            for j in range(self.COLS):
                if self.visited[i][j] >= 0:
                    print("  ", self.visited[i][j], end="")
                else:
                    print(" ", self.visited[i][j], end="")
            print("")
        
#testing the functions
"""board=Board()

board.updatePos([2,-4,-5,-6,-7], [(15,8),(9,9),(8,9),(9,10),(7,10)])
board.updateVisited([15,8])
#board.test()
board.updatePos([2,-4,-5,-6,-7], [(15,7),(18,17),(9,3),(13,14),(3,6)])
board.updateVisited([15,7])
#board.test()
board.reset()
board.test()
board.move(board.SNAKE, board.LEFT)
board.test()"""

