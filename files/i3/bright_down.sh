#!/bin/bash
# brightnessctl set $(expr $(brightnessctl i --machine-readable | cut -d, -f4 | head -c-2) - 5)%
sudo brightnessctl set $1-
killall -USR1 i3status