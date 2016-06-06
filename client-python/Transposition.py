class Transposition:

    def __init__(self, score, flag, depth):
        self.score = score
        self.flag = flag
        self.depth = depth

    def getALL(self):
        return [self.score, self.flag, self.depth]