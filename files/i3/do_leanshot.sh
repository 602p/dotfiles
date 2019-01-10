#!/bin/bash
set -e
SCREENSHOT=$HOME/.config/i3/leanshot
# choose some file to save it to
FILE="$HOME/.last_screenshot.png"
$SCREENSHOT selection -o $FILE
# optional: copy to clipboard
XCLIP=/usr/bin/xclip
$XCLIP -selection clipboard -t image/png -i $FILE