import random, sys, colorama
from colorama import Fore, Back, Style

colorama.init()

if len(sys.argv)!=2:
	print(Fore.RED+"E: Use as `dice 1d4+7`")
	sys.exit()

value=0
for thing in sys.argv[1].split("+"):
	thing=thing.strip()
	if thing:
		if "d" in thing:
			if thing.split("d")[0]=="" or int(thing.split("d")[0])==1:
				roll=random.randint(1, int(thing.split("d")[1]))
				if int(thing.split("d")[1])==20:
					if roll==20:
						print(" ", Back.GREEN, " ", Style.RESET_ALL, Fore.GREEN, " Nat 20 on roll!", Style.RESET_ALL, sep="")
					elif roll==1:
						print(" ", Back.RED, " ", Style.RESET_ALL, Fore.RED, " Nat 1 on roll!", Style.RESET_ALL, sep="")
				value+=roll
			else:
				rolls=[random.randint(1, int(thing.split("d")[1])) for _ in range(int(thing.split("d")[0]))]
				value+=sum(rolls)
		else:
			value+=int(thing)

print("=> ", Fore.CYAN, value, Style.RESET_ALL, sep="")
