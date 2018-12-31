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
	self.visited=[[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]*21
        self.indexDict={2: (9, 8), 5: (9, 9), 6: (9, 10), 7: (7, 9)}
        

    def index_2d(self, v):
        for i, x in enumerate(self.grid):
            if v in x:
                return (i, x.index(v))
        return -1

    def updatePos(self,keyList=[],indexList=[]):#,SNAKEindex,GHOSTindex,GHOST2index,GHOST3index,GHOST4index):
        for i in range(len(indexList)):
            self.indexDict[keyList[i]]=indexList[i]
	    self.
        return self.indexDict

    def updatePellets(self,path=[]):#,SNAKEindex,GHOSTindex,GHOST2index,GHOST3index,GHOST4index):
        for i in range(len(indexList)):
            self.indexDict[keyList[i]]=indexList[i]
	    self.
        return self.indexDict
        
board=Board()
print (board.update())
