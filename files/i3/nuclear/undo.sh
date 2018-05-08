sudo adduser nathan sudo
sudo sed -i "/AllowUsers/d" /etc/ssh/sshd_config 
sudo service ssh restart
sudo service sshd restart
