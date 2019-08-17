#!/usr/bin/env python3

import subprocess, sys, time, os

os.system("printf <clipboard upload in progress...> | xclip -selection clipboard")

def r(*a): return subprocess.run(*a, capture_output=True).stdout

opts = r(["xclip", "-selection", "clipboard", "-t", "TARGETS", "-o"]).decode("utf-8", "ignore").split()
print(opts)

if not opts: sys.exit(0)

res = None

for opt in opts:
	x = {
		"UTF8_STRING": "txt",
		"image/png": "png"
	}.get(opt)
	if x:
		res = x
		selopt = opt
		break

if not res:
	res = opts[-1].replace("/","")

lastpt = "sbh--"+str(time.time())+'--clipboard.'+res
name = "/tmp/"+lastpt
# 
print(name)

with open(name, 'wb') as fd:
	fd.write(r(["xclip", "-selection", "clipboard", "-t", selopt, "-o"]))

os.system("scp "+name+" hylaea:www/.share/."+lastpt)
os.system("printf https://louis.members.acm.umn.edu/www/.share/."+lastpt+" | xclip -selection clipboard")