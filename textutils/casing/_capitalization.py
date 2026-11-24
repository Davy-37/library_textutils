"""Capitalization helpers."""

import re

from textutils._validation import ensure_text

_WORD = re.compile(r"\S+")


def capitalize_words(text: str) -> str:
    r"""Capitalize the first letter of every word in a string.

    Words are separated by any whitespace (spaces, tabs or line breaks), which
    is preserved as is.

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
    >>> capitalize_words("red\tblue\ngreen")
    'Red\tBlue\nGreen'
    """
    ensure_text(text)
    return _WORD.sub(lambda match: match.group().capitalize(), text)
