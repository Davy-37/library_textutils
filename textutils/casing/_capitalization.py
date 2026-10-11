"""Capitalization helpers."""

from textutils._validation import ensure_text


def capitalize_words(text: str) -> str:
    """Capitalize the first letter of every word in a string.

    Parameters
    ----------
    text : str
        Input text to convert.

    Returns
    -------
    str
        The text with each word capitalized and its other letters lowercased.

    Raises
    ------
    TypeError
        If `text` is not a string.

    Examples
    --------
    >>> capitalize_words("the quick brown fox")
    'The Quick Brown Fox'
    """
    ensure_text(text)
    return " ".join(word.capitalize() for word in text.split(" "))
