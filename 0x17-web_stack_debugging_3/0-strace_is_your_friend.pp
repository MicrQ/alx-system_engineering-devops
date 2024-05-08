# a puppet manifest used to fix a server 500 status error
exec { 'strace':
  command  => 'sed -i "s/phpp/php/g" /var/www/html/wp-settings.php'
  provider => 'shell',
}
