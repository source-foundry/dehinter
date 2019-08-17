all: install

clean:
	- rm dist/*.whl dist/*.tar.gz dist/*.zip

dist-build: clean
	python3 setup.py sdist bdist_wheel

dist-push:
	twine upload dist/*.whl dist/*.tar.gz

install:
	pip3 install --ignore-installed -r requirements.txt .

install-dev:
	pip3 install --ignore-installed -r requirements.txt -e ".[dev]"

install-user:
	pip3 install --ignore-installed --user .

test: test-lint test-type-check test-unit

test-coverage:
	coverage run --source dehinter -m py.test
	coverage report -m
#	coverage html

test-lint:
	flake8 --ignore=E501,W50 lib/dehinter

test-type-check:
	pytype lib/dehinter

test-unit:
	tox

uninstall:
	pip3 uninstall --yes fontelemetry

.PHONY: all clean dist-build dist-push install install-dev install-user test test-lint test-type-check test-unit uninstall