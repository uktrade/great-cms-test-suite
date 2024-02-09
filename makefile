ARGUMENTS = $(filter-out $@,$(MAKECMDGOALS)) $(filter-out --,$(MAKEFLAGS))

clean:
	-find . -type f -name "*.pyc" -delete
	-find . -type d -name "__pycache__" -delete
	-rm -fr ./allure_report/
	-rm -fr ./allure_results/

# configuration for black and isort is in pyproject.toml
autoformat:
	isort $(PWD)
	black $(PWD)

checks:
	isort $(PWD) --check
	black $(PWD) --check --verbose
	flake8 .

flake8:
	flake8 . \
	--exclude=ENV,ENV2,.venv,venv,node_modules,migrations \
	--max-line-length=120

manage:
	ENV_FILES='secrets-do-not-commit,dev' ./manage.py $(ARGUMENTS)

requirements:
	pip-compile --upgrade -r --annotate requirements.in
	pip-compile --upgrade -r --annotate requirements_dev.in

install_requirements:
	pip install -q -r requirements.txt -r requirements_dev.txt
	pre-commit install --install-hooks

secrets:
	@if [ ! -f ./config/env/secrets-do-not-commit ]; \
		then sed -e 's/#DO NOT ADD SECRETS TO THIS FILE//g' config/env/secrets-template > config/env/secrets-do-not-commit \
			&& echo "Created config/env/secrets-do-not-commit"; \
		else echo "config/env/secrets-do-not-commit already exists. Delete first to recreate it."; \
	fi

behavioural_tests_local:
	ENV_FILES='secrets-do-not-commit,dev' behave ./tests/behavioural/features/

behavioural_tests_browserstack:
	ENV_FILES='secrets-do-not-commit,dev' BEHAVE_USE_BROWSERSTACK=True browserstack-sdk behave ./tests/behavioural/features/

confidence_tests:
	echo "Error: confidence tests not configured" && exit 1

integration_tests:
	echo "Error: integration tests not configured" && exit 1

load_tests:
	echo "Error: load tests not configured" && exit 1

security_tests:
	echo "Error: security tests not configured" && exit 1

ui_tests:
	echo "Error: ui tests not configured" && exit 1

unit_tests:
	echo "Error: unit tests not configured" && exit 1

all_tests:
	make behavioural_tests;
	make confidence_tests;
	make integration_tests;
	make load_tests;
	make security_tests;
	make ui_tests;
	make unit_tests;
