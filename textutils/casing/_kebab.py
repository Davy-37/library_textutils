"""Kebab case conversion."""

from textutils._validation import ensure_text
from textutils.casing._words import split_words


def kebab_case(text: str) -> str:
    """Convert a string to kebab case.

    Words may be separated by spaces, hyphens, underscores or camelCase
    boundaries. Punctuation is removed and repeated separators are collapsed.

    Parameters
    ----------
    text : str
        Input text to convert.

    Returns
    -------
    str
        The text in lowercase, with words joined by hyphens. An empty or
        whitespace-only text returns an empty string.

    Raises
    ------
    TypeError
        If `text` is not a string.

    Examples
    --------
    >>> kebab_case("User Profile Settings")
    'user-profile-settings'
    >>> kebab_case("parseHTTPResponse")
    'parse-http-response'
    """
    ensure_text(text)
    return "-".join(word.lower() for word in split_words(text))
