# Puppet Manifest for SSH Client Configuration

# Define SSH client configuration file
file { '/home/ubuntu/.ssh/config':  # Update path as necessary
  ensure => file,
  owner  => 'ubuntu',               # Update owner as necessary
  group  => 'ubuntu',               # Update group as necessary
  mode   => '0600',                 # Permissions for the config file
  content => template('ssh/config.erb'),  # Use a template for configuration
}

# Ensure SSH client configuration options are correctly set
file_line { 'Turn off passwd auth':
  ensure  => present,
  path    => '/home/ubuntu/.ssh/config',  # Update path as necessary
  line    => 'PasswordAuthentication no',
}

file_line { 'Declare identity file':
  ensure  => present,
  path    => '/home/ubuntu/.ssh/config',  # Update path as necessary
  line    => 'IdentityFile ~/.ssh/school',
}
