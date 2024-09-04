# Puppet Manifest to fix Apache 500 Internal Server Error
# Description: This manifest ensures that the index.php file exists with correct permissions
# and restarts the Apache service to resolve a 500 Internal Server Error issue.

# Ensure the index.php file exists with correct permissions
file { '/var/www/html/index.php':
  ensure  => file,
  source  => 'puppet:///modules/my_module/index.php',
  mode    => '0644',
  owner   => 'www-data',
  group   => 'www-data',
}

# Ensure Apache is running and configured properly
service { 'apache2':
  ensure    => running,
  enable    => true,
  subscribe => File['/var/www/html/index.php'], # Restart Apache if index.php changes
}

# Optionally, ensure the Apache configuration is reloaded if needed
exec { 'reload_apache':
  command => '/usr/sbin/apachectl graceful',
  path    => '/usr/sbin:/usr/bin',
  refreshonly => true,
  subscribe  => File['/var/www/html/index.php'], # Reload Apache if index.php changes
}
