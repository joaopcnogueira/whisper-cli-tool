all: build upload

build:
	# create source distribution
	python setup.py sdist

upload:
	# upload to PyPI
	twine upload dist/*

install:
	# install locally
	pip install -e .
