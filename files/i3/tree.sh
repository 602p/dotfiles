xdotool getwindowfocus windowfocus --sync
sleep 0.12
xdotool type --delay=10 
cat ~/.i3/tree.txt | xclip
sleep 0.05
xdotool key Return