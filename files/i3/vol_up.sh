amixer sset 'Master' $(expr $(amixer sget 'Master' | grep -o '\[.*%' | sed 's/\[//' | sed 's/%//' | tail -n 1) + 5)% unmute
pkill -RTMIN+1 i3blocks