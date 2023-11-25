# A puppet manifest - Install flask from pip3

package { 'Flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}

# A puppet manifest - Install Werkzeug from pip3

package { 'Werkzeug':
  ensure   => '2.1.1',
  provider => 'pip3'
}
