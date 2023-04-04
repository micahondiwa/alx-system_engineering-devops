# Installs puppet-lint, version 2.1.1

package { 'puppet-lint':
  ensure   => '3.0.0',
  provider => 'gem',
}
