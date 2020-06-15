# You are presented with an 8 by 8 matrix representing the positions of pieces on a chess board. 
# The only pieces on the board are the black king and various white pieces. 
# Given this matrix, determine whether the king is in check.

# For details on how each piece moves, see here.

# For example, given the following matrix:

# . . . K . . . .
# . . . . . . . .
# . B . . . . . .
# . . . . . . P . 
# . . . . . . . R 
# . . N . . . . .
# . . . . . . . .
# . . . . . Q . .

# You should return True, since the bishop is attacking the king diagonally. (N is a knight)
# Author: John Furlong
# Date: June 14, 2020
# Implemenetation assisted by https://gist.github.com/rsheldiii/2993225

WHITE = "White"
BLACK = "Black"
# Create a parent class -- Piece -- to be inherited by individual pieces 
class Piece:
    def __init__(self, color, name):
        self.name = name
        self.position = None
        self.color = color

    # Check to see if a move from position start to end is valid
    def valid(self, board, start, end, color):
        if end in self.availableMoves(board, start[0], start[1], color):
            return True
        return False

    # Defines the movement allowed by a certain piece
    def availableMoves(self, board, x, y, color):
        print("ERROR: No moves for base class")

    # Returns a list of all possible moves 
    def returnMoves(self, board, x, y, intervals, color):
        answers = []
        for coord in intervals:
            x2, y2 = x+coord[0] , y+coord[1]
            while self.inBounds(x2, y2):
                if board[(x2, y2)] == None: answers.append((x2, y2))
                elif board[(x2, y2)].color != color:
                    answers.append((x2, y2))
                    break
                else:
                    break
                x2, y2 = x2 + coord[0], y2 + coord[1]
        return answers
 
    # Checks if the piece is in a valid pos. on the board
    def inBounds(self, x, y):
        if x >= 0 and  x < 8 and y >= 0 and y < 8:
            return True
        return False

    # Checks if a position is in conflict with any rules of the game
    def checkRules(self, board, x, y, color):
        if self.inBounds(x, y) and ((board[(x,y)] == None) or board[(x, y)].color != color):
            return True
        return False

# Define coordinate indexes to use for directional validation
cardinals = [(1, 0), (0, 1), (-1, 0), (0, -1)]
diagonals = [(1, 1), (-1, 1), (1, -1), (-1, -1)]
# Define function to return all possible moves for Knights and Kings
def knightList(x,y):
    return [(x+2,y+1),(x-2,y+1),(x+2,y-1),(x-2,y-1),
            (x+1,y+2),(x-1,y+2),(x+1,y-2),(x-1,y-2)]
def kingList(x,y):
    return [(x+1,y),(x+1,y+1),(x+1,y-1),(x,y+1),
            (x,y-1),(x-1,y),(x-1,y+1),(x-1,y-1)]

# Define individual piece classes which inhereit the Piece class
class Knight(Piece):
    def availableMoves(self, board, x, y, color = None):
        if color is None: color = self.color
        return[(i, j) for i, j in knightList(x, y) if self.checkRules(board, i, j, color)]

class Rook(Piece):
    def availableMoves(self, board, x, y, color = None):
        if color is None: color = self.color
        return self.returnMoves(board, x, y, cardinals, color)

class Bishop(Piece):
    def availableMoves(self, board, x, y, color = None):
        if color is None : color = self.color
        return self.returnMoves(board, x, y, diagonals, color)

class Queen(Piece):
    def availableMoves(self, board, x, y, color=None):
        if color is None : color = self.color
        return self.returnMoves(board, x, y, cardinals+diagonals, color)

class King(Piece):
    def availableMoves(self, board, x, y, color = None):
        if color is None : color = self.color
        return [(i, j) for i, j in kingList(x, y) if self.checkRules(board, x, y, color)]

class Pawn(Piece):
    def __init__(self, name, color, direction):
        self.name = name
        self.color = color
        self.direction = direction
    def availableMoves(self, board, x, y, color = None):
        if color is None: color = self.color
        answers = []
        if(x+self.direction,y+1) in board and self.checkRules(board, x+1, y+self.direction, color) : answers.append((x+1, y+self.direction))
        if(x+self.direction, y-1) in board and self.checkRules(board, x-1, y+self.direction ,color) : answers.append((x-1, y+self.direction))
        if board[(x+self.direction, y)] == None : answers.append((x+self.direction, y))
        if (board[(x+(self.direction*2), y)] == None) and (x == 1 or x == 6):
            answers.append((x+(self.direction*2), y))
        return answers

