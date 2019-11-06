import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def test_node_version(host):
    cmd = host.run('/bin/bash -lc \'node --version\'')

    assert cmd.rc == 0
    assert '13.0.1' in cmd.stdout
