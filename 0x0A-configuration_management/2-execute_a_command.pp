# a puppet manifest that kill a process named 'killmenow'.
exec { 'killProcess' :
    command => '/usr/bin/pkill -f killmenow',
    onlyif  => '/usr/bin/pgrep -f killmenow',
    path    => '/usr/bin',
}