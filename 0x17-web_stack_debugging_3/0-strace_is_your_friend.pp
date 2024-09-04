# Puppet Manifest to fix WordPress configuration
# Description: This manifest fixes the WordPress configuration issue by replacing 'phpp' with 'php' in wp-settings.php

exec { 'fix-wordpress':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => ['/usr/local/bin', '/usr/bin', '/bin'],
}
