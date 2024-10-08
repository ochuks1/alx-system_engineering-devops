# Puppet Manifest to optimize Nginx configuration
# Description: This manifest optimizes Nginx configuration to handle more requests
# Adjusts the file descriptor limit for Nginx to manage increased traffic.

# Increase the file descriptor limit in the Nginx configuration
exec { 'increase-nginx-ulimit':
  command => 'sed -i "s/15/4096/" /etc/default/nginx',
  path    => '/usr/local/bin:/bin',
}

# Restart Nginx to apply the changes
exec { 'restart-nginx':
  command => '/etc/init.d/nginx restart',
  path    => '/etc/init.d',
}
