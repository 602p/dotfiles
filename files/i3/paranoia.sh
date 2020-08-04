ssh-agent -k
gpgconf --kill gpg-agent
keybase logout
rm ~/.ssh/controlmasters/*
fusermount3 -zu /files/media
killall -9 sshfs
