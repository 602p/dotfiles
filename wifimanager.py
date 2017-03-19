from curses import wrapper
import curses
import subprocess
import collections
import datetime
import os

WiFiNetwork=collections.namedtuple("WiFiNetwork", ['name', 'security'])

def runcmd(cmdline):
	return subprocess.Popen(cmdline, shell=True,stdout=subprocess.PIPE).stdout

def get_wifi_options():
	#return [WiFiNetwork("ABCD", []), WiFiNetwork("DEEZNUTS", ["WPA"]), WiFiNetwork("cucktown", ['a', 'b', 'c'])]
	lines=[line.decode("ascii", errors="ignore") for line in runcmd("nmcli d wifi list").readlines()]
	wifis=[]
	for line in lines[1:]:
		name=line[3:].split(" ")[0]
		security=[]
		for sectype in ["WPA1", "WPA2", "TKIP", "WEP"]:
			if line.find(sectype)!=-1:
				security.append(sectype)
		if name!="--":
			wifis.append(WiFiNetwork(name=name, security=security))
	return wifis

def main(scr):
	curses.noecho()
	curses.cbreak()
	networks=get_wifi_options()
	selected=0
	last_refresh=datetime.datetime.now()
	while 1:
		scr.clear()

		scr.addstr(0, 0, "(q) To Quit, (r) To Refresh, (Up) and (Down) to navigate, and (Enter) to connect")
		scr.addstr(1, 0, "WiFi Networks Availible: (Last Refresh ")
		scr.addstr(str(last_refresh))
		scr.addstr(")")
		scr.addstr(2, 0, "="*100)

		if len(networks)==0:
			scr.addstr(3, 0, "No networks availible")
		else:
			for i, network in enumerate(networks):
				scr.addstr(3+i, 0, " x " if i==selected else " o ")
				scr.addstr(network.name+": "+(", ".join(network.security) if network.security else "Unsecured"), curses.A_REVERSE if i==selected else 0)
		
		key=scr.getkey()
		if key.lower()=="q":
			break
		elif key.lower()=="r":
			networks=get_wifi_options()
			last_refresh=datetime.datetime.now()
			if selected>=len(networks):
				selected=len(networks)-1
		elif key=="KEY_UP":
			selected=selected-1 if selected>0 else 0
		elif key=="KEY_DOWN":
			selected=selected+1 if selected<len(networks)-1 else len(networks)-1
		elif key=="\n":
			if selected<len(networks) and selected>-1:
				command="nmcli dev wifi con \"%s\""%networks[selected].name
				if networks[selected].security:
					scr.clear()
					scr.addstr(0, 0, "Connecting to WiFi %s (Security type%s %s)..."
						%(networks[selected].name, "s" if len(networks[selected].security)>1 else "", ", ".join(networks[selected].security)))
					scr.addstr(1, 0, "Enter Password:")
					curses.echo()
					password=scr.getstr()
					command+=" password \"%s\""%password.decode("ascii")
				curses.endwin()
				os.system("clear")
				print("Running `%s`..."%command)
				os.system(command)
				return
		scr.refresh()

try:
	wrapper(main)
except KeyboardInterrupt:
	pass