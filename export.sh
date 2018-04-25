cp files/bashrc ~/.bashrc
cp files/bash_aliases ~/.bash_aliases
mkdir ~/.ssh
cp -r files/ssh/* ~/.ssh
if [ ! -e ~/.boxrc ]
then
	cp files/min_boxrc ~/.boxrc
else
	echo ".boxrc present"
fi
