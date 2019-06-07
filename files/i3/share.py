#!/usr/bin/env python3

import sys, time, os

arg = sys.argv[1]

name = "sbh--"+str(time.time())+'--'+os.path.basename(arg)

os.system("scp "+arg+" hylaea:www/.share/."+name)
os.system("printf https://louis.members.acm.umn.edu/www/.share/."+name+" | xclip -selection clipboard")