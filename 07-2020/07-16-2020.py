# Conway's Game of Life takes place on an infinite two-dimensional board of square cells. Each cell is either dead or alive, 
# and at each tick, the following rules apply:

# Any live cell with less than two live neighbours dies.
# Any live cell with two or three live neighbours remains living.
# Any live cell with more than three live neighbours dies.
# Any dead cell with exactly three live neighbours becomes a live cell.
# A cell neighbours another cell if it is horizontally, vertically, or diagonally adjacent.

# Implement Conway's Game of Life. It should be able to be initialized with a starting list of live cell coordinates
#  and the number of steps it should run for. Once initialized, it should print out the board state at each step. 
# Since it's an infinite board, print out only the relevant coordinates
#       i.e. from the top-leftmost live cell to bottom-rightmost live cell.

# You can represent a live cell with an asterisk (*) and a dead cell with a dot (.).

class Cell:
    def __init__(self, row, col):
        self.living = True
        self.row = row
        self.col = col
        self.adj = []

class GameOfLife:

    def __init__(self, cell_locations):
        self.board = dict()
        self.topLeft = (100, 100)
        self.bottomRight = (0, 0)
        # Only add cell locations -- infinite, so no need to add empty spaces
        for row, col in cell_locations:
            # Keep track of topLeft & bottomRight cells for printing
            if(row+col > self.bottomRight[0] + self.bottomRight[1]):
                self.bottomRight = (row, col)
            if(row+col < self.topLeft[0] + self.topLeft[1]):
                self.topLeft = (row, col)

            self.board[(row, col)] = Cell(row, col)
    
    # Check cells for adjacent cells
    def checkForNeighbors(self, cell):
        delta_r = [-1, -1, 0, 1, 1, 1, 0, -1]
        delta_c = [0, 1, 1, 1, 0, -1, -1, -1]
        adj = []
        for i in range(8):
            row = cell.row + delta_r[i]
            col = cell.row + delta_c[i]
            if(row < 0 or col < 0): continue
            if(self.board.get((row, col)) is None): continue
            if(self.board[(row, col)]):
                adj.append((row, col))
        cell.adj = adj
        return

    # Infinite baord -- print cells from the top-leftmost live cell to bottom-rightmost live cell
    def printBoard(self):
        for r in range(self.topLeft[0], self.bottomRight[0]):
            print(r , '|\t', end='')
            for c in range(self.topLeft[1], self.bottomRight[1]):
                if self.board.get((r, c)) is None:
                    print('[   ]', end='')
                elif(self.board[(r, c)].living == True):
                    print('[ * ]', end = '')
                elif(self.board[(r, c)].living == False):
                    print('[ . ]', end='')
            print()
                    
    # Called at each iteration of the "game" -- checks which cells should live/die
    def turn(self):
        pass

    # Driver function to simulate the game for nTurns
    def play(self, nTurns):
        for i in range(nTurns):
            # Print Board for each turn
            print("Iteration: ", i)
            self.printBoard()
            # For each turn (iteration) evaluate each cell
            for row, col in self.board.keys():
                cell = self.board[(row, col)]
                self.checkForNeighbors(cell)
                # Live cells with less than 3 neighbors dies
                if (cell.adj == [] or len(cell.adj) == 1) and cell.living:
                    cell.living = False
                # Live cell with more than 3 neighbors dies
                elif(len(cell.adj) > 3) and cell.living:
                    cell.living = False
                # Dead cell w/ excactly 3 neighbors comes back to life
                elif(len(cell.adj) == 3) and not cell.living:
                    cell.living = True
                # Live cells with 2 or 3 neighbors live -- No code needed
            

# Driver Code
cell_locs = [ (0, 0), (1, 1), (1, 2), (2, 0), (2, 2), (2, 3), (3, 2), (3, 3), (4, 1), (4, 3), (4, 4)]
game = GameOfLife(cell_locs)
game.play(5)