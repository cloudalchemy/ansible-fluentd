<a href="https://www.fluentd.org">
    <img src="https://www.fluentd.org/assets/img/miscellany/fluentd-logo.png" alt="fluentd logo" title="fluentd" align="right" height="60" />
</a>

# Ansible Role: fluentd

[![Build Status](https://travis-ci.org/cloudalchemy/ansible-fluentd.svg?branch=master)](https://travis-ci.org/cloudalchemy/ansible-fluentd)
[![License: MIT](https://img.shields.io/badge/license-MIT%20License-brightgreen.svg)](https://opensource.org/licenses/MIT)
[![Ansible Role](http://img.shields.io/badge/ansible%20role-cloudalchemy.fluentd-blue.svg)](https://galaxy.ansible.com/cloudalchemy/fluentd/)
[![GitHub tag](https://img.shields.io/github/tag/cloudalchemy/ansible-fluentd.svg)](https://github.com/cloudalchemy/ansible-fluentd/tags)
[![IRC](https://img.shields.io/badge/irc.freenode.net-%23cloudalchemy-yellow.svg)](https://kiwiirc.com/nextclient/#ircs://irc.freenode.net/#cloudalchemy)

## Important. Maintainer needed!

We are currently looking for a maintainer for this repository, if you know someone who would like to become one, let us know. Unfortunatelly if we don't find any volunteers we will need to archive this repository.

## Description

Install and manage [fluentd](https://github.com/fluent/fluentd) log forwarder and agregator.

## Requirements

- Ansible >= 2.7 (It might work on previous versions, but we cannot guarantee it)

## Role Variables

All variables which can be overridden are stored in [defaults/main.yml](defaults/main.yml) file as well as in table below.

| Name           | Default Value | Description                        |
| -------------- | ------------- | -----------------------------------|
| `fluentd_custom_conf` | [] | Paths to custom configuration templates. [Configuration examples]( https://github.com/fluent/fluentd/tree/master/example). |
| `fluentd_plugins` | [] | List of additional plugins |

## Example

### Playbook

Use it in a playbook as follows:
```yaml
- hosts: all
  become: true
  roles:
    - cloudalchemy.fluentd
```

### Demo site

We provide demo site for full monitoring solution based on prometheus and grafana. Repository with code and links to running instances is [available on github](https://github.com/cloudalchemy/demo-site) and site is hosted on DigitalOcean.

## Local Testing

The preferred way of locally testing the role is to use Docker and [molecule](https://github.com/metacloud/molecule) (v2.x). You will have to install Docker on your system. See "Get started" for a Docker package suitable to for your system.
We are using tox to simplify process of testing on multiple ansible versions. To install tox execute:
```sh
pip3 install tox
```
To run tests on all ansible versions (WARNING: this can take some time)
```sh
tox
```
To run a custom molecule command on custom environment with only default test scenario:
```sh
tox -e py35-ansible28 -- molecule test -s default
```
For more information about molecule go to their [docs](http://molecule.readthedocs.io/en/latest/).

If you would like to run tests on remote docker host just specify `DOCKER_HOST` variable before running tox tests.

## Travis CI

Combining molecule and travis CI allows us to test how new PRs will behave when used with multiple ansible versions and multiple operating systems. This also allows use to create test scenarios for different role configurations. As a result we have a quite large test matrix which will take more time than local testing, so please be patient.

## Contributing

See [contributor guideline](CONTRIBUTING.md).

## License

This project is licensed under MIT License. See [LICENSE](/LICENSE) for more details.
