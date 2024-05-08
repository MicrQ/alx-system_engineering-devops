# 0-strace_is_your_friend.pp

# Ensure the Apache service is installed and running
package { 'apache2':
  ensure => installed,
}

service { 'apache2':
  ensure => running,
  enable => true,
}

# Fix the PHP version causing the 500 error by upgrading PHP to a compatible version
package { 'php5':
  ensure  => '5.5.38-3+deb.sury.org~xenial+1', # Adjust version according to compatibility
  require => Service['apache2'],
}

# Restart Apache after PHP upgrade
service { 'apache2':
  ensure    => running,
  subscribe => Package['php5'],
}
