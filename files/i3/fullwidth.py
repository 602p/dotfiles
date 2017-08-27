import sys
alpha="abcdefghijklmnopqrstuvwxyz"
char = sys.argv[1][0]
if char.lower() in alpha:
	if char.lower()==char:
		print("ａｂｃｄｅｆｇｈｉｊｋｌｍｎｏｐｑｒｓｔｕｖｗｘｙｚ"[alpha.index(char)])
	else:
		print("ＡＢＣＤＥＦＧＨＩＪＫＬＭＮＯＰＱＲＳＴＵＶＷＸＹＺ"[alpha.index(char.lower())])
else:
	print(char)