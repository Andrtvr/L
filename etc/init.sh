sudo ln -s /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/
sudo rm /etc/nginx/sites-enabled/default
sudo /etc/init.d/mysql restart
sudo /etc/init.d/nginx restart
