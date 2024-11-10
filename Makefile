# shell
SHELL = /bin/bash
HOME =  /home/nikita/work/github/klfktutil
PROJECTNAME =klfktutil
TARGETDIR = ./src/$(PROJECTNAME)
TESTDIR = ./tests
PY = source $(HOME)/runtime/bin/activate&&python
BLACK = source $(HOME)/runtime/bin/activate&&black

help:
	@echo Usage
	@echo -----
	@echo test_all
	@echo test_list
	@echo black
	@echo py - Python prompt

# open Python prompt
py:
	$(PY)
black:
	cd $(TARGETDIR)/&&$(BLACK) *.py
	cd tests/&&$(BLACK) *.py


test_all: test_list test_tuple test_dict test_iter test_deep_copy test_repeat_iter
	@echo done

test_%:
	export PYTHONPATH=$(HOME)/src&&$(PY) ./$(TESTDIR)/$@.py

##	export PYTHONPATH=$(HOME)/$(TARGETDIR)&&$(PY) ./$(TESTDIR)/$@.py
