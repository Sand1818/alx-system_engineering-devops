#!/usr/bin/pup
# Kill a process with killmenow

exec { 'pkill':
  command  => 'pkill killmenow',
  provider => 'shell',
}