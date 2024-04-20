#Set up client config file

file {'~/.ssh/config':
ensure  => 'present',
path    => '~/.ssh/config',
mode    => '0644',
content => 'Host *\nUser ubuntu\IdentityFile ~/.ssh/school\nPasswordAuthentication no'
}
