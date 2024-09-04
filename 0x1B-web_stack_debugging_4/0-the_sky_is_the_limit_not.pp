# Puppet Manifest to optimize Nginx configuration
# Description: This manifest optimizes Nginx configuration to handle more requests
# Adjusts the file descriptor limit for Nginx to manage increased traffic.

# Update the file descriptor limit in Nginx's default configuration
exec { 'adjust-nginx-ulimit':
  command => 'sed -i "s/15/4096/" /etc/default/nginx',
  path    => '/usr/local/bin:/bin',
} ->

# Restart the Nginx service to apply changes
exec { 'restart-nginx':
  command => '/etc/init.d/nginx restart',
  path    => '/etc/init.d',
}
