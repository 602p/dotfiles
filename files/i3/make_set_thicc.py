
hexn = lambda c:hex(ord(c))[2:]

with open("set_thicc.sh", 'w') as fd:
	fd.write("xmodmap -pke > ~/.i3/old.xmodmap\n")
	alpha="abcdefghijklmnopqrstuvwxyz1234567890"
	for char in alpha:
		lower=("卂乃匚刀乇下厶卄工丁长乚从𠘨口尸㔿尺丂丅凵リ山乂丫乙①②③④⑤⑥⑦⑧⑨⓪"[alpha.index(char)])
		upper=("卂乃匚刀乇下厶卄工丁长乚从𠘨口尸㔿尺丂丅凵リ山乂丫乙!@#$%^&*()"[alpha.index(char.lower())])
		fd.write("xmodmap -e \"keysym "+char+" = U"+hexn(lower)+" U"+hexn(upper)+"\"\n")