all:
	# create source distribution
	python setup.py sdist
	# upload to PyPI
	twine upload dist/* 