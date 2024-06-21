# Puppet Manifest to fix Apache 500 Internal Server Error
# Description: Fixing issue identified with strace where Apache returns 500 error

# Ensure the index.php file exists with correct permissions
file { '/var/www/html/index.php':
  ensure => file,
  source => 'puppet:///modules/my_module/index.php',
  mode   => '0644',
  owner  => 'www-data',
  group  => 'www-data',
}

# Restart Apache to apply changes
service { 'apache2':
  ensure    => running,
  enable    => true,
  subscribe => File['/var/www/html/index.php'],
}

