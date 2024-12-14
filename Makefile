# shell
SHELL = /bin/bash
HOME =  /home/nikita/work/github/klfuncutil
PROJECTNAME =klfuncutil
TARGETDIR = ./src/$(PROJECTNAME)
TESTDIR = ./tests
SETUPENV =source $(HOME)/runtime/bin/activate
PY = $(SETUPENV)&&python
BLACK = $(SETUPENV)&&black
FLIT = $(SETUPENV)&&flit

help:
	@echo Usage
	@echo -----
	@echo make test_all
	@echo make test_list
	@echo make black
	@echo make py - Python prompt
	@echo make install - install package klfuncutil locally
	@echo make publish - publish a new version on pypi

# open Python prompt
py: runtime
	$(PY)

black: runtime
	cd $(TARGETDIR)/&&$(BLACK) *.py
	cd tests/&&$(BLACK) *.py

# --------------------------------------------------------

.PHONY testenv:
testenv: build
	-rm -Rf testenv
	python3 -m venv testenv
	source ./testenv/bin/activate&&pip install ./dist/klfuncutil-1.0.2-py2.py3-none-any.whl

test_all: testenv test_list test_tuple test_dict test_iter test_deep_copy test_repeat_iter_t test_repeat_iter_m
	@echo done

test_%:
	source ./testenv/bin/activate&&python ./$(TESTDIR)/$@.py

# --------------------------------------------------------
runtime:
	python3 -m venv runtime
	source runtime/bin/activate&&pip install -r requirements.txt

install: runtime black
	$(FLIT) install

.PHONY: build
build: runtime
	$(FLIT) build

publish: runtime black
	$(FLIT) build
	$(FLIT) publish
