vgs={}
with open("data.txt", 'r') as fd:
	for item in fd.readlines():
		shortcut, title, text, group, subgroup = (frag.strip().rstrip() for frag in item.split("||"))
		pos=vgs
		depth=0
		for char in shortcut[:-1]:
			if char not in pos:
				pos[char]={"_title":subgroup if depth>1 else group}
			pos=pos[char]
			depth+=1
		pos[shortcut[-1]]=[title, (text if text else title).split("''")[0]]

vgs["_title"]=""
import json
json.dump(vgs, open("data.json", 'w'))