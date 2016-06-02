import random
import time
##########################################################
boardState = [['.' for x in range(5)] for x in range(6)]
whoseTurn = 'W'
gameCounter = 1
movesStack = []
INFINITY = 10000
timeLeft = 0

def chess_reset():
    # reset the state of the game / your internal variables - note that this function is highly dependent on your implementation
    global boardState
    global whoseTurn
    global gameCounter
    global movesStack
    boardState[0] = ['k', 'q', 'b', 'n', 'r']
    boardState[1] = ['p', 'p', 'p', 'p', 'p']
    boardState[2] = ['.', '.', '.', '.', '.']
    boardState[3] = ['.', '.', '.', '.', '.']
    boardState[4] = ['P', 'P', 'P', 'P', 'P']
    boardState[5] = ['R', 'N', 'B', 'Q', 'K']
    whoseTurn = 'W'
    gameCounter = 1
    del movesStack[:]



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


    for i in xrange(0, 6):
        for j in xrange(0, 5):
            if (boardState[i][j] == 'k'):
                bKing = 1
            if (boardState[i][j] == 'K'):
                wKing = 1

    if bKing == 1 and wKing == 0:
        return 'B'
    elif bKing == 0 and wKing == 1:
        return 'W'
    elif gameCounter > 40:
        return '='
    return '?'

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
        'p': 5,
        'P': 5,
        'r': 12,
        'R': 12,
        'n': 11,
        'N': 11,
        'b': 9,
        'B': 9,
        'q': 15,
        'Q': 15,
        'k': 30,
        'K': 30,
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


def chess_moves():
    # with reference to the state of the game and return the possible moves - one example is given below - note that a move has exactly 6 characters
    """ Determines all the possible moves of the current state
        The input/output is expected to be in a well defined format
        returns a string/array"""
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

# hw3
def chess_movesShuffled():
    # with reference to the state of the game, determine the possible moves and shuffle them before returning them- note that you can call the chess_moves() function in here
    res = chess_moves()
    random.shuffle(res)
    return res


def getKey(item):
    return item[0]


# hw3
def chess_movesEvaluated():
    # with reference to the state of the game, determine the possible moves and sort them in order of an increasing evaluation score before returning them - note that you can call the chess_movesShuffled() function in here
    res = chess_moves()
    temp = []
    for move in res:
        chess_move(move)
        score = chess_eval()
        temp.append([score, move])
        chess_undo()
    temp = sorted(temp, key=getKey)
    del res[:]
    for move in temp:
        res.append(move[1])
    return res


def chess_move(strIn):
    # perform the supplied move (for example 'a5-a4\n') and update the state of the game / your internal variables accordingly - note that it advised to do a sanity check of the supplied move
    """ Performs the provided move
        The provided move is in a well defined format
        the board/state and therefore the internal variables need to be updated accordingly"""
    global whoseTurn
    global gameCounter
    theMoves = chess_moves()
    ss = str(strIn).split("-")
    #board2Store = chess_boardGet()
    iStart, jStart = hao_String2myIndex(ss[0])
    iEnd, jEnd = hao_String2myIndex(ss[1])
    toStore = [iStart, jStart, iEnd, jEnd, boardState[iStart][jStart], boardState[iEnd][jEnd]]
    #print toStore
    ss = hao_myIndex2String(iStart, jStart) + '-' + hao_myIndex2String(iEnd, jEnd) + '\n'
    if ss in theMoves:
        boardState[iEnd][jEnd] = boardState[iStart][jStart]
        boardState[iStart][jStart] = '.'
        if boardState[iEnd][jEnd] == 'p' and iEnd == 5:
            boardState[iEnd][jEnd] = 'q'
        if boardState[iEnd][jEnd] == 'P' and iEnd == 0:
            boardState[iEnd][jEnd] = 'Q'
    else:
        return
    if whoseTurn == 'W':
        whoseTurn = 'B'
    elif whoseTurn == 'B':
        whoseTurn = 'W'
        gameCounter += 1
    movesStack.append(toStore)

