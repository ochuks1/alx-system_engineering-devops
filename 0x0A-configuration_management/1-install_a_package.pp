# Puppet manifest to install Flask package version 2.1.0 using pip3
#
# This manifest ensures that Flask version 2.1.0 is installed.

package { 'Flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}
