# Puppet manifest to execute a command that kills a process named "killmenow"
#
# This manifest uses the exec resource to execute pkill command to kill the process.

exec { 'killmenow':
  command => 'pkill killmenow',
  path    => '/bin:/usr/bin',
  onlyif  => 'pgrep killmenow',
}
