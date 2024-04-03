# a puppet manifest that installs Nginx server on ubuntu machine and configures
package { 'nginx':
    ensure => installed,
}

file_line { 'redirect':
    ensure => 'present',
    path   => '/etc/nginx/sites-enabled/default',
    after  => 'listen 80 default_server;',
    line   => 'rewrite ^/redirect_me www.linkedin.com/in/abenetg permanent;',
}

file { '/var/www/html/index.nginx-debian.html':
    ensure  => 'present',
    content => 'Hello World!',
}

service { 'nginx':
    ensure  => 'running',
    require => package['nginx'],
}
