# a puppet manifest that installs Nginx server on ubuntu machine and configures
package { 'nginx':
    ensure => installed,
}

file_line { '_redirect':
    ensure => 'present',
    path   => '/etc/nginx/sites-available/default',
    after  => 'listen 80 default_server;',
    line   => 'rewrite ^/redirect_me https://www.linkedin.com/in/abenetg permanent;',
}

file { '/var/www/html/index.html':
    content => 'Hello World!',
}

service { 'nginx':
    ensure  => 'running',
    require => Package['nginx'],
}
