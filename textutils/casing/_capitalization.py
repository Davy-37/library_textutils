"""Capitalization helpers."""

from textutils._validation import ensure_text


def capitalize_words(text: str) -> str:
    """Capitalize the first letter of every word in ``text``.

    Args:
        text: The text to convert.

    Returns:
        The text with each word capitalized and the rest lowercased.

    Example:
        >>> capitalize_words("the quick brown fox")
        'The Quick Brown Fox'
    """
    ensure_text(text)
    return " ".join(word.capitalize() for word in text.split(" "))
