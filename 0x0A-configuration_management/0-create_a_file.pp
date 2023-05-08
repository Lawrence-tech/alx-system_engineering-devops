# A Puppet manifest that creates a file in /tmp called school, with specific
# permissions, ownership, and content.
#
# The file will be owned by the www-data user and group, with permissions set
# to 0744. The contents of the file will be the string "I love Puppet".
#
# This manifest can be used to quickly create a file with the specified settin
# which may be useful for testing or as part of a larger Puppet configuration.

file { '/tmp/school':
  ensure  => present,
  mode    => '0744',  # Set permissions to 0744 (rwxr--r--)
  owner   => 'www-data',  # Set file owner to www-data
  group   => 'www-data',  # Set file group to www-data
  content => 'I love Puppet',  # Set file contents to "I love Puppet"
}
