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

- Ansible >= 2.5

## Role Variables

All variables which can be overridden are stored in [defaults/main.yml](defaults/main.yml) file as well as in table below.

| Name           | Default Value | Description                        |
| -------------- | ------------- | -----------------------------------|
| `fluentd_custom_conf` | [] | Paths to custom configuration templates. [Configuration examples]( https://github.com/fluent/fluentd/tree/master/example). |
| `fluentd_metrics` | False | Enable or disable fluentd metrics exporter. Metrics exported in prometheus format |
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

The preferred way of locally testing the role is to use Docker and [molecule](https://github.com/metacloud/molecule) (v2.x). You will have to install Docker on your system. See Get started for a Docker package suitable to for your system.
All packages you need to can be specified in one line:
```sh
pip install ansible 'ansible-lint>=3.4.15' 'molecule>2.13.0' docker 'testinfra>=1.7.0' jmespath
```
This should be similar to one listed in `.travis.yml` file in `install` section.
After installing test suit you can run test by running
```sh
molecule test --all
```
For more information about molecule go to their [docs](http://molecule.readthedocs.io/en/latest/).

## Travis CI

Combining molecule and travis CI allows us to test how new PRs will behave when used with multiple ansible versions and multiple operating systems. This also allows use to create test scenarios for different role configurations. As a result we have a quite large test matrix (42 parallel role executions in case of [ansible-prometheus](https://github.com/cloudalchemy/ansible-prometheus)) which will take more time than local testing, so please be patient.

## Contributing

See [contributor guideline](CONTRIBUTING.md).

## License

This project is licensed under MIT License. See [LICENSE](/LICENSE) for more details.
