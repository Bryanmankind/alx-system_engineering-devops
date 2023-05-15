file { '/etc/ssh/ssh_config':
  ensure  => present,
  owner   => 'root',
  group   => 'root',
  mode    => '0644',
  content => "# SSH Client Configuration\n
               Host server_alias\n
               HostName server_ip_address\n
               User username\n
               IdentityFile ~/.ssh/id_rsa\n",
}

