#!/usr/bin/env bash
#Script that sets up my web servers for the deployment of web_static.
sudo apt update -y
sudo apt install nginx -y
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/
sudo sh -c 'echo "hello from /hbnb_static" > /data/web_static/releases/test/index.html'
sudo rm -f /data/web_static/current
sudo ln -s /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
sudo sed -i "/server_name _;/a\\        location /hbnb_static {\n                alias /data/web_static/current/;\n        }" /etc/nginx/sites-enabled/default
sudo service nginx restart
