class Board():    
    def __init__(self):
        self.PELLET = 0
        self.BLOCK = 1
        self.SNAKE = 2
        self.GWALL =3
        self.GHOST =4
        self.GHOST2 =5
        self.GHOST3 =6
        self.GHOST4 =7
        self.grid= [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ,1, 1, 1, 1, 1, 1, 1, 1, 1, 9],\
                [1, 0, 0, 0, 0, 0, 0, 0, 0, 1 ,0, 0, 0, 0, 0, 0, 0, 0, 1, 9],\
                [1, 0, 1, 1, 0, 1, 1, 1, 0, 1 ,0, 1, 1, 1, 0, 1, 1, 0, 1, 9],\
                [1, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0, 0, 0, 0, 0, 0, 0, 0, 1, 9],\
                [1, 0, 1, 1, 0, 1, 0, 1, 1, 1 ,1, 1, 0, 1, 0, 1, 1, 0, 1, 9],\
                [1, 0, 0, 0, 0, 1, 0, 0, 0, 1 ,0, 0, 0, 1, 0, 0, 0, 0, 1, 9],\
                [1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 9],\
                [1, 1, 1, 1, 0, 1, 0, 0, 0, 7, 0, 0, 0, 1, 0, 1, 1, 1, 1, 9],\
                [1, 1, 1, 1, 0, 1, 0, 1, 1, 3, 1, 1, 0, 1, 0, 1, 1, 1, 1, 9],\
                [1, 0, 0, 0, 0, 0, 0, 1, 4, 5, 6, 1, 0, 0, 0, 0, 0, 0, 1, 9],\
                [1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 9],\
                [1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 9],\
                [1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 9],\
                [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 9],\
                [1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 9],\
                [1, 0, 0, 1, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 1, 0, 0, 1, 9],\
                [1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 9],\
                [1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 9],\
                [1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 9],\
                [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 9],\
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 9]]
        self.visited=[]
        self.temp=[]
        for i in range(21):
            for j in range(20):
                self.temp+=[0]
            self.visited.append(self.temp)
            self.temp = [] #added by Daniel, visited board now has correct dimensions
        self.indexDict={2: (15, 9), 4: (9, 8), 5: (9, 9), 6: (9, 10), 7: (7, 9)} #do we need GHOST (4) as well? I added it (Daniel)
        self.score=0

    def index_2d(self, v):
        for i, x in enumerate(self.grid):
            if v in x:
                return (i, x.index(v))
        return -1

    def updatePos(self,keyList=[],indexList=[]):#,SNAKEindex,GHOSTindex,GHOST2index,GHOST3index,GHOST4index):
        for i in range(len(indexList)):
            self.indexDict[keyList[i]]=indexList[i]
        return 1

    def updateVisited(self,path=[]):#,SNAKEindex,GHOSTindex,GHOST2index,GHOST3index,GHOST4index):
        for i in range(len(path)):
            self.visited[path[i][0]][path[i][1]]+=1
            if self.visited[path[i][0]][path[i][1]]==1:
                self.score+=1
        return self.visited

    def isPellet(self,pos):
        return self.visited[pos[0]][pos[1]]>0

    def update(self,score,keyList=[],indexList=[],path=[]):
        a=updateVisited(self,path)
        b=updatePos(self,keyList,indexList)
        return 1
        
board=Board()
#print (board.updateVisited(path=[[2,10],[3,10],[4,10]]))
board.updateVisited(path=[[2,10],[3,10],[4,10]])
for i in range(21):
    for j in range(20):
        print(board.visited[i][j], " ", end="")
    print("")

