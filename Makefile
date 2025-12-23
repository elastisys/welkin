VENV=.venv
PIP=$(VENV)/bin/pip3
PIP-COMPILE=$(VENV)/bin/pip-compile

.PHONY: \
	help \
	default \
	verify-prerequisites \
	install-requirements \
	serve \
	clean

help:
	@echo 'Usage: make [target] ...'
	@echo
	@echo 'Targets:'
	@grep -F -h "## " $(MAKEFILE_LIST) | grep -v grep  \
	| sed 's/^\(.*\):[^#]*##*\(.*\)/\x1b[36m\1\x1b[0m:\2/' \
	| column -t -s ':'

default: help

verify-prerequisites: ## Verify that needed prerequisites are installed
	python3 --version
	@echo
	@echo "All prerequisites seem to be installed."

$(PIP):
	python3 -m venv .venv

$(PIP-COMPILE): $(PIP)
	$(PIP) install pip-tools

requirements.txt: requirements.in $(PIP-COMPILE)
	$(PIP-COMPILE) requirements.in

$(VENV)/.stamp: requirements.txt $(PIP)
	$(PIP) install -r requirements.txt
	touch $@

install-requirements: $(VENV)/.stamp ## Install requirements in virtual environment

docs/stylesheets/style.css: extra_sass/style.css.scss
	npx sass@1 $^:$@

legacy-images: ## Regenerate some legacy images in docs/img
	$(MAKE) -C docs/img

css: docs/stylesheets/style.css ## Regenerate CSS

serve: install-requirements ## Serve the website locally with live reload
	$(VENV)/bin/mkdocs serve

serve-with-version: install-requirements ## Serve the website locally with versions
	@echo "⚠️ WARNING: This workflow does not support live reload."
	. $(VENV)/bin/activate && mike deploy welkin -t main
	. $(VENV)/bin/activate && mike serve

clean:
	rm -rf .cache .venv site/
