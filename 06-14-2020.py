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
        if self.inBounds(x+self.direction, y+1) and board[(x+self.direction, y+1)] != None and board[(x+self.direction, y+1)].color != color:
             answers.append((x+self.direction,y+1))
        if self.inBounds(x+self.direction, y-1) and board[(x+self.direction, y-1)] != None and board[(x+self.direction, y-1)].color != color: 
            answers.append((x+self.direction, y-1))
        if board[(x+self.direction, y)] == None and self.checkRules(board, x+self.direction, y, color):
             answers.append((x+self.direction, y))
        if (board[(x+(self.direction*2), y)] == None) and (x == 1 or x == 6):
            if self.checkRules(board, (x+(self.direction*2)), y, color):
                answers.append((x+self.direction*2, y))
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
            self.board[(1, i)] = Pawn(uniDict[BLACK][Pawn], BLACK, 1)
            self.board[(6, i)] = Pawn(uniDict[WHITE][Pawn], WHITE, -1)

        pieces = [Rook, Knight, Bishop, Queen, King, Bishop, Knight, Rook]

        for i in range(0, 8):
            self.board[(0, i)] = pieces[i](BLACK, uniDict[BLACK][pieces[i]])
            self.board[(7, i)] = pieces[i](WHITE, uniDict[WHITE][pieces[i]])

        #pieces.reverse()

    # Returns a dictionary of pieces that can see the king
    # pieces = dict{ (piece, pos) }
    def canSeeKing(self, kingPos, pieces):
        checkingPieces = []
        for piece, pos in pieces:
            if piece.valid(self.board, pos, kingPos, piece.color):
                checkingPieces.append((piece, pos))
        return checkingPieces

    def check(self):
        kingDict = dict()
        pieces = {BLACK: [], WHITE: []}
        for pos, piece in self.board.items():
            if piece == None:
                continue
            if type(piece) == King:
                kingDict[piece.color] = pos
                #king = piece
            #print(piece)
            pieces[piece.color].append((piece, pos))
        checkingPieces = self.canSeeKing(kingDict[WHITE], pieces[BLACK])
        if(checkingPieces != []):
            if self.isCheckmate(kingDict[WHITE], pieces):
                return True
            print("White player is in check")
            return True
        checkingPieces = self.canSeeKing(kingDict[BLACK], pieces[WHITE])
        if(checkingPieces != []):
            if self.isCheckmate(kingDict[BLACK], pieces):
                return True
            print("Black player is in check")
            return True
        return False

    def doMove(self, piece, piecePos, move, color):
        capturedPiece = None
        if piece.valid(self.board, piecePos, move, color):
            if(self.board[move] == None):
                self.board[move] = piece
                self.board[piecePos] = None
            elif(self.board[move].color != self.turn):
                capturedPiece = self.board[move]
                self.board[move] = piece
                self.board[piecePos] = None
        return capturedPiece

    def undoMove(self, piece, piecePos, originalPos, capturedPiece=None):
        if(capturedPiece == None):                
            self.board[originalPos] = piece
            self.board[piecePos] = None
        else:
            self.board[originalPos] = piece
            self.board[piecePos] = capturedPiece 
        return piece, piecePos

    def isCheckmate(self, kingPos, pieces):
        validMoves = []
        # # There are three ways of escaping check:
        if self.turn == BLACK: color = WHITE
        else: color = BLACK
        # # 1. Moving your king to a non-attacked square
        # # 2. Blocking the piece(s) delivering check
        # # 3. Capturing the checking piece.
        # New Idea: if for every move for player X, player Y can capture player X's king next turn, then player X is in checkmate
        for piece, pos in pieces[color]:
            for move in piece.availableMoves(self.board, pos[0], pos[1], color):
                print("Move: ",piece, "from: ", pos)
                print("To: ", move)
                capturedPiece = self.doMove(piece, pos, move, color)
                # if the move does not result in check, then the player is not in checkmate
                if self.canSeeKing(kingPos, pieces[self.turn]) == []:
                    piece, validMove = self.undoMove(piece, move, pos, capturedPiece)
                    validMoves.append((piece, validMove))
                    print("Valid moves to escape checkmate: ")
                    print(validMoves)
                    return False
                # Move still results in check -- undo, then continue searching
                self.undoMove(piece, move, pos, capturedPiece)
        # Each move has been evaluated for each piece. Every possible move results in check => Checkmate!
        print("Checkmate!", self.turn, "wins!")
        return True           

    def play(self):
        print("Welcome to Chess! Moves are entered w/ the following format: 'start end'. (i.e, 'b2 c2')")
        while True:
            print(self.turn + "'s' turn.")
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
                    if(self.check()):
                        self.printBoard()
                        return
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

    # Test case: Uses a 4-move checkmate game for testing.
    def testCheckmate(self):
        print("Welcome to Chess! Moves are entered w/ the following format: 'start end'. (i.e, 'b2 c2')")
        moves = [("g6", "f6"), ("b5", "d5"), ("g7", "e7"), ("a4", "e8")]
        i = 0
        target = None
        while True:
            print(self.turn + "'s' turn.")
            self.printBoard()
            self.message = ""
            if i < 4:
                a, b = moves[i][0], moves[i][1]
                a = ((ord(a[0])-97), int(a[1])-1)
                b = (ord(b[0])-97, int(b[1])-1)
                start, end = a, b
                i += 1
            else:
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
                    if(self.check()):
                        self.printBoard()
                        return
                    if(self.turn == BLACK):
                        self.turn = WHITE
                    else:
                        self.turn = BLACK
                else:
                    print("Invalid move.") #+ str(target.availableMoves(self.board, start[0], start[1], target.color))
                    print(target.availableMoves(self.board, start[0], start[1], target.color))
            else:print("There is no piece to move at that space!")


uniDict = {BLACK : {Pawn : "♙", Rook : "♖", Knight : "♘", Bishop : "♗", King : "♔", Queen : "♕" },
            WHITE : {Pawn : "♟", Rook : "♜", Knight : "♞", Bishop : "♝", King : "♚", Queen : "♛" }}
game = Chess()
game.testCheckmate()
#game.play()