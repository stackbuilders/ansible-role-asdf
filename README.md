# Ansible Role: asdf

![CI](https://github.com/sestrella/ansible-role-asdf/workflows/CI/badge.svg)


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
asdf_version: v0.8.0
```

The version of asdf that will be installed.

```yml
asdf_legacy_version_file: false
```

If set to `true` it will cause plugins that support this feature to read the
version files used by other version managers (e.g. `.ruby-version` in the case
of Ruby’s `rbenv`).

```yml
asdf_use_release_candidates: false
```

If set to `true` it will cause the `asdf update` command to upgrade to the
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

Create a virtual environment:

```sh
python -m venv .venv
```

Activate the virtual environment:

```sh
# bash, or zsh
source .venv/bin/activate
# fish
source .venv/bin/activate.fish
```

Install the dependencies:

```sh
pip install -r requirements.txt
```

Run all the tests:

```sh
mol test --all
```

## License

MIT

## Author Information

This role was created by Sebastián Estrella.
