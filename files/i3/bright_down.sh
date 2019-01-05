#!/bin/bash
brightnessctl set $(expr $(brightnessctl i --machine-readable | cut -d, -f4 | head -c-2) - 5)%
killall -USR1 i3status