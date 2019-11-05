import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def test_asdf_version(host):
    cmd = host.run('/root/.asdf/bin/asdf --version')

    assert cmd.rc == 0
    assert 'v0.7.5' in cmd.stdout
