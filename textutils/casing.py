"""Functions that change the casing of a text."""


def capitalize_words(text: str) -> str:
    """Capitalize the first letter of every word in ``text``.

    Args:
        text: The text to convert.

    Returns:
        The text with each word capitalized and the rest lowercased.

    Example:
        >>> capitalize_words("hello open source")
        'Hello Open Source'
    """
    return " ".join(word.capitalize() for word in text.split(" "))