# Chess class for playing a game
class Chess:

    def __init__(self):
        self.board = dict()
        self.turn = WHITE
        self.message = "This will hold prompts"
        for i in range(0, 8):
            for j in range(0, 8):
                self.board[(i,j)] = None
        self.placePieces()
        
    def printBoard(self):
        # for (i, j) in self.board:
        print(self.turn + "'s' turn.")
        letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
        for i in range(0, 8):
            print(letters[i], '|  ', end='')
            for j in range(0, 8):
                if(self.board[(i,j)] == None):
                    if(j%7 == 0) and (j != 0):
                        print('[   ]')
                    else:
                        print('[   ], ', end='')
                elif(j%7 == 0) and (j != 0):
                    print('[', self.board[(i, j)].name, ']')
                else:
                    print('[', self.board[(i, j)].name, '], ', end='')
        print("----------------------------------------------------------")
        for i in range(0, 8):
            print('     ', i+1, end='')
        print()

    def placePieces(self):
        for i in range(0, 8):
            self.board[(1, i)] = Pawn(uniDict[WHITE][Pawn], WHITE, 1)
            self.board[(6, i)] = Pawn(uniDict[BLACK][Pawn], BLACK, -1)

        pieces = [Rook, Knight, Bishop, Queen, King, Bishop, Knight, Rook]

        for i in range(0, 8):
            self.board[(0, i)] = pieces[i](WHITE, uniDict[WHITE][pieces[i]])
            self.board[(7, 7-i)] = pieces[i](BLACK, uniDict[BLACK][pieces[i]])

        pieces.reverse()

    # pieces = dict{ (piece, pos) }
    def canSeeKing(self, kingPos, pieces):
        for piece, pos in pieces:
            if piece.valid(self.board, pos, kingPos, piece.color):
                return True

    def check(self):
        kingDict = dict()
        pieces = {BLACK: [], WHITE: []}
        for pos, piece in self.board.items():
            if piece == None:
                continue
            if type(piece) == King:
                kingDict[piece.color] = pos
            #print(piece)
            pieces[piece.color].append((piece, pos))
        if(self.canSeeKing(kingDict[WHITE], pieces[BLACK])):
            print("White player is in check")
            return True
        if(self.canSeeKing(kingDict[BLACK], pieces[WHITE])):
            print("Black player is in check")
            return True
        return False

    def play(self):
        print("Welcome to Chess! Moves are entered w/ the following format: 'start end'. (i.e, 'b2 c2')")
        while True:
            self.printBoard()
            self.message = ""
            start, end = self.parseInput()
            try:
                target = self.board[start]
            except:
                print("Could not find piece; index might be out of range")
                target = None
            if target:
                #print("Found: " + str(target))
                if(target.color != self.turn):
                    print("You are not allowed to move another player's piece!")
                    continue
                if target.valid(self.board, start, end, target.color):
                    print("Valid Move.")
                    self.board[end] = self.board[start]
                    self.board[start] = None
                    self.check()
                    if(self.turn == BLACK):
                        self.turn = WHITE
                    else:
                        self.turn = BLACK
                else:
                    print("Invalid move.") #+ str(target.availableMoves(self.board, start[0], start[1], target.color))
                    print(target.availableMoves(self.board, start[0], start[1], target.color))
            else:print("There is no piece to move at that space!")

    def parseInput(self):
        try:
            a,b = input().split()
            a = ((ord(a[0])-97), int(a[1])-1)
            b = (ord(b[0])-97, int(b[1])-1)
            #print(a,b)
            return (a,b)
        except:
            print("error decoding input. please try again")
            return((-1,-1),(-1,-1))

uniDict = {BLACK : {Pawn : "♙", Rook : "♖", Knight : "♘", Bishop : "♗", King : "♔", Queen : "♕" },
            WHITE : {Pawn : "♟", Rook : "♜", Knight : "♞", Bishop : "♝", King : "♚", Queen : "♛" }}
game = Chess()
game.play()