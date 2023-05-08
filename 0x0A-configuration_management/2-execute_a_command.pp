# A Puppet manifest that kills a process named "killmenow"
# using the "pkill" command
# The "exec" resource is used to run the command
# The manifest uses the 'pkill' command with the '-9' option to forcefully
# terminate the process.
# It also includes an 'onlyif' parameter to check if the process is running
# before attempting to kill it.
# The 'path' parameter specifies the paths where the command can be found.

exec { 'killing a process using pkill':
command => 'pkill -9 killmenow',
path => '/usr/bin:/bin',
onlyif => 'pgrep killmenow',
provider => shell,
}
