rm -rf files/*
mkdir files/i3
mkdir files/sublime-text-3
cp -r ~/.i3/* files/i3
cp ~/.bash_aliases files/bash_aliases
cp ~/.bashrc files/bashrc
cp ~/.config/sublime-text-3/ files/sublime-text-3 -r
#cp "$(echo ~)/.config/sublime-text-3/Packages/User/Default (Linux).sublime-keymap" files/sublime-text-3
#cp ~/.config/sublime-text-3/Packages/Boxy\ Theme/schemes/* files/sublime-text-3
cp ~/.Xresources files/Xresources
rm -rf files/sublime-text-3/sublime-text-3/Index
