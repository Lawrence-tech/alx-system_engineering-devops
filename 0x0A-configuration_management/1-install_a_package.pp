# A Puppet manifest that installs Flask version 2.1.0 from pip3.
#
# This manifest installs Flask using the pip3 package manager. It also ensures
# that Flask is installed at version 2.1.0, which may be useful if you need to
# maintain compatibility with a specific version of Flask.

package { 'python3-pip':
  ensure => installed,  # Ensure that pip3 is installed
}

# Install Flask using pip3, ensuring that version 2.1.0 is installed
package { 'Flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}
