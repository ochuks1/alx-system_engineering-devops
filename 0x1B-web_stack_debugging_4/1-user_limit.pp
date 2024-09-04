# Puppet Manifest to fix OS configuration for user limits
# Description: This manifest modifies OS configuration to resolve "Too many open files" issue

file { '/etc/security/limits.conf':
  ensure  => file,
  content => "holberton soft nofile 4096\nholberton hard nofile 8192\n",
}

file { '/etc/pam.d/common-session':
  ensure  => file,
  content => "session required pam_limits.so\n",
}

file { '/etc/pam.d/common-session-noninteractive':
  ensure  => file,
  content => "session required pam_limits.so\n",
}
