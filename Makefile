PYTHON = python

VENV_DIR = .venv

REQUIREMENTS = requirements.txt

SCRIPT = main.py

GREEN = \033[0;32m
RED = \033[0;31m
BLUE = \033[0;34m
YELLOW = \033[0;33m

.PHONY: all run clean run-silent

all: venv install

venv: $(VENV_DIR)
ifeq ($(OS),Windows_NT)
	$(PYTHON) -m venv $(VENV_DIR)
else
	$(PYTHON)3 -m venv $(VENV_DIR)
endif

install: venv
	$(VENV_DIR)/bin/pip install -r $(REQUIREMENTS)
	@echo "Installation complete."
	@echo "$(GREEN)To use this application, run $(YELLOW)'make run'."
	@echo "$(GREEN)To use this application with silent mode enabled, run $(YELLOW)'make run-silent'."
	@echo "$(GREEN)To clean up, run $(YELLOW)'make clean'."

run:
ifeq ($(OS),Windows_NT)
	$(VENV_DIR)\Scripts\python $(SCRIPT)
else
	sudo $(VENV_DIR)/bin/python $(SCRIPT)
endif

run-silent:
ifeq ($(OS),Windows_NT)
	$(VENV_DIR)\Scripts\python $(SCRIPT) -s
else
	sudo $(VENV_DIR)/bin/python $(SCRIPT) -s
endif

clean:
ifeq ($(OS),Windows_NT)
	rmdir /S /Q $(VENV_DIR)
	del /S /Q *.pyc __pycache__ >nul 2>&1 || exit 0
else
	rm -rf $(VENV_DIR) __pycache__ *.pyc
endif
