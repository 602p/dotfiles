if amixer sget 'Master' | grep -o "\[on\]"; then
	amixer sset 'Master' mute
else
	amixer sset 'Master' unmute
	amixer sset 'Speaker+LO' unmute
fi
pkill -RTMIN+1 i3blocks