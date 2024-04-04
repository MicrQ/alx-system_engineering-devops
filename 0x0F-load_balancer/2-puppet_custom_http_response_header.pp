# a puppet manifest that installs Nginx server and configures the server block file.
exec { 'Nginx_conf':
  command  => 'apt-get update -y; apt-get install nginx -y;
  sed -i "/listen 80 default_server;/a add_header X-Served-By $(hostname);" /etc/nginx/sites-enabled/default;
  service nginx restart',
  provider => 'shell',
}
