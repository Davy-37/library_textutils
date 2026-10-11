"""textutils: a lightweight library for common text-processing operations."""

from textutils.casing import capitalize_words, snake_case
from textutils.counting import character_count, word_count
from textutils.statistics import text_statistics
from textutils.transform import reverse

__all__ = [
    "capitalize_words",
    "character_count",
    "reverse",
    "snake_case",
    "text_statistics",
    "word_count",
]
__version__ = "0.1.0"
