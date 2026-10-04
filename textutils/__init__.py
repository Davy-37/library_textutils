"""textutils: a lightweight library for common text-processing operations."""

from textutils.casing import capitalize_words, snake_case
from textutils.counting import character_count, word_count
from textutils.transform import reverse
from textutils.statistics import text_statistics

__all__ = ["word_count", "character_count", "reverse", "capitalize_words", "snake_case", "text_statistics"]
__version__ = "0.1.0"
