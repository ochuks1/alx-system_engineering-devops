# Puppet Manifest to fix Apache 500 Internal Server Error
# Description: Fixing issue identified with strace where Apache returns 500 error


exec { 'fix-wordpress':
  command => '/usr/sbin/php5enmod mbstring && service apache2 restart',
  path    => ['/usr/bin', '/usr/sbin', '/bin', '/sbin'],
  onlyif  => '/usr/sbin/php5query -m | grep -q mbstring',
}
