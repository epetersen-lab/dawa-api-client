# List the recipes (this)
default:
  just --list

# Run example_1.py from the examples directory
example_1:
  uv run examples/example_1.py

# Run example_2.py from the examples directory
example_2:
  uv run examples/example_2.py

# Run tests with pytest
test:
  uv run pytest

