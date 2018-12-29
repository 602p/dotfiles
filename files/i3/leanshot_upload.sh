#!/bin/bash
SCREENSHOT=$HOME/.i3/leanshot
# choose some file to save it to
FILE="$HOME/last_screenshot.png"
$SCREENSHOT selection -o $FILE
# optional: copy to clipboard
TS=$(date +%s%N)
source ~/.ssh-agent-info
scp "$HOME/last_screenshot.png" hylaea:www/.screenshots/.$TS.png
echo -ne "https://louis.members.acm.umn.edu/www/.screenshots/.$TS.png" | xclip -selection clipboard