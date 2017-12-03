xdotool getwindowfocus windowfocus --sync ; sleep 0.1
xdotool type --delay=10 "$(python3 ~/.i3/fullwidth.py $1)"