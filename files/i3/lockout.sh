export DISPLAY=:0
if [ "$1" = "undo" ];
then
        xinput | grep -o 'id=[0-9]*' | grep -o '[0-9]*' | xargs -n 1 xinput enable
        echo Enabled
else
        xinput | grep -o 'id=[0-9]*' | grep -o '[0-9]*' | xargs -n 1 xinput disable
        echo Disabled
fi  