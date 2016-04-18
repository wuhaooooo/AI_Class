import random

##########################################################
boardState = [['.' for x in range(5)] for x in range(6)]
whoseTurn = 'W'
gameCounter = 1


def chess_reset():
    # reset the state of the game / your internal variables - note that this function is highly dependent on your implementation
    global boardState
    global whoseTurn
    global gameCounter
    boardState[0] = ['k', 'q', 'b', 'n', 'r']
    boardState[1] = ['p', 'p', 'p', 'p', 'p']
    boardState[2] = ['.', '.', '.', '.', '.']
    boardState[3] = ['.', '.', '.', '.', '.']
    boardState[4] = ['P', 'P', 'P', 'P', 'P']
    boardState[5] = ['R', 'N', 'B', 'Q', 'K']
    whoseTurn = 'W'
    gameCounter = 1


def chess_boardGet():
    # return the state of the game - one example is given below - note that the state has exactly 40 or 41 characters

    strOut = str(gameCounter) + ' ' + whoseTurn + '\n'
    for i in xrange(0, 6):
        for j in xrange(0, 5):
            strOut += boardState[i][j]
        strOut += '\n'
    return strOut


def chess_boardSet(strIn):
    # read the state of the game from the provided argument and set your internal variables accordingly - note that the state has exactly 40 or 41 characters

    global boardState
    global whoseTurn
    global gameCounter
    strIn = str(strIn)
    tempStr = str.split(strIn)
    gameCounter = int(tempStr[0])
    whoseTurn = tempStr[1]
    for i in xrange(0, 6):
        for j in xrange(0, 5):
            boardState[i][j] = tempStr[i + 2][j]


def chess_winner():
    # determine the winner of the current state of the game and return '?' or '=' or 'W' or 'B' - note that we are returning a character and not a string
    wKing = 0
    bKing = 0

    if gameCounter > 40:
        return '='

    for i in xrange(0, 6):
        for j in xrange(0, 5):
            if (boardState[i][j] == 'k'):
                bKing = 1
            if (boardState[i][j] == 'K'):
                wKing = 1

    if bKing == 1 and wKing == 1:
        return '?'
    elif (bKing == 1):
        return 'B'
    else:
        return 'W'


def chess_isValid(intX, intY):
    if intX < 0:
        return False

    elif intX > 4:
        return False

    if intY < 0:
        return False

    elif intY > 5:
        return False

    return True


def chess_isEnemy(strPiece):
    # with reference to the state of the game, return whether the provided argument is a piece from the side not on move - note that we could but should not use the other is() functions in here but probably
    if whoseTurn == 'W' and strPiece.islower():
        return True
    if whoseTurn == 'B' and strPiece.isupper():
        return True
    return False


def chess_isOwn(strPiece):
    # with reference to the state of the game, return whether the provided argument is a piece from the side on move - note that we could but should not use the other is() functions in here but probably
    if whoseTurn == 'W' and strPiece.isupper():
        return True
    if whoseTurn == 'B' and strPiece.islower():
        return True
    return False


def chess_isNothing(strPiece):
    # return whether the provided argument is not a piece / is an empty field - note that we could but should not use the other is() functions in here but probably
    if strPiece == '.':
        return True
    return False


def chess_eval():
    # with reference to the state of the game, return the the evaluation score of the side on move - note that positive means an advantage while negative means a disadvantage

    return 0


