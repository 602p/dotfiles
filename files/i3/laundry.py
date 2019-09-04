import requests
import colorama
from colorama import Fore, Back, Style
import collections
import sys
import datetime

if len(sys.argv) != 3:
	print("Usage: laundry <school id> <room id>")
	sys.exit()

school = sys.argv[1]
room = sys.argv[2]

printr = lambda *a: print(*a, sep="", end="")

colorama.init(strip=False)

def print_appliance(type, name, desc):
	if desc == "Available":
		printr(Fore.GREEN)
	elif desc == "Out of service":
		printr(Style.DIM + Fore.RED)
	else:
		printr(Fore.RED)
	print(type + "\t" + name + ":  " + desc + Style.RESET_ALL)

j=requests.get("https://www.laundryview.com/api/c_room?loc="+school+"&room="+room).json()

schoolname = j['school_name']
roomname = next(filter(lambda x:x['laundry_room_location']==room, j['room_data']))['laundry_room_name']
printr("Report For:  ", schoolname, " - ", roomname, "\n")
printr("Timestamp :  ", datetime.datetime.now(), "\n")

unknown = collections.Counter()
j=requests.get("https://www.laundryview.com/api/currentRoomData?school_desc_key="+school+"&location="+room).json()
for o in sorted(j['objects'], key=lambda o:int(o.get('appliance_desc', 999))):
	if o['type'] == 'washFL':
		print_appliance("Washer", o['appliance_desc'], o['time_left_lite'])
	elif o['type'] == 'dblDry':
		print_appliance("Dryer", o['appliance_desc'], o['time_left_lite'])
		print_appliance("Dryer", o['appliance_desc2'], o['time_left_lite2'])
	else:
		unknown.update([o['type']])

if unknown:
	print("Ignored   :  " + ", ".join(k + (" (" + str(v) +")" if v!=1 else "") for k, v in unknown.items()))