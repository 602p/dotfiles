i3-msg 'mark --add music_snapback'
i3-msg '[con_mark="music_player"] focus'
sleep 0.05
xdotool key k
sleep 0.05
i3-msg '[con_mark="music_snapback"] focus'