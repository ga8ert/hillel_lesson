setup:
	pip3 freeze > requirements.txt
	@echo 'setup has started'
	pip3 install -r requirements.txt
	@echo 'setup has finished'
	mypy library.py
	flake8 --ignore=E501 library.py
	pytest

run: setup
	python main.py
