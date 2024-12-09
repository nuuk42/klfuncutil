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


test_all: runtime test_list test_tuple test_dict test_iter test_deep_copy test_repeat_iter
	@echo done

test_%:
	export PYTHONPATH=$(HOME)/src&&$(PY) ./$(TESTDIR)/$@.py

runtime:
	python3 -m venv runtime
	source runtime/bin/activate&&pip install -r requirements.txt

install: runtime
	$(FLIT) install

.PHONY: build
build: runtime
	$(FLIT) build

publish: runtime
	$(FLIT) build
	$(FLIT) publish
