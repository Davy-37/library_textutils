"""textutils: a lightweight library for common text-processing operations."""

from textutils.casing import capitalize_words
from textutils.transform import character_count, reverse, word_count

__all__ = ["word_count", "character_count", "reverse", "capitalize_words"]
__version__ = "0.1.0"
