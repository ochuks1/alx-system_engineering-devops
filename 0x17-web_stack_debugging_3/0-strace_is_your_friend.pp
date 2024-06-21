# Puppet Manifest to fix Apache 500 Internal Server Error
# Description: Fixing issue identified with strace where Apache returns 500 error

# Example: If the error was due to a missing file that Apache was trying to serve
file { '/var/www/html/index.php':
  ensure => present,
  source => '/path/to/valid/index.php',
  mode   => '0644',
  owner  => 'www-data',
  group  => 'www-data',
}

# Example: Restart Apache to apply changes
service { 'apache2':
  ensure    => running,
  enable    => true,
  subscribe => File['/var/www/html/index.php'],
}
