# textutils

A lightweight Python library for common text-processing operations.

## Features

- Word counting
- Character counting
- Text reversal
- Word capitalization
- Snake case conversion
- Text statistics

## Installation

```bash
pip install textutils
```

## Usage

```python
from textutils import word_count

count = word_count("The quick brown fox")
print(count)  # 4
```

Convert a text to snake case:

```python
from textutils import snake_case

print(snake_case("User Profile Settings"))  # user_profile_settings
print(snake_case("parseHTTPResponse"))   # parse_http_response
```

## Development

Install the project with its development tools:

```bash
pip install -e ".[dev]"
```

Run the checks before opening a pull request:

```bash
pytest --cov=textutils    # tests and coverage
black --check .           # formatting
ruff check .              # linting
```

Tests live next to the code they verify, in a `tests/` folder inside each
submodule (for example `textutils/casing/tests/`).

The public API is exposed by the `__init__.py` files; modules whose name starts
with an underscore (for example `_snake.py`) are internal implementation
details and may change without notice.

## Contributing

Contributions are welcome! Please open an issue to discuss your idea, then
submit a pull request from a dedicated branch. Make sure that the tests pass
and that Black and Ruff report no issue.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
