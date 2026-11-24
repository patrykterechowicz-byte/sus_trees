lint:
    uv run basedpyright src
    uv run ruff check

test:
    uv run pytest
