#!/bin/bash

set -e

printf "<screenshot upload in progress...>" | xclip -selection clipboard

SCREENSHOT=$HOME/.config/i3/leanshot
# choose some file to save it to
FILE="$HOME/.last_screenshot.png"
$SCREENSHOT selection -o $FILE
# optional: copy to clipboard
TS=$(date +%s%N)
source ~/.ssh-agent-info
scp "$HOME/.last_screenshot.png" hylaea:www/.screenshots/.$TS.png
printf "https://louis.members.acm.umn.edu/www/.screenshots/.$TS.png" | xclip -selection clipboard