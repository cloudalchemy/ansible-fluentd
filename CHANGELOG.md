# Change Log

## [**Next release**](https://galaxy.ansible.com/cloudalchemy/fluentd)

**Implemented enhancements:**

- Different apprach to monitoring fluentd [\#15](https://github.com/cloudalchemy/ansible-fluentd/issues/15)

**Fixed bugs:**

- `fail on too small number of file descriptors` [\#35](https://github.com/cloudalchemy/ansible-fluentd/issues/35)

**Merged pull requests:**

- Synchronize files from cloudalchemy/skeleton [\#38](https://github.com/cloudalchemy/ansible-fluentd/pull/38) ([cloudalchemybot](https://github.com/cloudalchemybot))
- remove fluentd\_exporter as this feature is already integrated by using fluentd plugin [\#37](https://github.com/cloudalchemy/ansible-fluentd/pull/37) ([paulfantom](https://github.com/paulfantom))
- tasks: cast number of fds to int before assertion [\#36](https://github.com/cloudalchemy/ansible-fluentd/pull/36) ([paulfantom](https://github.com/paulfantom))
- Synchronize files from cloudalchemy/skeleton [\#34](https://github.com/cloudalchemy/ansible-fluentd/pull/34) ([cloudalchemybot](https://github.com/cloudalchemybot))
- added restartsec and startlimitinterval configurations [\#33](https://github.com/cloudalchemy/ansible-fluentd/pull/33) ([oguzhaninan](https://github.com/oguzhaninan))

## [0.1.0](https://galaxy.ansible.com/cloudalchemy/fluentd) (2019-05-04)
**Implemented enhancements:**

- Support plugins via jinja templates [\#2](https://github.com/cloudalchemy/ansible-fluentd/issues/2)

**Merged pull requests:**

- Synchronize files from cloudalchemy/skeleton [\#32](https://github.com/cloudalchemy/ansible-fluentd/pull/32) ([cloudalchemybot](https://github.com/cloudalchemybot))
- Wait for network to be online [\#31](https://github.com/cloudalchemy/ansible-fluentd/pull/31) ([paulfantom](https://github.com/paulfantom))
- Synchronize files from cloudalchemy/skeleton. [\#30](https://github.com/cloudalchemy/ansible-fluentd/pull/30) ([cloudalchemybot](https://github.com/cloudalchemybot))
- Make linter happy [\#29](https://github.com/cloudalchemy/ansible-fluentd/pull/29) ([jkrol2](https://github.com/jkrol2))
- Support configuration with jinja2 templates [\#28](https://github.com/cloudalchemy/ansible-fluentd/pull/28) ([jkrol2](https://github.com/jkrol2))
- Update preflight.yml [\#27](https://github.com/cloudalchemy/ansible-fluentd/pull/27) ([jkrol2](https://github.com/jkrol2))
- Remove Jinja2 templating delimiters under when [\#26](https://github.com/cloudalchemy/ansible-fluentd/pull/26) ([jkrol2](https://github.com/jkrol2))
- Modify gitignore [\#25](https://github.com/cloudalchemy/ansible-fluentd/pull/25) ([jkrol2](https://github.com/jkrol2))
- Update requirements in readme \[ci skip\] [\#24](https://github.com/cloudalchemy/ansible-fluentd/pull/24) ([jkrol2](https://github.com/jkrol2))
- Use tox for testing [\#23](https://github.com/cloudalchemy/ansible-fluentd/pull/23) ([jkrol2](https://github.com/jkrol2))
- \[ci skip\] Typo [\#21](https://github.com/cloudalchemy/ansible-fluentd/pull/21) ([jkrol2](https://github.com/jkrol2))
- Link to the documentation of v1.0 version [\#20](https://github.com/cloudalchemy/ansible-fluentd/pull/20) ([jkrol2](https://github.com/jkrol2))

## [0.0.9](https://galaxy.ansible.com/cloudalchemy/fluentd) (2019-02-02)
**Merged pull requests:**

- Use 3 latest ansible versions for testing [\#22](https://github.com/cloudalchemy/ansible-fluentd/pull/22) ([jkrol2](https://github.com/jkrol2))
- Fix issue when comparing string with int [\#19](https://github.com/cloudalchemy/ansible-fluentd/pull/19) ([xeroc](https://github.com/xeroc))

## [0.0.8](https://galaxy.ansible.com/cloudalchemy/fluentd) (2018-05-27)
**Fixed bugs:**

- fix architecture var parsing [\#18](https://github.com/cloudalchemy/ansible-fluentd/pull/18) ([paulfantom](https://github.com/paulfantom))

**Merged pull requests:**

- upgrade to molecule 2.x [\#16](https://github.com/cloudalchemy/ansible-fluentd/pull/16) ([paulfantom](https://github.com/paulfantom))
- Allow specifying plugin version [\#13](https://github.com/cloudalchemy/ansible-fluentd/pull/13) ([paulfantom](https://github.com/paulfantom))
- use binaries for metrics exporter [\#12](https://github.com/cloudalchemy/ansible-fluentd/pull/12) ([paulfantom](https://github.com/paulfantom))
- CI update; typos; docs [\#11](https://github.com/cloudalchemy/ansible-fluentd/pull/11) ([paulfantom](https://github.com/paulfantom))

## [0.0.7](https://galaxy.ansible.com/cloudalchemy/fluentd) (2018-01-12)
**Merged pull requests:**

- Plugins [\#10](https://github.com/cloudalchemy/ansible-fluentd/pull/10) ([jkrol2](https://github.com/jkrol2))

## [0.0.6](https://galaxy.ansible.com/cloudalchemy/fluentd) (2018-01-02)
**Implemented enhancements:**

- Add fluentd metrics exporter [\#3](https://github.com/cloudalchemy/ansible-fluentd/issues/3)

**Merged pull requests:**

- fix configuration files path [\#8](https://github.com/cloudalchemy/ansible-fluentd/pull/8) ([paulfantom](https://github.com/paulfantom))
- add metrics exporter [\#5](https://github.com/cloudalchemy/ansible-fluentd/pull/5) ([paulfantom](https://github.com/paulfantom))

## [0.0.5](https://galaxy.ansible.com/cloudalchemy/fluentd) (2018-01-01)
## [0.0.4](https://galaxy.ansible.com/cloudalchemy/fluentd) (2017-12-16)
**Merged pull requests:**

- fix tests; restart service when config changes [\#9](https://github.com/cloudalchemy/ansible-fluentd/pull/9) ([paulfantom](https://github.com/paulfantom))

## [0.0.3](https://galaxy.ansible.com/cloudalchemy/fluentd) (2017-12-11)
**Fixed bugs:**

- Fix service enabling on centos [\#1](https://github.com/cloudalchemy/ansible-fluentd/issues/1)

**Closed issues:**

- Use yum\_repository module [\#7](https://github.com/cloudalchemy/ansible-fluentd/issues/7)

**Merged pull requests:**

- use service module [\#4](https://github.com/cloudalchemy/ansible-fluentd/pull/4) ([jkrol2](https://github.com/jkrol2))

## [0.0.2](https://galaxy.ansible.com/cloudalchemy/fluentd) (2017-12-05)
## [0.0.1](https://galaxy.ansible.com/cloudalchemy/fluentd) (2017-12-04)


\* *This Change Log was automatically generated by [github_changelog_generator](https://github.com/skywinder/Github-Changelog-Generator)*