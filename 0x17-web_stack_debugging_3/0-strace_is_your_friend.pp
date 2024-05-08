# 0-strace_is_your_friend.pp
exec { 'fix':
  command => 'sed -i "s/pphp/php/g /var/www/html/wp-settings.php',
  path    => '/usr/local/bin/:/bin/'
}
