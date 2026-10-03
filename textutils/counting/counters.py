"""Word and character counters."""


def word_count(text: str) -> int:
    """Count the words in ``text``.

    Words are sequences of characters separated by whitespace.

    Args:
        text: The text to analyze.

    Returns:
        The number of words.

    Example:
        >>> word_count("Hello Open Source!")
        3
    """
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
    return len(text)
