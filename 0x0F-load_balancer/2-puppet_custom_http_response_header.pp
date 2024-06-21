# Define the Nginx class
class nginx_custom_header {

    # Package resource to ensure Nginx is installed
    package { 'nginx':
        ensure => installed,
    }

    # File resource to manage Nginx configuration file
    file { '/etc/nginx/nginx.conf':
        ensure  => file,
        replace => true,
        content => template('nginx/nginx.conf.erb'), # Using a template for configuration
        notify  => Service['nginx'], # Restart Nginx when config changes
    }

    # Service resource to manage Nginx service
    service { 'nginx':
        ensure    => running,
        enable    => true,
        hasstatus => true,
        hasrestart => true,
    }
}

# Apply the Nginx class
include nginx_custom_header
