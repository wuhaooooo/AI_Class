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
	boardState[0] = ['k','q','b','n','r']
	boardState[1] = ['p','p','p','p','p']
	boardState[2] = ['.','.','.','.','.']
	boardState[3] = ['.','.','.','.','.']
	boardState[4] = ['P','P','P','P','P']
	boardState[5] = ['R','N','B','Q','K']
	whoseTurn = 'W'
	gameCounter = 1




def chess_boardGet():
	# return the state of the game - one example is given below - note that the state has exactly 40 or 41 characters
	
	strOut = ''
	strOut = str(gameCounter) + ' ' + whoseTurn + '\n'
	for i in xrange(0,6):
		for j in xrange(0,5):
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
	for i in xrange(0,6):
		for j in xrange(0,5):
			boardState[i][j] = tempStr[i+2][j]



def chess_winner():
	# determine the winner of the current state of the game and return '?' or '=' or 'W' or 'B' - note that we are returning a character and not a string
	
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
	
	return False


def chess_isOwn(strPiece):
	# with reference to the state of the game, return whether the provided argument is a piece from the side on move - note that we could but should not use the other is() functions in here but probably
	
	return False


def chess_isNothing(strPiece):
	# return whether the provided argument is not a piece / is an empty field - note that we could but should not use the other is() functions in here but probably
	
	return False


def chess_eval():
	# with reference to the state of the game, return the the evaluation score of the side on move - note that positive means an advantage while negative means a disadvantage
	
	return 0


def chess_moves():
	# with reference to the state of the game and return the possible moves - one example is given below - note that a move has exactly 6 characters
	
	strOut = []
	
	strOut.append('a2-a3\n')
	strOut.append('b2-b3\n')
	strOut.append('c2-c3\n')
	strOut.append('d2-d3\n')
	strOut.append('e2-e3\n')
	strOut.append('b1-a3\n')
	strOut.append('b1-c3\n')
	
	return strOut


def chess_movesShuffled():
	# with reference to the state of the game, determine the possible moves and shuffle them before returning them- note that you can call the chess_moves() function in here
	
	return []


def chess_movesEvaluated():
	# with reference to the state of the game, determine the possible moves and sort them in order of an increasing evaluation score before returning them - note that you can call the chess_moves() function in here
	
	return []


def chess_move(strIn):
	# perform the supplied move (for example 'a5-a4\n') and update the state of the game / your internal variables accordingly - note that it advised to do a sanity check of the supplied move
	
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
