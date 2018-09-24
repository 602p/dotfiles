try:
	x=input()
	print(x if x else -1)
except EOFError:
	print(-1)
