# Changelog

All notable changes to this project are documented in this file.

The format follows [Keep a Changelog](https://keepachangelog.com/) and the
project adheres to [Semantic Versioning](https://semver.org/).

## [Unreleased]

## [1.0.0] - 2026-10-22

First stable release.

### Added
- `word_count()`, `character_count()`, `reverse()` and `capitalize_words()`.
- `snake_case()` to convert a text to snake case.
- `text_statistics()` to compute statistics about a text.
- `textutils.__version__`, read from the package metadata.
- Pull request and issue templates, and a contributing guide.
- Continuous integration with a `pre-commit` job and a `tests` job.
- The package is published on PyPI as `textutils-davy` (the import name stays
  `textutils`).

### Changed
- The public API is exposed by the `__init__.py` files; implementation modules
  are internal (prefixed with `_`).
- Public functions raise `TypeError` when the text is not a string.
- Docstrings follow the NumPy style.
- The project requires Python 3.10 or newer.

### Fixed
- `snake_case()` collapses multiple spaces, hyphens and underscores.
- The `text_statistics()` docstring example is a valid doctest.
