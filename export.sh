cp files/bashrc ~/.bashrc
cp files/bash_aliases ~/.bash_aliases
cp files/pythonrc.py ~/.pythonrc.py
mkdir ~/.ssh
cp -r files/ssh/* ~/.ssh
if [ ! -e ~/.boxrc ]
then
	cp min_boxrc ~/.boxrc
else
	echo ".boxrc present"
fi
touch ~/.hushlogin
