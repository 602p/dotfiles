hexn = lambda c:hex(ord(c))[2:]

with open("set_fullwidth.sh", 'w') as fd:
	fd.write("xmodmap -pke > ~/.i3/old.xmodmap\n")
	alpha="abcdefghijklmnopqrstuvwxyz1234567890"
	for char in alpha:
		lower=("ａｂｃｄｅｆｇｈｉｊｋｌｍｎｏｐｑｒｓｔｕｖｗｘｙｚ①②③④⑤⑥⑦⑧⑨⓪"[alpha.index(char)])
		upper=("ＡＢＣＤＥＦＧＨＩＪＫＬＭＮＯＰＱＲＳＴＵＶＷＸＹＺ①②③④⑤⑥⑦⑧⑨⓪"[alpha.index(char.lower())])
		fd.write("xmodmap -e \"keysym "+char+" = U"+hexn(lower)+" U"+hexn(upper)+"\"\n")