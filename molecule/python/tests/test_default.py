import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def test_python_version(host):
    cmd = host.run('/root/.asdf/installs/python/3.8.0/bin/python --version')

    assert cmd.rc == 0
    assert '3.8.0' in cmd.stdout
