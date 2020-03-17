def clear(): __import__("os").system("clear")
man=help
import json as j
import os
from math import *
def jl(f):
	with open(f, 'r') as fd:
		d=j.load(fd)
	return d
system=os.system
def banner(x):system("banner "+x)
def odir(x):return [a for a in dir(x) if not a.startswith("__")]
thing1=lambda:banner("Objects are Dicts")
thing2=lambda:banner("This aint 1933 OOP")
thing3=lambda:banner("Classess are Objects")
dang=lambda:banner("\"This Is\" Dangerous Knowledge")
fmap = lambda f,l:list(map(f,l))
sind = lambda x:sin(radians(x))
cosd = lambda x:cos(radians(x))
tand = lambda x:cos(radians(x))
