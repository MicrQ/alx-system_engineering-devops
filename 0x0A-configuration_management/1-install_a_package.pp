# a puppet manifest that installs flask from pip3
package {'flask':
    ensure   => installed,
    provider => 'pip3',
}
