# Nicholas Aubé
import random

class ChessGame():
	gameWon = False
	playerTurn = None

	'''
	RULES-----

	The player always plays as Os
	Os always go first


	'''
	# Empty board
	board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

	def __init__(self, boardInput = None):
		# Get the board if there is one passed in
		if boardInput is not None:
			self.board = boardInput

		self.printBoard()

		# Make sure the game isnt won already
		self.playerTurn = False
		self.checkWin()
		self.playerTurn = True
		self.checkWin()

		#See whose turn it is
		oCount = 0; xCount = 0
		for row in range(3):
			for col in range(3):
				if self.board[row][col] == "O":
					oCount += 1
				elif self.board[row][col] == "X":
					xCount += 1
		if oCount <= xCount:
			self.playerTurn = True
			print("\tO (Player) goes first")
		else:
			self.playerTurn = False
			print("\tX (AI) goes first")
		
		print()
		self.playGame()

	def getInput(self, text):
		val = None
		while(type(val) is not int):
			user_input = input (text)
			try:
				val = int(user_input)
				
			except ValueError:
				print("WARNING: Input was not an int, try again")

		return val

	def printBoard(self):
		print("\nCURRENT BOARDSTATE:")
		for row in range(3):
			line = " \t"
			for col in range(3):
				line += self.board[row][col] + " | "
			print(line[:len(line)-2])
			if(row < 2):
				print("\t---------")
		print()

	def tryMove(self, row, col):
		'''
		Try to make a move, returns true if successful
		returns false if row or column are not in range, or if position occupied
		'''

		token = "O" if self.playerTurn else "X"
		if(row not in [0, 1, 2] or col not in [0, 1, 2]):
			print("\t Incorrect values")
			return False
		elif(self.board[row][col] == " "):
			print("Successful move (" + str(row) + ", " + str(col) + ")")
			self.board[row][col] = token
			return True
		else:
			print("\t Position occupied")

		return False

	def AIMove(self):
		# Create a list of possible moves
		possibleMoves = []
		for row in range(3):
			for col in range(3):
				if self.board[row][col] == " ":
					possibleMoves.append((row, col))

		

		random.shuffle(possibleMoves)
		print(possibleMoves)
		return possibleMoves[0]

	def checkWin(self):
		#check down columns
		token = "O" if self.playerTurn else "X"
		output = False

		# Horizontal and Vertical lines 
		for row in range(3):
			hCount = 0
			vCount = 0
			for col in range(3):
				if (self.board[row][col] is token):
					hCount += 1
				if (self.board[col][row] is token):
					vCount += 1
			if hCount == 3 or vCount == 3:
				output = True

		# Diagonal lines
		if(self.board[0][0] is token and self.board[1][1] is token and self.board[2][2] is token):
			output = True
		elif(self.board[2][0] is token and self.board[1][1] is token and self.board[0][2] is token):
			output = True

		if output:
			name = "player " if self.playerTurn else "CPU "
			print("The " + name + "is the winner!\n")

		self.gameWon = output


	def playGame(self):
		'''
		Handles moves and win conditions until the game is over
		'''
		while (not self.gameWon):
			successfullMove = False
			y = None
			x = None

			if self.playerTurn is False:

				print("Ai's Turn\n")
				move = self.AIMove()
				successfullMove = self.tryMove(move[0], move[1])

			elif self.playerTurn is True:
				print("Player's Turn\n")
				# Get input
				y = self.getInput("What row would you like?      >")
				x = self.getInput("What column would you like?   >")
				
				# Try Moving
				successfullMove = self.tryMove(y, x)
				
			if successfullMove:
				self.printBoard()

				# check win condition
				self.checkWin()

				# Flip Turn
				self.playerTurn = not self.playerTurn
			print()

			

#Testing
#x = ChessGame(boardInput = [["X", "O", "X"], [" ", "O", "X"], ["X", "O", " "]])
x = ChessGame()
#x.printBoard()