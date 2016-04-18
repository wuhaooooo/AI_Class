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
    wscore = 0
    bscore = 0
    score = {
        'p': 1,
        'P': 1,
        'r': 5,
        'R': 5,
        'n': 4,
        'N': 4,
        'b': 5,
        'B': 5,
        'q': 8,
        'Q': 8,
        'k': 10,
        'K': 10,
    }
    # row = score.get(theRow, "")
    for i in xrange(0, 6):
        for j in xrange(0, 5):
            if boardState[i][j].isupper():
                wscore += score.get(boardState[i][j], 0)
            elif boardState[i][j].islower():
                bscore += score.get(boardState[i][j], 0)
    if whoseTurn == 'W':
        return wscore - bscore
    else:
        return bscore - wscore
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
    """
    strOut = []
    for i in xrange(0, 6):
        for j in xrange(0, 5):
            if whoseTurn == 'W':
                if boardState[i][j] == 'P':
                    hao_pawnMovesPrint('P', i, j, strOut)
                elif boardState[i][j] == 'R':
                    hao_rookMovesPrint(i, j, strOut)
                elif boardState[i][j] == 'N':
                    hao_knightMovesPrint(i, j, strOut)
                elif boardState[i][j] == 'B':
                    hao_bishopMovesPrint(i, j, strOut)
                elif boardState[i][j] == 'Q':
                    hao_queenMovesPrint(i, j, strOut)
                elif boardState[i][j] == 'K':
                    hao_kingMovesPrint(i, j, strOut)

            elif whoseTurn == 'B':
                if boardState[i][j] == 'p':
                    hao_pawnMovesPrint('p', i, j, strOut)
                elif boardState[i][j] == 'r':
                    hao_rookMovesPrint(i, j, strOut)
                elif boardState[i][j] == 'n':
                    hao_knightMovesPrint(i, j, strOut)
                elif boardState[i][j] == 'b':
                    hao_bishopMovesPrint(i, j, strOut)
                elif boardState[i][j] == 'q':
                    hao_queenMovesPrint(i, j, strOut)
                elif boardState[i][j] == 'k':
                    hao_kingMovesPrint(i, j, strOut)

    return strOut

def hao_queenMovesPrint(i, j, strOut):
    theMoves = hao_queenMoves(i, j)
    for x in theMoves:
        # if chess_isValid(x[1], x[0]):
        #     if not chess_isOwn(boardState[x[0]][x[1]]):
        strAppend = hao_myIndex2String(i, j) + '-' + hao_myIndex2String(x[0], x[1]) + '\n'
        strOut.append(strAppend)

def hao_queenMoves(ii, jj):
    res = []
    u = True
    d = True
    l = True
    r = True
    ul = True
    ur = True
    dl = True
    dr = True
    for x in range(1, 6):
        # for up
        if u and chess_isValid(jj, ii - x) and not chess_isOwn(boardState[ii - x][jj]):
            res.append((ii - x, jj))
            if not chess_isNothing(boardState[ii - x][jj]):
                u = False
        else:
            u = False
        # for down
        if d and chess_isValid(jj, ii + x) and not chess_isOwn(boardState[ii + x][jj]):
            res.append((ii + x, jj))
            if not chess_isNothing(boardState[ii + x][jj]):
                d = False
        else:
            d = False
        # for left
        if l and chess_isValid(jj - x, ii) and not chess_isOwn(boardState[ii][jj - x]):
            res.append((ii, jj - x))
            if not chess_isNothing(boardState[ii][jj-x]):
                l = False
        else:
            l = False
        # for right
        if r and chess_isValid(jj + x, ii) and not chess_isOwn(boardState[ii][jj + x]):
            res.append((ii, jj + x))
            if not chess_isNothing(boardState[ii][jj+x]):
                r = False
        else:
            r = False
        # for up left
        if ul and chess_isValid(jj - x, ii - x) and not chess_isOwn(boardState[ii - x][jj - x]):
            res.append((ii - x, jj - x))
            if not chess_isNothing(boardState[ii - x][jj - x]):
                ul = False
        else:
            ul = False
        # for up right
        if ur and chess_isValid(jj + x, ii - x) and not chess_isOwn(boardState[ii - x][jj + x]):
            res.append((ii - x, jj + x))
            if not chess_isNothing(boardState[ii - x][jj + x]):
                ur = False
        else:
            ur = False
        # for down left
        if dl and chess_isValid(jj - x, ii + x) and not chess_isOwn(boardState[ii + x][jj - x]):
            res.append((ii + x, jj - x))
            if not chess_isNothing(boardState[ii + x][jj - x]):
                dl = False
        else:
            dl = False
        # for down right
        if dr and chess_isValid(jj + x, ii + x) and not chess_isOwn(boardState[ii + x][jj + x]):
            res.append((ii + x, jj + x))
            if not chess_isNothing(boardState[ii + x][jj + x]):
                dr = False
        else:
            dr = False

    return res


def hao_bishopMovesPrint(i, j, strOut):
    theMoves = hao_bishopMoves(i, j)
    for x in theMoves:
        if chess_isValid(x[1], x[0]):
            if not chess_isOwn(boardState[x[0]][x[1]]):
                strAppend = hao_myIndex2String(i, j) + '-' + hao_myIndex2String(x[0], x[1]) + '\n'
                strOut.append(strAppend)


def hao_bishopMoves(ii, jj):
    res = []
    ul = True
    ur = True
    dl = True
    dr = True
    for x in range(1, 5):
        # for up left
        if ul and chess_isValid(jj - x, ii - x) and not chess_isOwn(boardState[ii - x][jj - x]):
            res.append((ii - x, jj - x))
            if not chess_isNothing(boardState[ii - x][jj - x]):
                ul = False
        else:
            ul = False
        # for up right
        if ur and chess_isValid(jj + x, ii - x) and not chess_isOwn(boardState[ii - x][jj + x]):
            res.append((ii - x, jj + x))
            if not chess_isNothing(boardState[ii - x][jj + x]):
                ur = False
        else:
            ur = False
        # for down left
        if dl and chess_isValid(jj - x, ii + x) and not chess_isOwn(boardState[ii + x][jj - x]):
            res.append((ii + x, jj - x))
            if not chess_isNothing(boardState[ii + x][jj - x]):
                dl = False
        else:
            dl = False
        # for down right
        if dr and chess_isValid(jj + x, ii + x) and not chess_isOwn(boardState[ii + x][jj + x]):
            res.append((ii + x, jj + x))
            if not chess_isNothing(boardState[ii + x][jj + x]):
                dr = False
        else:
            dr = False
    # up
    if chess_isValid(jj, ii - 1) and chess_isNothing(boardState[ii - 1][jj]):
        res.append((ii - 1, jj))
    # down
    if chess_isValid(jj, ii + 1) and chess_isNothing(boardState[ii + 1][jj]):
        res.append((ii + 1, jj))
    # left
    if chess_isValid(jj - 1, ii) and chess_isNothing(boardState[ii][jj - 1]):
        res.append((ii, jj - 1))
    # right
    if chess_isValid(jj + 1, ii) and chess_isNothing(boardState[ii][jj + 1]):
        res.append((ii, jj + 1))

    return res

def hao_rookMovesPrint(i, j, strOut):
    theMoves = hao_rookMoves(i, j)
    for x in theMoves:
        if chess_isValid(x[1], x[0]):
            if not chess_isOwn(boardState[x[0]][x[1]]):
                strAppend = hao_myIndex2String(i, j) + '-' + hao_myIndex2String(x[0], x[1]) + '\n'
                strOut.append(strAppend)


def hao_rookMoves(ii, jj):
    res = []
    u = True
    d = True
    l = True
    r = True
    for x in range(1, 6):
        # for up
        if u and chess_isValid(jj, ii - x) and not chess_isOwn(boardState[ii - x][jj]):
            res.append((ii - x, jj))
            if not chess_isNothing(boardState[ii - x][jj]):
                u = False
        else:
            u = False
        # for down
        if d and chess_isValid(jj, ii + x) and not chess_isOwn(boardState[ii + x][jj]):
            res.append((ii + x, jj))
            if not chess_isNothing(boardState[ii + x][jj]):
                d = False
        else:
            d = False
        # for left
        if l and chess_isValid(jj - x, ii) and not chess_isOwn(boardState[ii][jj - x]):
            res.append((ii, jj - x))
            if not chess_isNothing(boardState[ii][jj - x]):
                l = False
        else:
            l = False
        # for right
        if r and chess_isValid(jj + x, ii) and not chess_isOwn(boardState[ii][jj + x]):
            res.append((ii, jj + x))
            if not chess_isNothing(boardState[ii][jj + x]):
                r = False
        else:
            r = False
    return res

def hao_kingMovesPrint(i, j, strOut):
    theMoves = hao_kingMoves(i, j)
    for x in theMoves:
        if chess_isValid(x[1], x[0]):
            if not chess_isOwn(boardState[x[0]][x[1]]):
                strAppend = hao_myIndex2String(i, j) + '-' + hao_myIndex2String(x[0], x[1]) + '\n'
                strOut.append(strAppend)

def hao_kingMoves(ii, jj):
    # generating all kings move
    res = []
    # ii-1
    res.append((ii - 1, jj - 1))
    res.append((ii - 1, jj))
    res.append((ii - 1, jj + 1))
    # ii
    res.append((ii, jj - 1))
    res.append((ii, jj + 1))
    # ii + 1
    res.append((ii + 1, jj - 1))
    res.append((ii + 1, jj))
    res.append((ii + 1, jj + 1))

    return res


def hao_knightMovesPrint(i, j, strOut):
    theMoves = hao_knightMoves(i, j)
    for x in theMoves:
        if chess_isValid(x[1], x[0]):
            if not chess_isOwn(boardState[x[0]][x[1]]):
                strAppend = hao_myIndex2String(i, j) + '-' + hao_myIndex2String(x[0], x[1]) + '\n'
                strOut.append(strAppend)


def hao_knightMoves(ii, jj):
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


def hao_pawnMovesPrint(target, i, j, strOut):
    theMoves = hao_pawnMoves(target, i, j)
    for x in theMoves:
        if chess_isValid(x[1], x[0]):
            if chess_isNothing(boardState[x[0]][x[1]]):
                strAppend = hao_myIndex2String(i, j) + '-' + hao_myIndex2String(x[0], x[1]) + '\n'
                strOut.append(strAppend)

    theMoves = hao_pawnCaptures(target, i, j)
    for x in theMoves:
        if chess_isValid(x[1], x[0]):
            if chess_isEnemy(boardState[x[0]][x[1]]):
                strAppend = hao_myIndex2String(i, j) + '-' + hao_myIndex2String(x[0], x[1]) + '\n'
                strOut.append(strAppend)


def hao_pawnMoves(theTarget, ii, jj):
    # generating all pawns move
    res = []
    if theTarget == 'p':
        res.append((ii + 1, jj))
    else:
        res.append((ii - 1, jj))
    return res

def hao_pawnCaptures(theTarget, ii, jj):
    # generating all pawns capture
    res = []
    if theTarget == 'p':
        res.append((ii + 1, jj - 1))
        res.append((ii + 1, jj + 1))
    else:
        res.append((ii - 1, jj - 1))
        res.append((ii - 1, jj + 1))
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

def hao_String2myIndex(strIn):
    # convert chess index to my board index
    # example "a2" --> (4,0)
    rowConvert = {
        '6': 0,
        '5': 1,
        '4': 2,
        '3': 3,
        '2': 4,
        '1': 5,
    }
    ii = rowConvert.get(strIn[1], -1)

    colConvert = {
        'a': 0,
        'b': 1,
        'c': 2,
        'd': 3,
        'e': 4,
    }
    jj = colConvert.get(strIn[0], -1)
    return ii, jj

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
    global whoseTurn
    global gameCounter
    theMoves = chess_moves()
    ss = str(strIn).split("-")
    iStart, jStart = hao_String2myIndex(ss[0])
    iEnd, jEnd = hao_String2myIndex(ss[1])
    ss = hao_myIndex2String(iStart, jStart) + '-' + hao_myIndex2String(iEnd, jEnd) + '\n'
    if ss in theMoves:
        boardState[iEnd][jEnd] = boardState[iStart][jStart]
        boardState[iStart][jStart] = '.'
        if boardState[iEnd][jEnd] == 'p' and iEnd == 5:
            boardState[iEnd][jEnd] = 'q'
        if boardState[iEnd][jEnd] == 'P' and iEnd == 0:
            boardState[iEnd][jEnd] = 'Q'
    if whoseTurn == 'W':
        whoseTurn = 'B'
    elif whoseTurn == 'B':
        whoseTurn = 'W'
        gameCounter += 1


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
