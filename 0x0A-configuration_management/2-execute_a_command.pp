#!/usr/bin/pup
# Kill a process with killmenow

exec {
  command => 'pkill killmenow',
  provider => 'shell',
}