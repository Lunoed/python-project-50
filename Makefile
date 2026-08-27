install:
	uv venv

build:
	vu build

package-install:
	uv tool install --force sdist/*.whl

lint:
	uv run ruff check ...

black:
	black .
	