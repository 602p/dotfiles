MOUSEID="$(xinput list --short | grep "PS/2 Generic Mouse" | python3 -c "i=input();print(i[i.index('=')+1:i.index('[')])")"

xinput --set-prop $MOUSEID "Evdev Middle Button Emulation" 1
xinput --set-prop $MOUSEID "Device Accel Constant Deceleration" 0.5