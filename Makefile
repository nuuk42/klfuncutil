# shell
SHELL = /bin/bash
HOME =  /home/nikita/work/github/klfuncutil
PROJECTNAME =klfuncutil
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
