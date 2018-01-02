<a href="https://www.fluentd.org">
    <img src="https://www.fluentd.org/assets/img/miscellany/fluentd-logo.png" alt="fluentd logo" title="fluentd" align="right" height="60" />
</a>

# Ansible Role: fluentd

[![Build Status](https://travis-ci.org/cloudalchemy/ansible-fluentd.svg?branch=master)](https://travis-ci.org/cloudalchemy/ansible-fluentd)
[![License: MIT](https://img.shields.io/badge/license-MIT%20License-brightgreen.svg)](https://opensource.org/licenses/MIT)
[![Ansible Role](http://img.shields.io/badge/ansible%20role-cloudalchemy.fluentd-blue.svg)](https://galaxy.ansible.com/cloudalchemy/fluentd/)
[![GitHub tag](https://img.shields.io/github/tag/cloudalchemy/ansible-fluentd.svg)](https://github.com/cloudalchemy/ansible-fluentd/tags)

## Description

Install and manage [fluentd](https://github.com/fluent/fluentd) log forwarder and agregator.

## Requirements

- Ansible > 2.2
- go-lang installed on deployer machine (same one where ansible is installed)

## Role Variables

All variables which can be overridden are stored in [defaults/main.yml](defaults/main.yml) file as well as in table below.

| Name           | Default Value | Description                        |
| -------------- | ------------- | -----------------------------------|
| `fluentd_additional_conf` | [] | Paths to custom configuration templates |
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

The preferred way of locally testing the role is to use Docker and [molecule](https://github.com/metacloud/molecule) (v1.25). You will have to install Docker on your system. See Get started for a Docker package suitable to for your system.
All packages you need to can be specified in one line:
```sh
pip install ansible ansible-lint>=3.4.15 molecule==1.25.0 docker testinfra>=1.7.0
```
This should be similiar to one listed in `.travis.yml` file in `install` section. 
After installing test suit you can run test by running
```sh
molecule test
```
For more information about molecule go to their [docs](http://molecule.readthedocs.io/en/stable-1.25/).

## Contributing

See [contributor guideline](CONTRIBUTING.md).

## License

This project is licensed under MIT License. See [LICENSE](/LICENSE) for more details.
