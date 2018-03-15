i3-msg 'mark --add music_snapback'
i3-msg '[con_mark="music_player"] focus'
sleep 0.1
xdotool key k
sleep 0.1
i3-msg '[con_mark="music_snapback"] focus'