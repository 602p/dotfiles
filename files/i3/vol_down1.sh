amixer sset 'Master' $(expr $(amixer sget 'Master' | grep -o '\[.*%' | sed 's/\[//' | sed 's/%//' | tail -n 1) - 2)% unmute
if amixer sget 'Master' | grep -o "\[0%\]"; then
	amixer sset 'Master' 0% mute
fi
pkill -RTMIN+1 i3blocks