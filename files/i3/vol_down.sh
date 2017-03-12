amixer sset 'Master' $(expr $(amixer sget 'Master' | grep -o '\[.*%' | sed 's/\[//' | sed 's/%//' | tail -n 1) - 5)% unmute
if amixer sget 'Master' | grep -o "\[0%\]"; then
	amixer sset 'Master' 0% mute
fi
killall -USR1 i3status