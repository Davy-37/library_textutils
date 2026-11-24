"""textutils: a lightweight library for common text-processing operations."""

from importlib.metadata import PackageNotFoundError, version

from textutils.casing import capitalize_words, snake_case
from textutils.counting import character_count, word_count
from textutils.statistics import text_statistics
from textutils.transform import reverse

try:
    __version__ = version("textutils-davy")
except PackageNotFoundError:  # pragma: no cover - source tree that is not installed
    __version__ = "unknown"

__all__ = [
    "capitalize_words",
    "character_count",
    "reverse",
    "snake_case",
    "text_statistics",
    "word_count",
]
