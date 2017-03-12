xdotool getwindowfocus windowfocus --sync
sleep 0.1
xdotool type --delay=10 "$@"
sleep 0.05
xdotool key Return