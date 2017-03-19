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
	#return []
	#return [WiFiNetwork("ABCD", []), WiFiNetwork("DEEZNUTS", ["WPA"]), WiFiNetwork("cucktown", ['a', 'b', 'c'])]
	lines=[line.decode("ascii", errors="ignore") for line in runcmd("nmcli d wifi list").readlines()]
	wifis=[]
	for line in lines[1:]:
		name=line[3:].split(" ")[0]
		security=[]
		for sectype in ["WPA1", "WPA2", "TKIP", "WEP", "802.1X"]:
			if line.find(sectype)!=-1:
				security.append(sectype)
		wifis.append(WiFiNetwork(name=name if name!="--" else "<Hidden>", security=security))
	return wifis

def main(scr):
	curses.noecho()
	curses.cbreak()
	scr.nodelay(1)
	networks=get_wifi_options()
	selected=0
	last_refresh=datetime.datetime.now()
	last_poll_time=last_refresh.second
	ticker="|/-\\"
	ticker_pos=0
	while 1:
		scr.clear()

		scr.addstr(0, 0, "(q) To Quit, (r) To Refresh, (Up) and (Down) to navigate, and (Enter) to connect")
		scr.addstr(1, 0, "WiFi Networks Availible: (Scanning... %s, Last Refresh "%ticker[ticker_pos])
		scr.addstr(str(last_refresh))
		scr.addstr(")")
		scr.addstr(2, 0, "="*100)

		i=0

		if len(networks)==0:
			scr.addstr(3, 0, "No networks availible")
		else:
			for network in networks:
				scr.addstr(3+i, 0, " x " if i==selected else " o ")
				scr.addstr(network.name+": "+(", ".join(network.security) if network.security else "Unsecured"), curses.A_REVERSE if i==selected else 0)
				i+=1

		scr.addstr(4+i, 0, " x " if i==selected else " o ")
		scr.addstr("Manual/Hidden Network (Enter SSID)", curses.A_REVERSE if i==selected else 0)
		try:
			key=scr.getkey()
		except:
			key=""
		if key.lower()=="q":
			break
		if key.lower()=="r" or (datetime.datetime.now()-last_refresh).seconds>0:
			networks=get_wifi_options()
			last_refresh=datetime.datetime.now()
			ticker_pos+=1
			if ticker_pos==len(ticker):
				ticker_pos=0
			if selected>len(networks):
				selected=len(networks)-1
		if key=="KEY_UP":
			selected=selected-1 if selected>0 else 0
		if key=="KEY_DOWN":
			selected=selected+1 if selected<len(networks) else len(networks)
		if key=="\n":
			scr.nodelay(0)
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
			elif selected==len(networks):
				scr.clear()
				scr.addstr(0, 0, "Connecting to manual WiFi (Security type(s) ?)...")
				scr.addstr(1, 0, "Enter SSID:")
				curses.echo()
				network=scr.getstr().decode("ascii")
				scr.addstr(2, 0, "Enter Password:")
				password=scr.getstr().decode("ascii")
				command="nmcli dev wifi con \"%s\" password \"%s\""%(network, password)
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