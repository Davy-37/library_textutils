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

count = word_count("Hello Open Source!")
print(count)  # 3
```

Convert a text to snake case:

```python
from textutils import snake_case

print(snake_case("Hello Open Source!"))  # hello_open_source
print(snake_case("parseHTTPResponse"))   # parse_http_response
```

## Contributing

Contributions are welcome! Please open an issue to discuss your idea, then
submit a pull request from a dedicated branch.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
