# Puppet manifest to create a file /tmp/school
#
# This manifest ensures the file /tmp/school exists with the following properties:
# - Permission: 0744
# - Owner: www-data
# - Group: www-data
# - Content: "I love Puppet"

file { '/tmp/school':
  ensure   => present,
  mode     => '0744',
  owner    => 'www-data',
  group    => 'www-data',
  content  => "I love Puppet\n",
}
