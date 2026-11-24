"""Word splitting shared by the case conversion functions."""

import re

_CAMEL_BOUNDARY = re.compile(r"(?<=[a-z0-9])(?=[A-Z])|(?<=[A-Z])(?=[A-Z][a-z])")
_WORD = re.compile(r"[^\W_]+")


def _split_camel_case(text: str) -> str:
    """Insert a space at each camelCase boundary of a text.

    Parameters
    ----------
    text : str
        Text to split, for example ``"HTTPServerError"``.

    Returns
    -------
    str
        The text with spaces at the boundaries, for example
        ``"HTTP Server Error"``.
    """
    return _CAMEL_BOUNDARY.sub(" ", text)


def split_words(text: str) -> list[str]:
    """Split a text into words, whatever the separators used.

    Words can be separated by spaces, hyphens, underscores, punctuation or
    camelCase boundaries.

    Parameters
    ----------
    text : str
        Text to split.

    Returns
    -------
    list of str
        The words of the text, without any separator.

    Examples
    --------
    >>> split_words("parseHTTPResponse")
    ['parse', 'HTTP', 'Response']
    >>> split_words("user-profile_settings")
    ['user', 'profile', 'settings']
    """
    return _WORD.findall(_split_camel_case(text))
