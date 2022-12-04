freeze_req:
	pip freeze > requirements.txt

setup:
	pip install wikipedia
	@echo 'setup has started'
	pip install -r requirements.txt
	@echo 'setup has finished'

check:
	mypy main.py
	flake8 --ignore=E501 main.py

setup_check: setup
	mypy main.py
	flake8 --ignore=E501 main.py

run: setup check test
	python main.py

test:
	pytest

all:
	@echo 'You will be happy'