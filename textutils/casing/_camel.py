"""Camel case conversion."""

from textutils._validation import ensure_text
from textutils.casing._words import split_words


def camel_case(text: str) -> str:
    """Convert a string to camel case.

    Words may be separated by spaces, hyphens, underscores or camelCase
    boundaries. Punctuation is removed. The first word is lowercased and every
    other word is capitalized.

    Parameters
    ----------
    text : str
        Input text to convert.

    Returns
    -------
    str
        The text in camel case. An empty or whitespace-only text returns an
        empty string.

    Raises
    ------
    TypeError
        If `text` is not a string.

    Examples
    --------
    >>> camel_case("User Profile Settings")
    'userProfileSettings'
    >>> camel_case("parse_http_response")
    'parseHttpResponse'
    """
    ensure_text(text)
    first, *others = split_words(text) or [""]
    return first.lower() + "".join(word.capitalize() for word in others)
