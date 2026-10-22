# textutils

[![CI](https://github.com/Davy-37/library_textutils/actions/workflows/ci.yml/badge.svg)](https://github.com/Davy-37/library_textutils/actions/workflows/ci.yml)

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
pytest --cov=textutils      # tests and coverage
pre-commit run --all-files  # Black, Ruff and file checks
```

The public API is exposed by the `__init__.py` files; modules whose name starts
with an underscore (for example `_snake.py`) are internal implementation
details and may change without notice.

## Contributing

Contributions are welcome! Please read [CONTRIBUTING.md](CONTRIBUTING.md): open
an issue, work on a dedicated branch and submit a pull request. `main` is
protected and a pull request is merged only when the CI is green.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
