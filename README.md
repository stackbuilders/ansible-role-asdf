# Ansible Role: asdf

[![Build Status](https://travis-ci.org/sestrella/ansible-role-asdf.svg?branch=master)](https://travis-ci.org/sestrella/ansible-role-asdf)

Installs [asdf](https://github.com/asdf-vm/asdf) on Linux.

## Usage

### Requirements

None.

### Role Variables

Available variables are listed below, along with [default
values](defaults/main.yml):

```yml
asdf_repo: https://github.com/asdf-vm/asdf.git
```

The URL from which asdf will be cloned.

```yml
asdf_dir: ~/.asdf
```

The location where asdf will be cloned.

```yml
asdf_version: v0.7.5
```

The version of asdf that will be installed.

```yml
asdf_legacy_version_file: "no"
```

If set to `yes` it will cause plugins that support this feature to read the
version files used by other version managers (e.g. `.ruby-version` in the case
of Ruby’s `rbenv`).

```yml
asdf_use_release_candidates: "no"
```

If set to `yes` it will cause the `asdf update` command to upgrade to the
latest release candidate release instead of the latest semantic version.

### Dependencies

None.

### Example Playbook

```yml
- hosts: servers
  roles:
    - sestrella.asdf
```

## Development

Install tox:

```sh
pip install tox
```

Run all the tests:

```sh
tox -e py37-ansible29 -- molecule test
```

## License

MIT

## Author Information

This role was created by Sebastián Estrella.
