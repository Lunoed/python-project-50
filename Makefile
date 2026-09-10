.PHONY: tests

install:
	uv sync

build:
	uv build

package-install:
	uv tool install --force dist/*.whl

lint:
	uv run ruff check gendiff

black:
	black .
	
test-coverage:
	uv run pytest --cov=gendiff --cov-report term --cov-report xml

tests:
	uv run pytest
	
