import subprocess, pygame, time, sys

conn = subprocess.Popen(['ssh', '-C', sys.argv[1]],
	stdin=subprocess.PIPE)
pygame.init()
screen = pygame.display.set_mode((200,200))
pygame.event.set_grab(True)

# time.sleep(1)

clock=pygame.time.Clock()


pygame.key.set_repeat(125, 50)

run=True
while run:
	clock.tick(60)
	total_rel=[0, 0]
	pygame.key.set_mods(0)
	for e in pygame.event.get():
		if e.type==pygame.QUIT:
			run=False
		if e.type==pygame.KEYDOWN:
			if e.key==pygame.K_F1:
				run=False
			elif 'unicode' in dir(e):
				# print(e)
				keystr=chr(e.key)
				map={
					pygame.K_SPACE: 'space',
					pygame.K_RETURN: 'Return',
					pygame.K_BACKSPACE: 'BackSpace',
					pygame.K_PERIOD: 'period',
					pygame.K_COMMA: 'comma',
					pygame.K_SEMICOLON: 'semicolon',
					pygame.K_QUOTE: 'apostrophe',
					pygame.K_EQUALS: 'equal',
					pygame.K_MINUS: 'minus',
					pygame.K_SLASH: 'slash',
					pygame.K_BACKSLASH: 'backslash',
					pygame.K_LEFTBRACKET: 'bracketleft',
					pygame.K_RIGHTBRACKET: 'bracketright',
					pygame.K_ESCAPE: 'Escape',
					pygame.K_UP: 'Up',
					pygame.K_LEFT: 'Left',
					pygame.K_RIGHT: 'Right',
					pygame.K_DOWN: 'Down',
					pygame.K_TAB: 'Tab',
					pygame.K_LCTRL: 'Control_L',
					pygame.K_LSHIFT: 'Shift',
					pygame.K_LSUPER: 'Super_L',
					pygame.K_LALT: 'Alt_L',
					pygame.K_BACKQUOTE: 'grave',
					pygame.K_CAPSLOCK: 'Caps_Lock'
				}
				if e.key in map:
					keystr=map[e.key]
				if pygame.key.get_pressed()[pygame.K_LCTRL] and not e.key==pygame.K_LCTRL:
					keystr="Control_L+"+keystr
				if pygame.key.get_pressed()[pygame.K_LSHIFT] and not e.key==pygame.K_LSHIFT:
					keystr="Shift+"+keystr
				if pygame.key.get_pressed()[pygame.K_LSUPER] and not e.key==pygame.K_LSUPER:
					keystr="Super_L+"+keystr
				if pygame.key.get_pressed()[pygame.K_LALT] and not e.key==pygame.K_LALT:
					keystr="Alt_L+"+keystr
				# print("--->", keystr)
				try:
					conn.stdin.write(b"DISPLAY=:0 xdotool key \"%b\"\n"%keystr.encode("ascii"))
					conn.stdin.flush()
				except UnicodeEncodeError:
					pass
		if e.type==pygame.MOUSEMOTION:
			if e.pos!=(100,100):
				total_rel[0]+=e.rel[0]
				total_rel[1]+=e.rel[1]
		if e.type==pygame.MOUSEBUTTONDOWN:
			conn.stdin.write(b"DISPLAY=:0 xdotool mousedown %i\n"%e.button)
			conn.stdin.flush()
		if e.type==pygame.MOUSEBUTTONUP:
			conn.stdin.write(b"DISPLAY=:0 xdotool mousedown %i\n"%e.button)
			conn.stdin.flush()
	if sum(total_rel):
		# print(total_rel)
		conn.stdin.write(b"DISPLAY=:0 xdotool mousemove_relative -- %i %i\n"%tuple(total_rel))
		conn.stdin.flush()
		pygame.mouse.set_pos((100,100))