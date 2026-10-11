"""Word and character counters."""

from textutils._validation import ensure_text


def word_count(text: str) -> int:
    """Count the words in ``text``.

    Words are sequences of characters separated by whitespace.

    Args:
        text: The text to analyze.

    Returns:
        The number of words.

    Example:
        >>> word_count("The quick brown fox jumps")
        5
    """
    ensure_text(text)
    return len(text.split())


def character_count(text: str) -> int:
    """Count the characters in ``text``, spaces included.

    Args:
        text: The text to analyze.

    Returns:
        The number of characters.

    Example:
        >>> character_count("Hello")
        5
    """
    ensure_text(text)
    return len(text)
