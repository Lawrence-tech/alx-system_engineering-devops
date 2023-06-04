#!/usr/bin/env bash
# Install nginx, set up to listen to port 80 and change default page served to
# "Hello World!"
# Configure Nginx server so that /redirect_me is redirecting to another page

sudo apt-get -y update
sudo apt-get -y install nginx
sudo ufw allow 'Nginx HTTP'
echo "Hello World!" | sudo tee /var/www/html/index.nginx-debian.html

# configure redirection
new_str="\\trewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4\n\t301 Moved Permanently;"
sudo sed -i "42i$new_str" /etc/nginx/sites-available/default

# create custom error 404 page
echo "Ceci n'est pas une page" | sudo tee /var/www/html/error404
# configure custom error page to be served
new_str="\\terror_page 404 /error404;"
sudo sed -i "43i$new_str" /etc/nginx/sites-available/default

# restart nginx server
sudo service nginx restart
