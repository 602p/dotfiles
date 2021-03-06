#!/bin/bash

set -e

# printf "<screenshot upload in progress...>" | xclip -selection clipboard
~/.config/i3/notifypaste screenshot upload in progress ... &
NOTIFYpASTE_PID=$!


maim -s -u > "$HOME/.last_screenshot.png"

TS=$(date +%s%N)
source ~/.ssh-agent-info
scp "$HOME/.last_screenshot.png" hylaea:www/.screenshots/.$TS.png
printf "https://louis.members.acm.umn.edu/www/.screenshots/.$TS.png" | xclip -selection clipboard
kill $NOTIFYpASTE_PID