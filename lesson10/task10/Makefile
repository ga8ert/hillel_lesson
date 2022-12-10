setup:
	@echo 'setup has started'
	pip install -r requirements.txt
	@echo 'setup has finished'
	mypy library.py
	flake8 --ignore=E501 library.py
	pytest

run: setup
	python main.py
