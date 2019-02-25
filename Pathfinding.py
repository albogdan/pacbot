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
    else: return 1 #we are trapped!
    
    if x < current.x:
        return board.LEFT
    elif y < current.y:
        return board.UP
    elif x > current.x:
        return board.RIGHT
    elif y > current.y:
        return board.DOWN



                
                            
        
