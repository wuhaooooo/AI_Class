import random

class Zobrist:

    # zobrist number for white
    ZW = 0xffffaaaabbbbcccc
    # ZW = 0xffffaaaabbbbccccddddeeee00001111
    # zobrist number for black
    ZB = 0x1111222233334444
    # ZB = 0x11112222333344445555666677770000
    zobristNumber = ZW

    squareNumber = [[1 for x in range(5)] for x in range(6)]

    m = random.sample(range(-999999, 999999), 43)
    for i in xrange(0, 6):
        for j in xrange(0, 5):
            squareNumber[i][j] = m[5*i + j]

    pieceNumber = {
        'p': m[30],
        'P': m[31],
        'r': m[32],
        'R': m[33],
        'n': m[34],
        'N': m[35],
        'b': m[36],
        'B': m[37],
        'q': m[38],
        'Q': m[39],
        'k': m[40],
        'K': m[41],
        '.': m[42],
    }

    def __init__(self, theboard):
        strIn = str(theboard)
        tempStr = str.split(strIn)
        if tempStr[1] == 'B':
            Zobrist.zobristNumber = Zobrist.ZB

        for i in xrange(0, 6):
            for j in xrange(0, 5):
                self.XOR(tempStr[i + 2][j], i, j)

    def XOR(self, piece, x, y):
        piece = Zobrist.pieceNumber.get(piece)
        square = Zobrist.squareNumber[x][y]
        updateValue = piece*square
        Zobrist.zobristNumber ^= updateValue

    def update(self, strIn, oldSource, newSource, oldDest, newDest, whoNext):
        ss = str(strIn).split("-")
        iStart, jStart = self.String2myIndex(ss[0])
        iEnd, jEnd = self.String2myIndex(ss[1])
        self.XOR(oldSource, iStart, jStart)
        self.XOR(newSource, iStart, jStart)
        self.XOR(oldDest, iEnd, jEnd)
        self.XOR(newDest, iEnd, jEnd)

        Zobrist.zobristNumber ^= Zobrist.ZW
        Zobrist.zobristNumber ^= Zobrist.ZB

    def getZValue(self):
        return Zobrist.zobristNumber


    def String2myIndex(self, strIn):
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




