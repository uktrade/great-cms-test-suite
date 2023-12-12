# Great CMS Tests

[![circle-ci-image]][circle-ci]
[![codecov-image]][codecov]
[![docs-image]][docs]
[![gitflow-image]][gitflow]
[![semver-image]][semver]

**Test suite for the GREAT platform - The Department for Business and Trade (DBT)**

---

## Development

### Installing

    $ git clone https://github.com/uktrade/great-cms-test-suite
    $ cd great-cms-test-suite
    $ [create and activate virtual environment]
    $ make install_requirements
    $ make secrets
    $ make ARGUMENTS=migrate manage

### Requirements

* [Python 3.9](https://www.python.org/downloads/release/python-3913/)


### Install virtualenv

`pip` is required. Refer to the [pip website](https://pip.pypa.io/en/stable/getting-started/) for more info.

### Configuration

Secrets such as API keys and environment specific configurations are placed in `conf/env/secrets-do-not-commit` - a file
that is not added to version control. To create a template secrets file with dummy values run `make secrets`.

### Commands

| Command                       | Description |
| ----------------------------- | ------------|
| make clean                    | Delete pyc files |
| make flake8                   | Run flake8 linting only |
| make checks                   | Run black, isort and flake8 in check mode |
| make autoformat               | Run black and isort in file-editing mode |
| make manage <foo>             | Run arbitrary management command |
| make requirements             | Compile the requirements file |
| make install_requirements     | Installed the compile requirements file |
| make secrets                  | Create your secret env var file |
| make all_tests                | Run all tests |
| make confidence_tests         | Run tests labelled as confidence tests |
| make integration_tests        | Run integration tests |
| make load_tests               | Run load tests |
| make security_tests           | Run security tests |
| make ui_tests                 | Run UI tests |


### Folder structure
`integration` - contain integration tests
`load` - contain load tests
`security` - contain security tests
`ui` - contain ui tests

*Note it is envisaged that confidence tests are derived from marked tests in the above categories*
___

## Helpful links

* [Developers Onboarding Checklist](https://uktrade.atlassian.net/wiki/spaces/ED/pages/32243946/Developers+onboarding+checklist) /PS-IGNORE
* [Gitflow branching](https://uktrade.atlassian.net/wiki/spaces/ED/pages/737182153/Gitflow+and+releases)
* [GDS service standards](https://www.gov.uk/service-manual/service-standard)
* [GDS design principles](https://www.gov.uk/design-principles)
* [Github Hooks](https://pre-commit.com/hooks)

## Related projects:

https://github.com/uktrade?q=directory

https://github.com/uktrade?q=great
