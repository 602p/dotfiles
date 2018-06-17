def clear(): __import__("os").system("clear")
man=help
import json as j
def jl(f):
	with open(f, 'r') as fd:
		d=j.load(fd)
	return d
