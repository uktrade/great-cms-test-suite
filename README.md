# Great CMS Tests

**Test suite for the GREAT platform - The Department for Business and Trade (DBT)**

---

## Development

### Installing

    $ git clone https://github.com/uktrade/great-cms-test-suite
    $ cd great-cms-test-suite
    $ [create and activate virtual environment]
    $ make install_requirements
    $ make secrets

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
| make requirements             | Compile the requirements file |
| make install_requirements     | Installed the compile requirements file |
| make secrets                  | Create your secret env var file |
| make all_tests                | Run all tests |
| make confidence_tests         | Run tests labelled as confidence tests |
| make integration_tests        | Run integration tests |
| make load_tests               | Run load tests |
| make security_tests           | Run security tests |
| make ui_tests                 | Run UI tests |
| make behavioural_tests_local       | Runs behave tests against a locally available browser |
| make behavioural_tests_browserstack| Runs behave tests on browserstack [`see below`](#browserstack) |


### Folder structure
* `behavioural` - UI tests written in `behave` syntax
* `integration` - contains integration tests
* `load` - contains load tests
* `security` - contains security tests
* `ui` - contains ui tests


*Note it is envisaged that confidence tests are derived from marked tests in the above categories*
___
## Behavioural tests

### Development workflow
1. Write tests and run against local browser using `make behavioural_tests_local`.

    * These tests will use the browser indicated by the test's tag, for example `@Chrome`

2. When the tests are passing run on [browerstack](#browserstack)

    * These tests will run on the device/browser combinations listed in `browserstack.yml`


#### Running a subset of tests
During development it is often necessary to repeatedly run a subset of tests. A full list of behave command line flags are available [here](https://behave.readthedocs.io/en/stable/behave.html#command-line-arguments). Of note are:

* Run work-in-progress tests.

    1. Tag features or scenarios with @wip, for an example scenario with a pre-existing @Chrome tag:

        ```
            @Chrome @wip
            Scenario: User can sign up to the EYB service

        ````

        Similarily we can indicate a complete feature is a work-in-progress, for example,

        ```
            @wip
            Feature: UK Export Academy
        ```
    2.  Add `-- -w` to the make command, i.e. `make behavioural_tests_local -- -w` to run work-in-progress tests.

* Run features with a filename that adheres to a pattern. For example `make behavioural_tests_local -- -i features/ukea.feature` will only run scenarios inside the `ukea.feature` file.

* Run features with a certain tag. For example:

        @Chrome @core_user_journey
        Scenario: User can sign up to the EYB service

    We can then run `make behavioural_tests_local -- -t core_user_journey`

### Browserstack
Browserstack can be used to evaluate the behave tests against the suite of devices defined in `browserstack.yml`. To use browserstack locally the environmental variables `BROWSERSTACK_USERNAME` and `BROWSERSTACK_ACCESS_KEY` must be present in `config/env/secrets-do-not-commit`.

## Helpful links

* [Developers Onboarding Checklist](https://uktrade.atlassian.net/wiki/spaces/ED/pages/32243946/Developers+onboarding+checklist) /PS-IGNORE
* [Gitflow branching](https://uktrade.atlassian.net/wiki/spaces/ED/pages/737182153/Gitflow+and+releases)
* [GDS service standards](https://www.gov.uk/service-manual/service-standard)
* [GDS design principles](https://www.gov.uk/design-principles)
* [Github Hooks](https://pre-commit.com/hooks)

## Related projects:

https://github.com/uktrade?q=directory

https://github.com/uktrade?q=great
