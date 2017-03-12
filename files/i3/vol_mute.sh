if amixer sget 'Master' | grep -o "\[on\]"; then
	amixer sset 'Master' mute
else
	amixer sset 'Master' unmute
fi
killall -USR1 i3status