install:
	python -m pip install --upgrade pip && pip install -r requirements.txt

test:
	python -m unittest

lint:
	pylint scripts --disable=E1120