def chess_moves():
    # with reference to the state of the game and return the possible moves - one example is given below - note that a move has exactly 6 characters
    """ Determines all the possible moves of the current state
        The input/output is expected to be in a well defined format
        returns a string/array"""

    """For pawn
       1. determine which side
       2. find all pawns
            for loop
                if board == 'p' or 'P'
       3. get the index of each 'p'
       4. create a new position, newPostion, add 1 or deduct 1 to its row
       5. checkout chess_isValid(x, y) if false, continue
       6. checkout chess_isOwn(board[y][x]) if true continue
            if false create a string 'a2-a3'
            convert x,y to a2 by calling hao_myIndex2String(y, x)
            convert x+1,y to a3 by calling hao_myIndex2String(y, x)
            append that string
    -------------------------------------------
    whoseTurn = 'W'
    boardState[0] = ['k', 'q', 'b', 'n', 'r']
    boardState[1] = ['p', 'p', 'p', 'p', 'p']
    boardState[2] = ['.', '.', '.', '.', '.']
    boardState[3] = ['.', '.', '.', '.', '.']
    boardState[4] = ['P', 'P', 'P', 'P', 'P']
    boardState[5] = ['R', 'N', 'B', 'Q', 'K']
    """
    strOut = []
    # Pawns default is lower 'p'
    target = 'p'
    if whoseTurn == 'W':
        target = 'P'

    for i in xrange(0, 6):
        for j in xrange(0, 5):
            if boardState[i][j] == target:
                theMoves = hao_pawnMoves(target, i, j)
                for x in theMoves:
                    if chess_isValid(x[1], x[0]):
                        if not chess_isOwn(boardState[x[0]][x[1]]):
                            strAppend = hao_myIndex2String(i, j) + '-' + hao_myIndex2String(x[0], x[1]) + '\n'
                            strOut.append(strAppend)
    # Knight default is lower 'n'
    target = 'n'
    if whoseTurn == 'W':
        target = 'N'
    for i in xrange(0, 6):
        for j in xrange(0, 5):
            if boardState[i][j] == target:
                theMoves = hao_knightMoves(i, j)
                for x in theMoves:
                    if chess_isValid(x[1], x[0]):
                        if not chess_isOwn(boardState[x[0]][x[1]]):
                            strAppend = hao_myIndex2String(i, j) + '-' + hao_myIndex2String(x[0], x[1]) + '\n'
                            strOut.append(strAppend)

    print strOut
    return strOut


def hao_knightMoves(ii, jj):
    # generating all pawns move
    # whoseTurn = 'W'
    # boardState[0] = ['k', 'q', 'b', 'n', 'r']
    # boardState[1] = ['p', 'p', 'p', 'p', 'p']
    # boardState[2] = ['.', '.', '.', '.', '.']
    # boardState[3] = ['.', '.', '.', '.', '.']
    # boardState[4] = ['P', 'P', 'P', 'P', 'P']
    # boardState[5] = ['R', 'N', 'B', 'Q', 'K']
    res = []
    # top four
    res.append((ii - 1, jj - 2))
    res.append((ii - 2, jj - 1))
    res.append((ii - 2, jj + 1))
    res.append((ii - 1, jj + 2))
    # bottom four
    res.append((ii + 1, jj - 2))
    res.append((ii + 2, jj - 1))
    res.append((ii + 2, jj + 1))
    res.append((ii + 1, jj + 2))
    return res


def hao_pawnMoves(theTarget, ii, jj):
    # generating all pawns move
    res = []
    if theTarget == 'p':
        res.append((ii + 1, jj))
    else:
        res.append((ii - 1, jj))
    return res


def hao_myIndex2String(theRow, theCol):
    # convert chess index to my board index
    # example "40" --> "a2"
    rowConvert = {
        0: '6',
        1: '5',
        2: '4',
        3: '3',
        4: '2',
        5: '1',
    }
    row = rowConvert.get(theRow, "")

    colConvert = {
        0: 'a',
        1: 'b',
        2: 'c',
        3: 'd',
        4: 'e',
    }
    col = colConvert.get(theCol, "")
    return col + row


def chess_movesShuffled():
    # with reference to the state of the game, determine the possible moves and shuffle them before returning them- note that you can call the chess_moves() function in here

    return []


def chess_movesEvaluated():
    # with reference to the state of the game, determine the possible moves and sort them in order of an increasing evaluation score before returning them - note that you can call the chess_movesShuffled() function in here
    return []


def chess_move(strIn):
    # perform the supplied move (for example 'a5-a4\n') and update the state of the game / your internal variables accordingly - note that it advised to do a sanity check of the supplied move
    """ Performs the provided move
        The provided move is in a well defined format
        the board/state and therefore the internal variables need to be updated accordingly"""
    pass


def chess_moveRandom():
    # perform a random move and return it - one example output is given below - note that you can call the chess_movesShuffled() function as well as the chess_move() function in here

    return 'a2-a3\n'


def chess_moveGreedy():
    # perform a greedy move and return it - one example output is given below - note that you can call the chess_movesEvaluated() function as well as the chess_move() function in here

    return 'a2-a3\n'


def chess_moveNegamax(intDepth, intDuration):
    # perform a negamax move and return it - one example output is given below - note that you can call the the other functions in here

    return 'a2-a3\n'


def chess_moveAlphabeta(intDepth, intDuration):
    # perform a alphabeta move and return it - one example output is given below - note that you can call the the other functions in here

    return 'a2-a3\n'


def chess_undo():
    # undo the last move and update the state of the game / your internal variables accordingly - note that you need to maintain an internal variable that keeps track of the previous history for this

    pass
