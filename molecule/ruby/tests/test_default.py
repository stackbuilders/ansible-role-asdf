import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def test_ruby_version(host):
    cmd = host.run('/bin/bash -lc \'ruby --version\'')

    assert cmd.rc == 0
    assert '2.6.5' in cmd.stdout
