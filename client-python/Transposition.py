class Transposition:

    def __init__(self, score, alpha, beta, flag):
        self.score = score
        self.alpha = alpha
        self.beta = beta
        self.flag = flag

    def getALL(self):
        return [self.score, self.alpha, self.beta, self.flag]