#!/bin/bash
echo $(expr $(cat /sys/class/backlight/radeon_bl0/brightness) + 5) | tee /sys/class/backlight/radeon_bl0/brightness
killall -USR1 i3status