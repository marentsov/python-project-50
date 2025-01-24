install:
	uv sync
gendiff:
	uv run gendiff
build:
	uv build
package-install:
	uv tool install dist/*.whl
make lint:
	uv run ruff check gendiff
make tests:
	uv run pytest
make tests-coverage:
	uv run pytest --cov
