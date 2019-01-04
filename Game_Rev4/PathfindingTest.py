from pathfinding.core.diagonal_movement import DiagonalMovement
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder
from board import Board
from random import randint

def generatePath(board, row, column, display=False):
    grid = Grid(matrix=board.grid)
    end = grid.node(column, row)
    start = grid.node(board.indexDict[board.SNAKE][1], board.indexDict[board.SNAKE][0]) 
    current = start
    finder = AStarFinder(diagonal_movement=DiagonalMovement.never)
    path, runs = finder.find_path(start, end, grid)

    if display == True:
        #print('operations:', runs, 'path length:', len(path))
        print(grid.grid_str(path=path, start=start, end=end))
    
    #first path instruction
    x = 0
    y = 0
    if len(path) > 1: (x, y) = path[1]
    elif len(path) == 1: (x, y) = path[0]
    else: print("Aiya! Pacman is stuck! Pathfinding won't work here so we need to make another method to avoid the ghosts (TODO)")
    
    if x < current.x:
        print("LEFT")
        return board.LEFT
    elif y < current.y:
        print("UP")
        return board.UP
    elif x > current.x:
        print("RIGHT")
        return board.RIGHT
    elif y > current.y:
        print("DOWN")
        return board.DOWN

board = Board()
def randCoords():
    randRow = randint(7, 15)
    randCol = randint(6, 14)
    while board.grid[randRow][randCol] != board.PELLET or (randRow == 7 and randCol == 8):
        randRow = randint(7, 15)
        randCol = randint(6, 14)
    #print(randRow, " ", randCol)
    return [randRow, randCol]
def moveGhostsRandomly():
    board.updatePos([board.GHOST], [randCoords()])
    board.updatePos([board.GHOST2], [randCoords()])
    board.updatePos([board.GHOST3], [randCoords()])
    board.updatePos([board.GHOST4], [randCoords()])

print("Pacman (s) moves to destination e uninterruptued")
board.move(board.SNAKE, generatePath(board, 7, 8, True))
for i in range(12):
    board.move(board.SNAKE, generatePath(board, 7, 8))
board.move(board.SNAKE, generatePath(board, 7, 8, True))

print("\nNow,let's make it a bit more complicated by randomly moving ghosts.")
print("But ghost won't land on (7,8) for the sake of this test")
board.reset()
while board.indexDict[board.SNAKE] != (7, 8):
    board.move(board.SNAKE, generatePath(board, 7, 8, True))
    moveGhostsRandomly()
print("Pacman has reached (7, 8)")

#old testing methods
"""board.move(board.SNAKE, generatePath(board, 7, 8, True))
board.updatePos([board.GHOST], [(10,6)])
board.move(board.SNAKE, generatePath(board, 7, 8, True))
board.updatePos([board.GHOST2], [(9,4)])
board.move(board.SNAKE, generatePath(board, 7, 8, True))"""


                
                            
        
