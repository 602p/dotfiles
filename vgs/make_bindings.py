import json
from pprint import pprint
vgs=json.load(open("data.json", 'r'))

modes={}

def find_modes(layer, path):
	for key, item in layer.items():
		if type(item)==dict and "_title" in item:
			modes[path+key]=item
			find_modes(item, path+key)
find_modes(vgs, "")

def get_layer(path):
	pos=vgs
	for char in path:
		pos=pos[char]
	return pos

def get_mode_name(path):
	mode=get_layer(path)
	return ">%s - %s"%(path, " | ".join(k+": "+("*"+mode[k]["_title"] if "_title" in mode[k] else mode[k][0]) for k in mode.keys() if k!="_title"))

pprint(modes)

with open("bindings.txt", 'w') as fd:
	fd.write("\n\n###START VGS AUTOGEN###\n")
	for path, mode in modes.items():
		fd.write("mode \"%s\" {\n"%get_mode_name(path))
		for key, member in mode.items():
			if key!="_title":
				fd.write("\tbindsym "+key.lower()+" ")
				if type(member)==list:
					fd.write("exec bash ~/.i3/pasta.sh \""+member[1]+"\"; mode \"default\"")
				else:
					fd.write(" mode \""+get_mode_name(path+key)+"\"")
				fd.write("\n")
		fd.write("\n\tbindsym Return mode \"default\"\n")
		fd.write("\n\tbindsym Escape mode \"default\"\n")
		fd.write("}\n")

	fd.write("bindsym $mod+v mode \"%s\""%get_mode_name("V"))
	fd.write("\n\n###END VGS AUTOGEN###\n")