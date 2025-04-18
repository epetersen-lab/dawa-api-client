VENV = venv
VENV_PYTHON    = $(VENV)/bin/python
SYSTEM_PYTHON  = $(or $(shell which python3), $(shell which python))
# If virtualenv exists, use it. If not, find python using PATH
PYTHON         = $(or $(wildcard $(VENV_PYTHON)), $(SYSTEM_PYTHON))
PIP            = $(dir $(VENV_PYTHON))pip

PKG_NAME = $(shell grep -A 1 '\[project\]' pyproject.toml | grep 'name' | sed 's/.*=\s*//' | sed 's/"//g')

.PHONY: clean deps deps-dev dev dist lint pkg-name test venv
.SILENT: pkg-name

default: dist

deps: venv
	$(PIP) install -r requirements.txt

deps-dev: venv
	$(PIP) install -r requirements-dev.txt

dist: venv deps deps-dev test
	$(PIP) install build
	$(PYTHON) -m build .

lint: venv
	$(PYTHON) -m flake8 src/
	$(PYTHON) -m flake8 tests/

dev: pkg-name venv deps deps-dev
	$(PIP) show $(PKG_NAME) > /dev/null || $(PIP) install -e .

pkg-name:
	if [ -z "$(PKG_NAME)" ]; then \
		echo "Project name could not be found. Please make sure the 'name' field is the first line within the [project] section of your pyproject.toml"; \
		exit 1; \
	else \
		echo "Project name is: '$(PKG_NAME)'"; \
	fi

test: venv deps-dev dev
	$(PYTHON) -m unittest discover tests

# Dev/build environment
$(VENV_PYTHON):
	$(SYSTEM_PYTHON) -m venv $(VENV)

venv: $(VENV_PYTHON)

clean:
	find . -type f -name *.pyc -delete
	find . -type d -name __pycache__ -delete
	rm -rf .pytest_cache
	rm -rf src/*.egg-info
	rm -rf dist
	rm -rf $(VENV)

