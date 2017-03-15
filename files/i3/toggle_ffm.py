import os, os.path

with open(os.path.expanduser('~/.i3/config'), 'r') as fd:
	text=fd.read()

if "#toggle_ffm toggle this" in text:
	if "focus_follows_mouse no #toggle_ffm toggle this" in text:
		text=text.replace("focus_follows_mouse no #toggle_ffm toggle this", "focus_follows_mouse yes #toggle_ffm toggle this")
	else:
		text=text.replace("focus_follows_mouse yes #toggle_ffm toggle this", "focus_follows_mouse no #toggle_ffm toggle this")

with open(os.path.expanduser('~/.i3/config'), 'w') as fd:
	fd.write(text)

os.system("i3-msg reload")