check:
	black rgwaspy --check
	isort -c rgwaspy
	flake8 rgwaspy

dev:
	pip install -r requirements-dev.txt
	pre-commit install

env:
	conda env create -f environment.yaml

fix:
	black rgwaspy
	isort rgwaspy

update-env:
	conda env update -f environment.yaml -prune

.PHONY: check dev env fix update-env
