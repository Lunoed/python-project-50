run:
	uv run gendif

build:
	uv build

package-install:
	uv tool install --force dist/*.whl

lint:
	uv run ruff

black:
	black .
