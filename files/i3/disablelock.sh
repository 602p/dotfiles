if [ $1 ]
then
	i3-msg "[class=\"URxvt\" instance=\"lockdisable\"] floating enable; sticky enable; resize set 180 20; move position 1740 980" > /dev/null
	i3-msg "focus mode_toggle"
	printf "\033[1;31;5mLOCK DISABLED\033[0m"
	read
else
	killall xautolock
	xset dpms 0 0 0
	xset dpms force on
	xset -dpms
	urxvt -name lockdisable -e ~/.config/i3/disablelock.sh -child
	~/.config/i3/setupxautolock.sh
fi