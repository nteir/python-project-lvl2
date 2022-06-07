install:
	poetry install

build:
	poetry build

package-install:
	python3 -m pip install --user --force dist/*.whl

make lint:
	poetry run flake8 gendiff