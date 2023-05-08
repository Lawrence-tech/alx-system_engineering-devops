# Puppet manifest to install and configure Nginx with a 301 redirect

package { 'nginx':
  ensure => 'installed',
}

file { '/var/www/html/index.html':
  ensure  => file,
  content => 'Hello World!',
}

file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => "
    server {
      listen 80 default_server;
      root /var/www/html;

      location /redirect_me {
        return 301 https://www.youtube.com/;
      }
    }
  ",
}

service { 'nginx':
  ensure => 'running',
  enable => true,
}
