"""Snake case conversion."""

import re

from textutils._validation import ensure_text

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


def _split_words(text: str) -> list[str]:
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
    """
    return _WORD.findall(_split_camel_case(text))


def snake_case(text: str) -> str:
    """Convert a string to snake case.

    Words may be separated by spaces, hyphens, underscores or camelCase
    boundaries. Punctuation is removed and repeated separators are collapsed.

    Parameters
    ----------
    text : str
        Input text to convert.

    Returns
    -------
    str
        The text in lowercase, with words joined by underscores. An empty or
        whitespace-only text returns an empty string.

    Raises
    ------
    TypeError
        If `text` is not a string.

    Examples
    --------
    >>> snake_case("User Profile Settings")
    'user_profile_settings'
    >>> snake_case("parseHTTPResponse")
    'parse_http_response'
    """
    ensure_text(text)
    return "_".join(word.lower() for word in _split_words(text))
