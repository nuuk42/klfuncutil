# shell - 
SHELL = /bin/bash
PRJHOME := $(CURDIR)
PROJECTNAME =klfuncutil
TARGETDIR = ./src/$(PROJECTNAME)
TESTDIR = ./tests
SETUPENV = source $(PRJHOME)/runtime/bin/activate
PY = $(SETUPENV)&&python
BLACK = $(SETUPENV)&&black
FLIT = $(SETUPENV)&&flit
VERSION := $(shell sed -n 's/^__version__ *= *"\([^"]*\)".*/\1/p' $(TARGETDIR)/__init__.py)

.PHONY: help py black testenv test_all runtime install build dist publish

help:
	@echo Usage
	@echo -----
	@echo make runtime - create/refresh the virtual environment
	@echo make test_all
	@echo make test_list
	@echo make test_tuple
	@echo make test_dict
	@echo make test_iter
	@echo make test_deep_copy
	@echo make test_repeat_iter_t
	@echo make test_repeat_iter_m
	@echo make test_tuplefactory
	@echo make testenv - build and install the current version in a test venv
	@echo make black
	@echo make py - Python prompt
	@echo make install - install package klfuncutil locally
	@echo make build - build sdist and wheel
	@echo make dist - alias for build
	@echo make publish - publish a new version on pypi

# open Python prompt
py: runtime
	$(PY)

black: runtime
	cd $(TARGETDIR)/&&$(BLACK) *.py
	cd tests/&&$(BLACK) *.py

# --------------------------------------------------------

testenv: build
	-rm -Rf testenv
	python3 -m venv testenv
	source ./testenv/bin/activate&&pip install --force-reinstall --no-index --find-links ./dist klfuncutil==$(VERSION)

test_all: testenv test_list test_tuple test_dict test_iter test_deep_copy test_repeat_iter_t test_repeat_iter_m test_tuplefactory
	@echo done

test_%:
	source ./testenv/bin/activate&&python ./$(TESTDIR)/$@.py

# --------------------------------------------------------
runtime:
	python3 -m venv runtime
	source runtime/bin/activate&&pip install -r <(grep -v '^klfuncutil @ ' requirements.txt)
	source runtime/bin/activate&&pip install -e .

install: runtime black
	$(FLIT) install

build: runtime
	$(FLIT) build

dist: build

publish: runtime black
	$(FLIT) build
	$(FLIT) publish
