
#Board is array of length 14
# D 0 1 2 3 4 5 6
# D C B A 9 8 7 6

class Board:
	__slots__=['pieces', 'moves']
	def __init__(self, pieces, calculate_move_depth=0):
		self.pieces=pieces
		if calculate_move_depth:
			pass
		else:
			self.moves=None

	def show(self):
		print("   ", end="")
		for i in range(7):
			print("%02i "%i, end="")
		print()
		for i in range(14, 7, -1):
			print("%02i "%i, end="")
		print()

Board([]).show()