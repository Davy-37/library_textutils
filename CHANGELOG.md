# Changelog

All notable changes to this project are documented in this file.

## [Unreleased]

### Added
- `word_count()`, `character_count()`, `reverse()`, `capitalize_words()` and `text_statistics()`.
- `snake_case()`.
- Black, Ruff, pytest and coverage configuration in `pyproject.toml`.

### Changed
- Implementation modules are now internal (prefixed with `_`); the public API is exposed by the `__init__.py` files.
- Public functions raise `TypeError` when the text is not a string.
- Docstrings follow the NumPy style.
- The project requires Python 3.10 or newer.
