rm -rf files/*
mkdir files/i3
mkdir files/sublime-text-3
mkdir files/ssh
mkdir files/ssh/controlmasters
touch files/ssh/controlmasters/.exists
cp -r ~/.i3/* files/i3
cp ~/.bash_aliases files/bash_aliases
cp ~/.bashrc files/bashrc
cp ~/.pythonrc.py files/pythonrc.py
cp ~/.config/sublime-text-3/ files/sublime-text-3 -r
#cp "$(echo ~)/.config/sublime-text-3/Packages/User/Default (Linux).sublime-keymap" files/sublime-text-3
#cp ~/.config/sublime-text-3/Packages/Boxy\ Theme/schemes/* files/sublime-text-3
cp ~/.Xresources files/Xresources
rm -rf files/sublime-text-3/sublime-text-3/Index
cp ~/.ssh/config files/ssh/config
cp ~/.ssh/known_hosts files/ssh/known_hosts
cp /opt/nbfc/Configs/HP\ EliteBook\ 8570p.xml files
