# a manifest tha create a file '/tmp/school'.
file {'/tmp/school':
    ensure  => present,
    content => 'I love Puppet',
    mode    => '0744',
    owner   => 'www-data',
    group   => 'www-data',
}
