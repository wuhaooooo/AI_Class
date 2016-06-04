import chess
import random

class Zobrist:

    # zobrist number for white
    ZW = 0xffffaaaabbbbccccddddeeee00001111
    # zobrist number for black
    ZB = 0x11112222333344445555666677770000
    zobristNumber = ZW

    squareNumber = [[1 for x in range(5)] for x in range(6)]

    m = random.sample(range(-1000, 1000), 30)
    for i in xrange(0, 6):
        for j in xrange(0, 5):
            squareNumber[i][j] = m[5*i + j]

    pieceNumber = {
        'p': 57,
        'P': -35,
        'r': 12,
        'R': -212,
        'n': 131,
        'N': -113,
        'b': 9,
        'B': -91,
        'q': 15,
        'Q': -135,
        'k': 30,
        'K': -301,
        '.': 45,
    }

    def __init__(self):
        board = chess.chess_boardGet()
        strIn = str(board)
        tempStr = str.split(strIn)
        if tempStr[1] == 'B':
            Zobrist.zobristNumber = Zobrist.ZB

        for i in xrange(0, 6):
            for j in xrange(0, 5):
                self.XOR(Zobrist.squareNumber[i][j], i, j)

    def XOR(self, piece, x, y):
        Zobrist.zobristNumber ^= Zobrist.pieceNumber.get(piece)*Zobrist.squareNumber[x][y]

    def update(self, theMove, oldSource, newSource, oldDest, newDest, whoNext):
        ss = str(theMove).split("-")
        iStart, jStart = chess.hao_String2myIndex(ss[0])
        iEnd, jEnd = chess.hao_String2myIndex(ss[1])
        self.XOR(oldSource, iStart, jStart)
        self.XOR(newSource, iStart, jStart)
        self.XOR(oldDest, iEnd, jEnd)
        self.XOR(newDest, iEnd, jEnd)
        if whoNext == 'W':
            Zobrist.zobristNumber ^= Zobrist.ZW
        else:
            Zobrist.zobristNumber ^= Zobrist.ZB

    def getZValue(self):
        return Zobrist.zobristNumber





