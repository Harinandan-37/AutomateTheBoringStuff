chessBoard = {'1b':'bking', '6c': 'bqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'}

def isValidPlace(board):
    placeCount = 0
    squares = {'0':'a', '1':'b', '2':'c', '3':'d', '4':'e', '5':'f', '6':'g', '7':'h'}
    
    for i,j in board.items():
        for x in range(1,9,1):
            for y in range(8):
                if i == str(x) + squares[str(y)]:
                    placeCount += 1
    if len(board) <= 32 and placeCount == len(board):
        return 1
    
    return -1

def isValidPiece(board):
    pieceCount = 0
    pieceList = ['pawn','knight','bishop','rook','queen','king']
    pieceCol = ['w','b']
    
    for place, piece in board.items():
        for x in range(2):
            for y in range(6):
                if piece == pieceCol[x] + pieceList[y]:
                    pieceCount += 1
    if len(board) <= 32 and pieceCount == len(board):
        return 1
    return -2


def isValidChessBoard(board):
    if isValidPiece(board) == 1 and isValidPlace(board) == 1:
        print("Valid Board")
        return 1
    
    if isValidPiece(board) == -2:
        print("Invalid Board: Invalid Piece(s)")
    if isValidPlace(board) == -1:
        print("Invalid Board: Invalid Place(s)")
    return 0

'''
There should be a bug if the chessBoard dict had the  same value for two different key.
Since this would mean the piece exists in two places at the same time.
But we don't have to worry about two pieces being in one place since the dict itself
would return an error for repeating a key.

So we should probably fix that but its not required according to the question.
'''

x = isValidChessBoard(chessBoard)
                   
        
        
        
