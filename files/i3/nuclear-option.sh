if [ "$1" = "undo" ];
then
	echo "Undoing..."
	echo " - hestia"
	ssh -t hestia .nuclear/undo.sh
	echo " - argo"
	ssh -t argo .nuclear/undo.sh
	echo " - medusa"
	ssh -t medusa .nuclear/undo.sh
	echo " - clubby"
	ssh -t clubby .nuclear/undo.sh
else
	clear
	echo "===NUCLEAR OPTION==="
	read -p "Press enter to continue..."
	ssh hestia .nuclear/nuclear
	ssh argo .nuclear/nuclear
	ssh medusa .nuclear/nuclear
	ssh clubby .nuclear/nuclear
fi