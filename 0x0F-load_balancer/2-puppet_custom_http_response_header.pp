# Puppet manifest to configure Nginx with a custom HTTP header
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

class { 'nginx':
    manage_repo => true,
}

nginx::resource::server { 'BarbieCathy':
    listen_port => 80,
    server_name => 'BarbieCathy',
}

nginx::resource::location { 'root':
    server => 'BarbieCathy',
    location => '/',
    ensure => present,
    add_header => {
        'X-Served-By' => '487685-web-01', # Change to 487685-web-02 for the second server
    },
}
