# A Puppet manifest that kills a process named "killmenow"
# using the "pkill" command
# The "exec" resource is used to run the command
exec { 'killmenow':
  command => 'pkill killmenow',
  onlyif  => 'pgrep killmenow',
}