# hw4
def chess_moveRandom():
    # perform a random move and return it - one example output is given below - note that you can call the chess_movesShuffled() function as well as the chess_move() function in here
    moves = chess_movesShuffled()
    chess_move(moves[0])
    return moves[0]

# hw4
def chess_moveGreedy():
    # perform a greedy move and return it - one example output is given below - note that you can call the chess_movesEvaluated() function as well as the chess_move() function in here
    moves = chess_movesEvaluated()
    chess_move(moves[0])
    return moves[0]


def chess_moveNegamax(intDepth, intDuration):
    # perform a negamax move and return it - one example output is given below - note that you can call the the other functions in here
    # startTime = time.time()
    best = ''
    score = -INFINITY
    moves = chess_movesEvaluated()
    if intDepth == 0:
        return  
    for move in moves:
        chess_move(move)
        temp = -hao_negamax(intDepth-1)
        chess_undo()
        if temp > score:
            best = move
            score = temp
    chess_move(best)
    return best


def hao_negamax(intDepth):
    if intDepth == 0 or chess_winner() != '?':
        if chess_winner() == 'B' or chess_winner() == 'W':
            return -INFINITY
        return chess_eval()
    score = -INFINITY
    moves = chess_movesShuffled()
    for move in moves:
        chess_move(move)
        score = max(score, -hao_negamax(intDepth - 1))
        chess_undo()
    return score

breakingtimes = 0
def chess_moveAlphabeta(intDepth, intDuration=10000):
    # perform a alphabeta move and return it - one example output is given below - note that you can call the the other functions in here
    global breakingtimes
    # flag = 0 # 0 for test, 1 for tournament
    timeThisRound = 9999999
    currentTime = int(round(time.time() * 1000))

    if intDepth < 0:
        # flag = 1
        if gameCounter < 5:
            intDepth = 5
            timeThisRound = 10000
        # elif gameCounter < 10:
        #     intDepth = 5
        #     timeThisRound = 25000
        elif gameCounter < 20:
            intDepth = 5
            timeThisRound = 20000
        else:
            intDepth = 4
            timeThisRound = intDuration / (41 - gameCounter) + 4000

    best = ''
    alpha = -INFINITY
    beta = INFINITY
    moves = chess_movesEvaluated()

    for move in moves:
        if timeThisRound-(int(round(time.time() * 1000))-currentTime) < 0:
            breakingtimes += 1
            print("breaking due to the timebound " + str(breakingtimes))
            break
        chess_move(move)
        temp = -hao_alphabeta(intDepth-1, -beta, -alpha)
        chess_undo()
        if temp > alpha:
            best = move
            alpha = temp
    print("round:%s time spend "%(gameCounter) + str(((((time.time() * 1000))-currentTime))/1000))
    chess_move(best)
    return best


def hao_alphabeta(depth, alpha, beta):
    if depth == 0 or chess_winner() != '?':
        return chess_eval()
    score = - INFINITY
    moves = chess_moves()
    for move in moves:
        chess_move(move)
        score = max(score, -hao_alphabeta(depth-1, -beta, -alpha))
        chess_undo()
        alpha = max(alpha, score)
        if alpha >= beta:
            break
    return score

# hw3
def chess_undo():
    # undo the last move and update the state of the game / your internal variables accordingly - note that you need to maintain an internal variable that keeps track of the previous history for this
    global boardState
    global whoseTurn
    global gameCounter
    if len(movesStack) > 0:
        iStart, jStart, iEnd, jEnd, start, end = movesStack[-1]
        boardState[iStart][jStart] = start
        boardState[iEnd][jEnd] = end
        if whoseTurn == 'W':
            whoseTurn = 'B'
            gameCounter -= 1
        elif whoseTurn == 'B':
            whoseTurn = 'W'
        movesStack.pop()



